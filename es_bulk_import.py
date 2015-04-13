from datetime import datetime
#from elasticsearch import Elasticsearch
import os
import requests
import time

ll_rel = '~/latin_text_latin_library/'
ll = os.path.expanduser(ll_rel)
ll_contents =  os.listdir(ll)

ip_port = 'http://104.131.178.18:9200/'


def ll_es_input(author_name, file_name, contents, count):
    url = ip_port + 'texts/text/' + str(count)
    data = {"author": author_name,
            "title": file_name,
            "text": contents,
            "date": str(datetime.utcnow())}
    print(url)
    print(author_name, file_name)
    requests.post(url, json=data)
    #time.sleep(1)


def open_file(filepath):
    with open(filepath, 'rb') as f:
        return str(f.read())


def crawl_ll():
    count = 0
    for x in ll_contents:
        file_or_dir = os.path.join(ll, x)
        if os.path.isfile(file_or_dir):
            author_file_name = file_or_dir.split('/')[-1][:-4]
            if '.' in author_file_name:
                count += 1
                author_name = author_file_name.split('.')[0]
                text_title = author_file_name.split('.')[1]
                contents = open_file(file_or_dir)
                ll_es_input(author_name, text_title, contents, count)
        elif os.path.isdir(file_or_dir) and not file_or_dir.split('/')[-1] == '.git':
            author_name = file_or_dir.split('/')[-1]
            author_dir_contents = os.listdir(file_or_dir)
            for text_file in author_dir_contents:
                count += 1
                text_file_path = os.path.join(file_or_dir, text_file)
                text_title = text_file[:-4]
                contents = open_file(text_file_path)
                ll_es_input(author_name, text_title, contents, count)

if __name__ == '__main__':
    crawl_ll()