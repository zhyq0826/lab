import requests
import time


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


def block_task():
    time.sleep(10)
    return 'finish'


def timeout_task():
    time.sleep(20)
