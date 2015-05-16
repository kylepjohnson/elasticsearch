from datetime import datetime
#from elasticsearch import Elasticsearch
from json import dumps
import os
import requests
import time
from urllib.parse import urljoin

ll_rel = '~/latin_text_latin_library/'
ll = os.path.expanduser(ll_rel)
ll_contents =  os.listdir(ll)


#ip_port = 'http://104.131.178.18:9200/'
es_server = 'http://localhost'
es_port = 9200

def ll_es_input(author_name, file_name, contents, count):
    url = ip_port + 'texts/text/' + str(count)
    data = {"author": author_name,
            "title": file_name,
            "text": contents,
            "date": str(datetime.utcnow())}
    print(url)
    print(author_name, file_name)
    requests.post(url, json=data)
    time.sleep(1)


def open_file(filepath):
    with open(filepath, 'r') as f:
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


def is_in_index(data, url, count=0):
    count += 1
    try:
        request = requests.get(url)
        if request.status_code not in [200, 404] and count < 4:
            is_in_index(data, url, count)
            if count > 1:
                print(url, count)
    except ConnectionError:
        print('Elasticsearch seems to be turned off: {0}'.format(ConnectionError))
        #raise
    if request.status_code == 200:
        return True
    elif request.status_code == 404:
        return False


def post_to_es(data, url, file_name=None):
    count = 0
    in_index = is_in_index(data, url)
    #print('Is in index already? {0}'.format(in_index))
    if in_index is True:
        pass
    elif in_index is False:
        try:
            count += 1
            request = requests.post(url, json=data)
            if count < 4 and request.status_code not in [200, 201]:
                print('Post failed. Trying again …')
                post_to_es(data, url)
        except Exception as e:
            print(e, url, file_name)  # ('Connection aborted.', OSError(41, 'Protocol wrong type for socket')) http://localhost:9200/text/tlg/1242 TLG2062.TXT


def build_post(text, index_path, id_tlg, count):
    url = es_server + ':' + str(es_port) + '/' + index_path + '/' + str(count)
    assert isinstance(text, str)
    data = {"text": text,
            "id_tlg": id_tlg}
    return data, url


def load_tlg():
    tlg_dir_rel = '~/cltk_data/greek/text/tlg/plaintext/'
    tlg_dir = os.path.expanduser(tlg_dir_rel)
    tlg_files = os.listdir(tlg_dir)
    tlg_files = [x for x in tlg_files if x.startswith('TLG')]
    count = 0
    for tlg_file in tlg_files:
        count += 1
        tlg_file_contents = open_file(tlg_dir + tlg_file)
        tlg_id = tlg_file[:-4]
        if count % 100 == 0:
            print(count)
        post_data, uri = build_post(tlg_file_contents, 'text/tlg', tlg_id, count)
        post_to_es(post_data, uri, tlg_file)
        #input()



if __name__ == '__main__':
    load_tlg()