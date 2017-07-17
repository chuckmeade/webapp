#!/usr/bin/python

from SocketServer import BaseRequestHandler

class Base(object): 
    def __init__(self):
        print "Initialize Base"
        self.handle()

class Stream(Base):
    def __init__(self):
        self.wfile = "Stream.wfile"
        super(Stream, self).__init__()

class Secure(Base):
    def __init__(self):
        self.wfile = "Secure.wfile"
        super(Secure, self).__init__()

class BaseHTTP(Stream):
    def __init__(self):
        self.wfile = "BaseHTTP.wfile"
        super(BaseHTTP, self).__init__()
    def handle(self):
        print "BaseHTTP.handle()"
        self.handle_one_request()
    def handle_one_request(self):
        print "handle_one_request is reading from " + self.wfile
        method = getattr(self, "do_STUFF")
        print method()

    def send_headers(self, key, value):
        print "%s %s" % (key, value)

class SecureHTTP(BaseHTTP, Secure):
    def __init__(self):
        super(SecureHTTP, self).__init__()
    def do_STUFF(self):
        self.send_headers("Content-Length", "128")
        print self.wfile
        return "do_STUFF returned"

print(SecureHTTP.__mro__)
req = SecureHTTP()

