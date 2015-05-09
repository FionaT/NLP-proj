import tornado.ioloop
import tornado.web
import sys
import tornado.httpclient
import urllib
import json
from tornado import gen

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')

    @gen.coroutine
    def get(self):
        query = self.get_argument('query', None)
        query = query.lower()
        # get postingslist from indexer
        httpClient = tornado.httpclient.AsyncHTTPClient()
        url = "http://localhost:15925/index?query=%s" % query
        response = yield httpClient.fetch(url)
        dic = json.loads(response.body)
        # get merchant info
        futures = []
        for each in dic:
            url = "http://localhost:15926/doc?id=%s" % each
            futures.append(httpClient.fetch(url))
        responses = yield futures
        responses = [response.body for response in responses]
        # write response to user
        self.write(json.dumps({"list" : responses}))
        self.finish()