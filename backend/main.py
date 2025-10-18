from reputability import linkCreditability
from ddgs import DDGS
import json
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

userLink = input("Enter a link to a website: ")

# Get metadata for the main link
creditabilityScore = linkCreditability(userLink)
userLinkJson = creditabilityScore.formatContent()
userNewLink = json.loads(userLinkJson)

userLinkTitle = userNewLink[0]["title"]
userLinkDescription = userNewLink[0]["description"]

# Fetch similar links via DDGS
similarLinks = []
results = DDGS().text(userLinkTitle, max_results=10)
for result in results:
    similarLinks.append(result["href"])

# Function to extract text from a webpage
def extract_text(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        return text
    except Exception:
        return ""  # skip if fetch fails

# Collect all page texts
texts = [extract_text(userLink)]  # main link first
for link in similarLinks:
    texts.append(extract_text(link))

# Vectorize the texts
vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)
tfidf_matrix = vectorizer.fit_transform(texts)

# Compute cosine similarities
similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Display results
 
for link, score in zip(similarLinks, similarities):
    print(f"{link}  →  Similarity: {score:.3f}")
