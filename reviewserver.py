import tornado.ioloop
import tornado.web
import json
import naiveKeywords

class Reviewserver(tornado.web.RequestHandler):
    docs = {}
    def initialize(self, index):
        self.docs = index

    def get(self):
        bid = self.get_argument('id', None)
        text = "merchant not found!"
        if bid in self.docs:
        	text = self.docs[bid]
        features = self.extractFeatures(text)
        # write back response
        self.write(json.dumps(features))

    def extractFeatures(self, text):
        return naiveKeywords.extractFeatures(text)