import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import re


def search_question(question):
    search_url = "https://www.google.com/search?q=site:stackoverflow.com+{}"
    response = requests.get(search_url.format(question))
    html = pq(response.text)
    href = html('.r')('a')[0].attrib["href"]
    question_url = re.search("q=(.*?)&", href).group(1)
    return question_url

def get_answer(url):
    response = requests.get(url)
    print(type(response.text))
    soup = BeautifulSoup(response.text, 'html.parser')
    accepted_answer = soup.find('div', {'class' : 'accepted-answer'})
    print(type(accepted_answer))
    if accepted_answer is not None:
        return accepted_answer.find('div', {'class' : 'post-text'})

    return soup.find('div', {'class' : 'post-text'})
    # soup = BeautifulSoup(accepted_answer, 'html.parser')


def main():
    question = "length of list python"
    question_url = search_question(question)
    answer = get_answer(question_url)
    print(answer)


main()
