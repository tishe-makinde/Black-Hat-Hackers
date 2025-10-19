from reputability import linkCreditability
from ddgs import DDGS
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
        print(item)
        summary = creditabilityScore.generateContentSummaries(url)
        summaries.append(summary)
    else:
        pass

    

similarLinks = []
results = DDGS().text(userLinkTitle, max_results=15)
for result in results:
   similarLinks.append(result["href"]) 

for link in similarLinks:
    if "youtube" not in link:
        returnURLInfo(link)



scores = []

for item in urlInfos:
    docs = []
    docs.append(userInfo["title"])
    docs.append(item["title"])
    vectorizer = TfidfVectorizer().fit_transform(docs)
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
    print(similarity[0][0])
    if similarity[0][0] < 0.001 or similarity[0][0] > 0.99:
        pass
    else:    
        scores.append(similarity[0][0])

scores.sort()
if len(scores) % 2 == 1:
    print(f"Average score is {scores[len(scores)//2]}")
else:
    print(f"Average score is {(scores[len(scores)//2] + scores[len(scores) - 1]) / 2}")

