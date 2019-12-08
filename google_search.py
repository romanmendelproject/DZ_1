# -*- coding: utf-8 -*-
import requests,sys
from bs4 import BeautifulSoup

def request(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml" )
    return soup

def recursion(link,req_num):
    soup_req=request(link)
    links_req=list()
    link_number=0
    for link_req in soup_req.find_all('a'):
        if req_num > link_number:
            link_req_item = link_req.get('href')
            if len(str(link_req_item))>4 and link_req_item[:4] == 'http':
                links_req.append(link_req_item)
                link_number+=1
            else:
                continue
        else:
            break
    return links_req

def pars_google(search_text,number_reursion):
    with open('result.txt', 'w', encoding='utf-8') as output_file:
        url='https://www.google.com/search?q={}'.format(search_text)
        soup=request(url)
        if number_reursion:
            for i,tag in enumerate(soup.find_all("div", {"class": "g"})):
                if i<7:
                    link = tag.find('a').get('href')
                    result_main = "ОПИСАНИЕ:\n{}\nОСНОВНАЯ ССЫЛКА:\n{}\n".format(tag.text,link)
                    output_file.write(result_main)
                    rec = recursion(link,number_reursion)
                    output_file.write("РЕКУРСИВНЫЕ ССЫЛКИ:\n")
                    for rec_item in rec:
                        output_file.write("{}\n".format(rec_item))
                    output_file.write("\n\n")
                else:
                    break
        else:
            for i,tag in enumerate(soup.find_all("div", {"class": "g"})):
                if i<7:
                    link = tag.find('a').get('href')
                    result_main = "ОПИСАНИЕ:\n{}\nОСНОВНАЯ ССЫЛКА:\n{}\n\n".format(tag.text,link)
                    output_file.write(result_main)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Ошибка. Слишком мало параметров!")
        sys.exit (1)
    elif len(sys.argv) == 2:
        pars_google(sys.argv[1],0)
    elif len(sys.argv) == 3:
        try:
            pars_google(sys.argv[1],int(sys.argv[2]))
        except ValueError:
            print("Ошибка. Укажите целое число!")
            sys.exit(1)
    else:
        print("Ошибка. Слишком много параметров!")
        sys.exit(1)
