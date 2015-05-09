import tornado.ioloop
import tornado.web
import json
import editdistance

class Indexer(tornado.web.RequestHandler):
    merchants = {}
    def initialize(self, index):
        self.merchants = index

    def get(self):
        query = self.get_argument('query', None).encode('utf-8').lower()
        result = []
        exact_match = ""
        if (query + "__") in self.merchants:
            bid = self.merchants[query + "__"]
            exact_match = bid
        else:
            single = query.split()
            li = {}
            for each in single:
                if each in self.merchants:
                    res = self.merchants[each]
                    for (bid, time) in res:
                        if bid not in li:
                            li[bid] = time
                        else:
                            li[bid] += time
            result = li.items()
            result.sort(key=lambda x : x[1])
            result.reverse()
            result = [a for (a, b) in result]
        if len(result) >= 10:
            result = result[0:10]
        if exact_match:
            result.insert(0, exact_match)
        # write back response
        self.write(json.dumps(result))


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/index", Indexer),
    ])
    application.listen(15924)
    print 'indexer on %s' % 15924
    tornado.ioloop.IOLoop.instance().start()