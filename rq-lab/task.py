import requests


def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())


def block_task():
    import time
    time.sleep(10)
    return 'finish'
