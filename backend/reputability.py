import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google import genai
from webScraper import WebScraper

class linkCreditability:
    def __init__(self, link):
        self.link = link

    def formatContent(self):
        # use web scraper class to get content
        webScraper = WebScraper()
        result = webScraper.scrape("https://quotes.toscrape.com")
        # format it so that 
        print(result)


creditabilityScore = linkCreditability("https://quotes.toscrape.com")

creditabilityScore.formatContent()


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

