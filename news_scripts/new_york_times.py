from bs4 import BeautifulSoup
import requests
from .commons import write_to_html,filter_topic
from playwright.sync_api import sync_playwright

base_url="https://www.nytimes.com"

def get_articles(topic):
    re=requests.get(f"https://www.nytimes.com/search?dropmab=false&lang=en&query={topic}&sort=best")
    write_to_html(re.text)
    soup=BeautifulSoup(re.content,"html.parser")
    art=[]
    articles= soup.find_all("div","css-1i8vfl5")
    for i in articles:
        art.append({"Title":i.find("h4","css-nsjm9t").text,"URL":base_url+i.find("a").get("href")})
    content=scrape_article(art[0]["URL"])
    return content

def scrape_article(url):

    soup=None
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()
        
        page.goto(url)
        
        
        page.wait_for_selector("div.css-53u6y8")
        write_to_html(page.content())

        soup=BeautifulSoup(page.content(),"html.parser")
        browser.close()
    div=soup.find("div",class_="css-53u6y8")
    return div.text