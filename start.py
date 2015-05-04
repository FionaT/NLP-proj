from multiprocessing import Process
import tornado.ioloop
import tornado.web
import tornado.httpclient
import json
import indexserver, docserver, reviewserver, mainhandler

def loadInvertedIndex():
    temp = json.loads(open("index/invertedindex", "r").read())
    return temp

def loadDocInfo():
    temp = json.loads(open("index/info.json", "r").read())
    return temp

def loadDetail():
    return {"secret" : "not implemented"}

def front():
    application = tornado.web.Application([
        (r"/search", mainhandler.MainHandler),
    ])
    application.listen(15924)
    print 'frontend on 15924'
    tornado.ioloop.IOLoop.instance().start()

def back():
    invertedIndex = loadInvertedIndex()
    application = tornado.web.Application([
        (r"/index", indexserver.Indexer, {'index' : invertedIndex}),
    ])
    application.listen(15925)
    print 'indexer on 15925'

    docInfo = loadDocInfo()
    application = tornado.web.Application([
        (r"/doc", docserver.Docserver, {'index' : docInfo}),
    ])
    application.listen(15926)
    print 'docserver on 15926'

    detail = loadDetail()
    application = tornado.web.Application([
        (r"/detail", reviewserver.Reviewserver, {'index' : detail}),
    ])
    application.listen(15927)
    print 'reviewserver on 15927'
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    print 'all servers on localhost'
    p1 = Process(target = front)
    p1.start()
    p2 = Process(target = back)
    p2.start()