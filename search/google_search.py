import requests
from bs4 import BeautifulSoup
from constants import User_Agent


def request(url):
    headers = {'User-Agent': User_Agent}
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, "lxml")


def recursion(link, req_num):
    soup_req = request(link)
    links_req = list()
    link_number = 0
    for link_req in soup_req.find_all('a'):
        if req_num > link_number:
            link_req_item = link_req.get('href')
            if len(str(link_req_item)) > 4 and link_req_item[:4] == 'http':
                links_req.append(link_req_item)
                link_number += 1
            else:
                continue
        else:
            break
    return links_req


def pars_google(search_text, number_reursion):
    with open('result.txt', 'w', encoding='utf-8') as output_file:
        url = 'https://www.google.com/search?q={}'.format(search_text)
        soup = request(url)
        if number_reursion:
            for i, tag in enumerate(soup.find_all("div", {"class": "g"})):
                if i < 7:
                    link = tag.find('a').get('href')
                    result_main = f"ОПИСАНИЕ:\n{tag.text}\n\
                    ОСНОВНАЯ ССЫЛКА:\n{link}\n"
                    output_file.write(result_main)
                    rec = recursion(link, number_reursion)
                    output_file.write("РЕКУРСИВНЫЕ ССЫЛКИ:\n")
                    for rec_item in rec:
                        output_file.write(f"{rec_item}\n")
                    output_file.write("\n\n")
                else:
                    break
        else:
            for i, tag in enumerate(soup.find_all("div", {"class": "g"})):
                if i < 7:
                    link = tag.find('a').get('href')
                    result_main = f"ОПИСАНИЕ:\n{tag.text}\n\
                    ОСНОВНАЯ ССЫЛКА:\n{link}\n\n"
                    output_file.write(result_main)
