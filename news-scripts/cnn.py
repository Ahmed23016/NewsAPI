import requests
from bs4 import BeautifulSoup

def get_url(topic):
    base_url = "https://edition.cnn.com"
    query = topic.replace(" ", "+")
    return f"{base_url}/search?q={query}&from=0&size=10&page=1&sort=newest&types=all&section="

topic = "trump crypto"
print(get_url(topic))


re=requests.get(get_url(topic))
print(re.status_code)
with open("index.html","w",encoding="utf-8") as f:
    f.write(re.text)