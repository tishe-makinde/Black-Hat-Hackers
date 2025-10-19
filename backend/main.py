from reputability import linkCreditability
from ddgs import DDGS
from googleapiclient.discovery import build
import json
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resultOfQuery = False

urlInfos = []
summaries = []
userInfo = {
    "title": "",
    "description": ""
}
userSummary = ""

while resultOfQuery == False:
    userLink = input("Enter a valid link to check credibility: ")

    creditabilityScore = linkCreditability(userLink)
    userLinkJson = creditabilityScore.formatContent()

    userNewLink = json.loads(userLinkJson)
    try:
        userLinkTitle = userNewLink[0]["title"]
        userLinkDescription = userNewLink[0]["description"]
        userInfo["title"] = userLinkTitle
        userInfo["description"] = userLinkDescription
        userSummary = creditabilityScore.generateContentSummaries(userLink)
        resultOfQuery = True
    except:
        pass



def returnURLInfo(url):
    creditabilityScore = linkCreditability(url)

    linkJson = creditabilityScore.formatContent()
    newLink = json.loads(linkJson)

    if len(newLink) > 0:
        item = {
        "title": newLink[0]["title"],
        "description": newLink[0]["description"]
        }
        urlInfos.append(item)
        summary = creditabilityScore.generateContentSummaries(url)
        summaries.append(summary)
    else:
        pass

    

similarLinks = []
results = DDGS().text(userLinkTitle, max_results=10)
for result in results:
   similarLinks.append(result["href"]) 

for link in similarLinks:
    if "youtube" not in link:
        returnURLInfo(link)

titleScores = []
descriptionScores = []
contentScores = []

def calculateSimilarities(item, data):
    docs = []
    if item["description"] is not None:
        docs.append(userInfo[data])
        docs.append(str(item[data]))
        vectorizer = TfidfVectorizer().fit_transform(docs)
        similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
        if similarity[0][0] < 0.001 or similarity[0][0] > 0.99:
            item["description"] = 1
            item["title"] = 1
        else:    
            if data == "title":
                titleScores.append(similarity[0][0])
            else:
                descriptionScores.append(similarity[0][0])
    else:
        pass


for item in urlInfos:
    calculateSimilarities(item, "title")
    calculateSimilarities(item, "description")

def compareSentences(sentenceOne, sentenceTwo):
    docs = [sentenceOne, sentenceTwo]

    vectorizer = TfidfVectorizer().fit_transform(docs)
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
    negationWords = ["not", "never", "no", "none", "neither"]
    countOne = 0
    countTwo = 0

    for word in sentenceOne:
        if word in negationWords:
            countOne += 1

    for word in sentenceTwo:
        if word in negationWords:
            countTwo += 1

    if abs(countOne - countTwo) % 2 == 1:
        return similarity[0][0] * 0.5
    else:
        return similarity[0][0] 


def compareContent():
    splitUserContent = userSummary.split(".")
    for summary in summaries:
        overallSimilarity = 0
        splitSummaryContent = summary.split(".")
        for userSentence in splitUserContent:
            for similarSentence in splitSummaryContent:
                if len(userSentence) > 0 and len(similarSentence) > 0:
                    similarity = compareSentences(userSentence, similarSentence)
                    overallSimilarity += similarity
        
        contentScores.append(overallSimilarity)

averageTitleScore = 0
averageDescriptionScore = 0
averageContentScore = 0
compareContent()
titleScores.sort()
if len(titleScores) % 2 == 1:
    averageTitleScore = titleScores[len(titleScores)//2]
    print(f"Average score is {averageTitleScore}")
else:
    averageTitleScore = (titleScores[len(titleScores)//2] + titleScores[(len(titleScores)//2) - 1]) / 2
    print(f"Average score is {averageTitleScore}")

descriptionScores.sort()
if len(descriptionScores) % 2 == 1:
    averageDescriptionScore = descriptionScores[len(descriptionScores)//2]
    print(f"Average score is {averageDescriptionScore}")
else:
    averageDescriptionScore = (descriptionScores[len(descriptionScores)//2] + descriptionScores[(len(descriptionScores)//2) - 1]) / 2
    print(f"Average score is {averageDescriptionScore}")

if len(contentScores) % 2 == 1:
    averageContentScore = contentScores[len(contentScores)//2]
    print(f"Average score is {averageContentScore}")
else:
    averageContentScore = (contentScores[len(contentScores)//2] + contentScores[(len(contentScores)//2) - 1]) / 2
    print(f"Average score is {averageContentScore}")

overall_score = numpy.median([averageTitleScore, averageDescriptionScore, averageContentScore])

