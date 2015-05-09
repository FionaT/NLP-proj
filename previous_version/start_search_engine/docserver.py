import tornado.ioloop
import tornado.web
import json

class Docserver(tornado.web.RequestHandler):
    docs = {}
    def initialize(self, index):
        self.docs = index

    def get(self):
        bid = self.get_argument('id', None)
        if bid in self.docs:
        	infos = self.docs[bid]
        	infos['business_id'] = bid
        # write back response
        self.write(json.dumps(infos))