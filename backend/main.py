from reputability import linkCreditability
from ddgs import DDGS
import json

API_KEY = "AIzaSyDDr7H0NdM4PF4-JeHxIc-DLeQl1D27YwY"

userLink = input("Enter a link to a website: ")

urlInfos = []

creditabilityScore = linkCreditability(userLink)

userLinkJson = creditabilityScore.formatContent()
userNewLink = json.loads(userLinkJson)

userLinkTitle = userNewLink[0]["title"]
userLinkDescription = userNewLink[0]["description"]

def returnURLInfo(url):
    creditabilityScore = linkCreditability(url)

    linkJson = creditabilityScore.formatContent()
    newLink = json.loads(linkJson)

    linkTitle = newLink[0]["title"]
    linkDescription = newLink[0]["description"]

    urlInfo = {"title": linkTitle, "description": linkDescription, "url": url}

    urlInfos.append(urlInfo)

similarLinks = []
results = DDGS().text(userLinkTitle, max_results=10)
for result in results:
   similarLinks.append(result["href"]) 

for link in similarLinks:
    print(link)


print(urlInfos)



