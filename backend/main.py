from reputability import linkCreditability
from ddgs import DDGS
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SourceVerification:
    def __init__(self, link):
        self.link = link
        self.urlInfos = []
        self.summaries = []
        self.userInfo = {"title": "", "description": ""}
        self.userSummary = ""
        self.resultOfQuery = False
        self.titleScores = []
        self.descriptionScores = []
        self.contentScores = []

    def getLink(self):
        while not self.resultOfQuery:
            creditabilityScore = linkCreditability(self.link)
            userLinkJson = creditabilityScore.formatContent()

            try:
                userNewLink = json.loads(userLinkJson)
                self.userInfo["title"] = userNewLink[0]["title"]
                self.userInfo["description"] = userNewLink[0]["description"]
                self.userSummary = creditabilityScore.generateContentSummaries(self.link)
                self.resultOfQuery = True
            except Exception as e:
                print("Failed to retrieve content. Try another link.", e)

    def returnURLInfo(self, url):
        creditabilityScore = linkCreditability(url)
        linkJson = creditabilityScore.formatContent()
        newLink = json.loads(linkJson)
        if newLink:
            self.urlInfos.append({
                "title": newLink[0]["title"],
                "description": newLink[0]["description"]
            })
            summary = creditabilityScore.generateContentSummaries(url)
            self.summaries.append(summary)

    def findSimilarLink(self):
        similarLinks = []
        results = DDGS().text(self.userInfo["title"], max_results=10)
        for result in results:
            href = result.get("href")
            if href and "youtube" not in href:
                similarLinks.append(href)

        for link in similarLinks:
            self.returnURLInfo(link)

        for item in self.urlInfos:
            self.calculateSimilarities(item, "title")
            self.calculateSimilarities(item, "description")

        self.compareContent()

        avgTitle = self.median(self.titleScores)
        avgDesc = self.median(self.descriptionScores)
        avgContent = self.median(self.contentScores)

        overall = np.median([avgTitle, avgDesc, avgContent])

        # Store results as attributes
        self.scores = {
            "title": avgTitle,
            "description": avgDesc,
            "content": avgContent,
            "overall": overall
        }

        # Print results for CLI users
        print(f"Title: {avgTitle:.3f}, Description: {avgDesc:.3f}, Content: {avgContent:.3f}")
        print(f"Overall credibility: {overall:.3f}")

        # Return results for external use
        return self.scores


    def calculateSimilarities(self, item, key):
        if item[key]:
            docs = [self.userInfo[key], str(item[key])]
            vectorizer = TfidfVectorizer().fit_transform(docs)
            similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
            if 0.001 < similarity < 0.99:
                if key == "title":
                    self.titleScores.append(similarity)
                else:
                    self.descriptionScores.append(similarity)

    def compareSentences(self, s1, s2):
        docs = [s1, s2]
        vectorizer = TfidfVectorizer().fit_transform(docs)
        similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]
        negationWords = {"not", "never", "no", "none", "neither"}
        count1 = sum(word.lower() in negationWords for word in s1.split())
        count2 = sum(word.lower() in negationWords for word in s2.split())
        if abs(count1 - count2) % 2 == 1:
            similarity *= 0.5
        return similarity

    def compareContent(self):
        splitUser = [s.strip() for s in self.userSummary.split(".") if s.strip()]
        for summary in self.summaries:
            splitSummary = [s.strip() for s in summary.split(".") if s.strip()]
            overall = 0
            for u_sent in splitUser:
                for s_sent in splitSummary:
                    overall += self.compareSentences(u_sent, s_sent)
            if splitUser and splitSummary:
                overall /= (len(splitUser) * len(splitSummary))
            self.contentScores.append(overall)

    def median(self, scores):
        return float(np.median(scores)) if scores else 0


if __name__ == "__main__":
    app = SourceVerification("https://example.com")
    app.getLink()
    app.findSimilarLink()
