import requests
import validators
import socket
import logging
from bs4 import BeautifulSoup
from constants import User_Agent


def request(url):
    headers = {'User-Agent': User_Agent}
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.content, "lxml")


def recursion(link, req_num):
    links_req = list()
    link_number = 0
    try:
        soup_req = request(link)
    except socket.error:
        return 'link_error'
    for link_req in soup_req.find_all('a'):
        link_req_item = str(link_req.get('href'))
        if validators.url(link_req_item) and link_number < req_num:
            links_req.append(link_req_item)
            link_number += 1
        else:
            continue
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
                    if rec == 'link_error':
                        output_file.write("Ресурс недоступен!\n\n\n")
                        continue
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
