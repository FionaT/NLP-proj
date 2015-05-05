import tornado.ioloop
import tornado.web
import json
import NaiveKeywords

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
        res = self.wrapResponse(features)
        self.write(res)

    def extractFeatures(self, text):
        return NaiveKeywords.extractFeatures(text)

    def wrapResponse(self, features):
        res = "<head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'><meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'><title>Detail Page</title>"
        res += '<style>.login-input {display: block;cursor: pointer;float: left;height: 37px;margin-bottom: 20px;padding: 0 9px;color: white;text-align: left; font-size: 12px;text-shadow: 0 1px black;background: #2b3e5d;border: 1px solid #15243b;border-top-color: #0d1827;border-radius: 4px;background-image: -webkit-linear-gradient(top, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.2) 20%, rgba(0, 0, 0, 0));background-image: -moz-linear-gradient(top, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.2) 20%, rgba(0, 0, 0, 0));background-image: -o-linear-gradient(top, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.2) 20%, rgba(0, 0, 0, 0));background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.2) 20%, rgba(0, 0, 0, 0));-webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.3), 0 1px rgba(255, 255, 255, 0.2);box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.3), 0 1px rgba(255, 255, 255, 0.2);} .login-input:left {float: left;} .login-input:right {float: right;}</style>'
        res += '</head><body><div style="width:15%">'
        for each in features:
            (a, b) = each
            pos = str(b[0])
            neg = str(b[1])
            res += '<p><input type="text" class="login-input" style="width:100%; float:left" value="' + a + "   +" + pos + ",-" + neg + '"></p>'
        return res + '</div></body>'