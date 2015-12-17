#-*- coding:utf-8 -*-
from tornado.httpclient import HTTPClient, AsyncHTTPClient
import tornado.ioloop
from tornado.concurrent import Future
from tornado import gen
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

#同步方法调用
def synchronous_fetch(url, callback):
    http_client = HTTPClient()
    def handle_response(response):
        callback(response)
    http_client.fetch(url, callback=handle_response)

#异步调用, 当完成时 调用回调
def asynchronous_fetch(url, callback):
    http_client = AsyncHTTPClient()
    def handle_response(response):
        callback(response)
    http_client.fetch(url, callback=handle_response)

#把异步结果封装成feture
def asyn_fetch_feture(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    def handler_feture(feture):
        my_future.set_result(feture.result())
        tornado.ioloop.IOLoop.current().add_callback(asyn_fetch_feture_callback, feture.result())
    fetch_future.add_done_callback(handler_feture)
    return my_future

@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response)

def blocking_func(t):
    print('call blocking func')
    time.sleep(t)

@gen.coroutine
def call_blocking():
    yield executor.submit(blocking_func, (4, ))

def synchronous_fetch_callback(result):
    print('synchronous_callback')
    print(result.body)

def asynchronous_fetch_callback(result):
    print('asynchronous_callback')
    print(result.body)

def asyn_fetch_feture_callback(result):
    print('future_callback')
    print(result.headers)

def fetch_coroutine_callback(result):
    print('coroutine callback')
    print(result.body)

if __name__ == '__main__':
    url = 'http://baidu.com'
    synchronous_fetch(url, synchronous_fetch_callback)
    asynchronous_fetch(url, asynchronous_fetch_callback)
    result = asyn_fetch_feture('https://apple.com')
    ioloop = tornado.ioloop.IOLoop.current()
    ioloop.start()

