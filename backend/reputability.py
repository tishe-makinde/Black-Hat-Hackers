import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google import genai
from webScraper import webScraper
import json

class linkCreditability:
    def __init__(self, link):
        self.link = link
        self.scraper = webScraper(self.link)
        self.result = ""
    def formatContent(self):
        # use web scraper class to get content
        self.result = self.scraper.scrape()
        # format it so that 
        return self.result


    def generateContentSummaries(self, url):
        client = genai.Client(api_key="AIzaSyDDr7H0NdM4PF4-JeHxIc-DLeQl1D27YwY")
        formatContent = json.loads(self.result)

        stringContent = ""

        content = formatContent[0]["paragraphs"]

        for item in content:
            stringContent = stringContent + " " + item
        
        

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents="Generate a 100 word summary, without any information added or removed, based on:" + stringContent
        )

        return response.text


        


# docs = [
#     "AI is transforming the world.",
#     "AI is not transforming the world"
# ]



# vectorizer = TfidfVectorizer().fit_transform(docs)
# similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
# print(similarity[0][0])

