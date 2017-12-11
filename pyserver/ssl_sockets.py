#!/usr/bin/python

'''
Run a test server that opens up a socket wrapped in SSL on a non-standard port.
'''

import socket
import ssl

def main():
    suites = 'ECDHE-RSA-AES128-GCM-SHA256'
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_s.bind(('127.0.0.1', 7000));
    server_s.listen(10)

    while True:
        print "Awaiting connections..."

        (s, addr) = server_s.accept()

        print "Accepted connection: %s : %s\n" % (s, addr)

        ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ctx.set_ciphers(suites)

        ctx.load_cert_chain(certfile='/home/zmazar/public/16c/ssl/server.crt', \
                            keyfile='/home/zmazar/public/16c/ssl/server.key')
        ctx.load_dh_params('/home/zmazar/public/16c/ssl/dhparams.pem')

        try:
            tls_s = ctx.wrap_socket(s, server_side=True)

            print str(tls_s)

            tls_s.close()
        except ssl.SSLError as e:
            print e

if __name__ == '__main__':
    main()
