import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.linkedin.com/jobs/search?keywords=Dev&location=Utah%20County%2C%20Utah%2C%20United%20States&geoId=100107366&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

def get_text_element(bs, tag, class_=None):
    result = bs.find(tag, class_=class_)
    if result:
        return result.text.strip()
    return ''

def element(bs, tag, class_=None):
    result = bs.find(tag, class_=class_)
    return result

if not os.path.exists('utah.html'):
    print("Loading page from the internet...")
    page = requests.get(url, headers=HEADERS)
    page_content = page.content.decode()

    with open('utah.html', 'w') as outfile:
        outfile.write(page_content)
else:
    print("Reading html from file...")
    with open('utah.html', 'r') as infile:
        page = infile.read()
    page_content = page.encode('utf-8')

soup = BeautifulSoup(page_content, 'html.parser')

link_soup = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

for link in link_soup:
    title = get_text_element(link, 'span', class_="sr-only")
    location = get_text_element(link, 'span', class_="job-search-card__location")
    links=element(link, 'a', class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]")

    if title:
        print(f'Title: {title} \nLocation: {location} \nLink: {links.get("href")}\n')