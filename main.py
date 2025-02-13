# main.py

from news_scripts.google import main as google_search
from news_scripts.new_york_times import get_articles as nyt_get_articles
from news_scripts.economic_times import get_articles as et_get_articles
from news_scripts.complex import get_articles as complex_get_articles
from news_scripts.commons import *

WATCHLIST = ["The New York Times", "The Economic Times", "Complex"]

def main(topic):
    print(f"=== Scraping Articles for Topic: '{topic}' ===\n")
    all_articles = []

    for author in WATCHLIST:
        search_query = f"{topic} {author}"
        print(f"--- Searching Google News for: '{search_query}' ---")
        
        google_results = google_search(search_query) 
        

        for idx, item in enumerate(google_results, start=1):
            title = item.get("Title", "").strip()
            result_author = item.get("Author", "").strip()
            print(f"Result #{idx}: '{title}' by {result_author}")

            if result_author == author:
                print(f"  --> '{author}' is in watchlist, scraping this article...")
                if author == "The New York Times":
                    scraped_content = nyt_get_articles(topic)
                elif author == "The Economic Times":
                    scraped_content = et_get_articles(topic)
                elif author == "Complex":
                    scraped_content = complex_get_articles(topic)
                else:
                    scraped_content = None  
                if scraped_content:
                    all_articles.append({
                        "source": author,
                        "title": title,
                        "topic": topic,
                        "content": scraped_content
                    })
                    print(f"    --> Successfully scraped article: '{title}'\n")
                else:
                    print(f"    --> Failed to scrape article: '{title}'\n")
            else:
                print(f"  --> Author mismatch. Expected '{author}', but found '{result_author}'. Skipping...\n")

    print("\n=== Final Scraped Articles ===")
    if not all_articles:
        print("No articles were scraped based on the given topic and watchlist.")
    else:
        for idx, article in enumerate(all_articles, start=1):
            print(f"\nArticle #{idx} from '{article['source']}' about '{article['topic']}':")
            print(f"Title: {article['title']}")
            print(f"Content:\n{article['content']}")
            print("-" * 40)

if __name__ == "__main__":
    test_topic = "Hawk Tuah"
    main(test_topic)
