import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google import genai
from webScraper import webScraper

class linkCreditability:
    def __init__(self, link):
        self.link = link
        self.scraper = webScraper(self.link)

    def formatContent(self):
        # use web scraper class to get content
        result = self.scraper.scrape()
        # format it so that 
        return result
# errorMessage = "Make sure your link is valid"
# webContent = []
# try:
#     userLink = input("Enter a link to check credibility: ")
# except:
#     print(errorMessage)
#     userLink = input("Enter a link to check credibility: ")




# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.5-flash-lite", contents="Explain how AI works in a few words"
# )
# print(response.text)


# docs = [
#     "AI is transforming the world.",
#     "AI is not transforming the world"
# ]



# vectorizer = TfidfVectorizer().fit_transform(docs)
# similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
# print(similarity[0][0])

