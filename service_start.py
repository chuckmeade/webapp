#!/usr/bin/python

from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer
from pyserver import LieutenantRequestHandler, CommanderRequestHandler
import threading
import time

'''
Startup script for the Lieutenant/Commander servers.
'''

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread"""
    pass

def SpinupServer(ip, port, handler):
    # Create the server object
    server = ThreadedHTTPServer((ip, port), handler)

    # Create a separate server thread for the handler to begin to run within.
    server_thread = threading.Thread(target=server.serve_forever)

    # Set the thread to be a daemon
    server_thread.setDaemon(True)

    # Start the thread
    server_thread.start()

    print "Server thread started on %s:%d" % (ip, port)
    print handler
    print "\n"


def main():
    # Setup the IP/port listeners
    LT_IP, LT_PORT = "127.0.0.1", 5000
    COM_IP, COM_PORT = "127.0.0.1", 5001

    # Initialize the server daemons to listen on their respective ports.
    SpinupServer(LT_IP, LT_PORT, LieutenantRequestHandler)
    SpinupServer(COM_IP, COM_PORT, CommanderRequestHandler)

    while(1):
        time.sleep(1)

if __name__ == "__main__":
    main()
