import requests

def get_news():
    # Example API call to a news service
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=your_news_api_key")
    articles = response.json().get("articles", [])
    if articles:
        headlines = [article["title"] for article in articles[:5]]
        return "\n".join(headlines)
    return "Sorry, I couldn't fetch the latest news at the moment."
