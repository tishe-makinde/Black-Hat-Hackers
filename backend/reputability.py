import json
from webScraper import webScraper
from google import genai

class linkCreditability:
    def __init__(self, link):
        self.link = link
        self.scraper = webScraper(self.link)
        self.result = ""

    def formatContent(self):
        self.result = self.scraper.scrape()
        return self.result

    def generateContentSummaries(self, url):
        # Extract publisher domain
        try:
            publisher = url.split("/")[2]
        except:
            publisher = "unknown"

        if not self.result:
            return ""

        content_json = json.loads(self.result)
        if not content_json:
            return ""

        paragraphs = content_json[0].get("paragraphs", [])
        stringContent = " ".join(paragraphs)

        client = genai.Client(api_key="AIzaSyDDr7H0NdM4PF4-JeHxIc-DLeQl1D27YwY")
        prompt = (
            "Use two or three words to estimate the reputability of an article based on its content: "
            + stringContent
            + f" and article's publisher: {publisher}. Give a score from 1 to 10 as well. Put all text in a dictionary format as so: "
            + " {'reputation': value, 'score': value}"
        )
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"AI generation failed: {e}")
            return "Unable to generate summary."
