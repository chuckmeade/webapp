'''
This is the Lieutenant Server daemon that takes care of menial tasks that the
Commander Server can't be bothered to do.
'''

from BaseHTTPServer import BaseHTTPRequestHandler

HTML_GET_RESPONSE = """ 
<html>
    <body>
        <h1> The Commander is responding to your GET request </h1>
    </body>
</html>
"""

HTML_POST_RESPONSE = """
<html>
    <body>
        <h1> The Commander is responding to your POST request </h1>
    </body>
</html>
"""

class CommanderRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Setup the basics of the response
        self.send_response(200)
        self.end_headers()

        # Write the actual HTML response for the GET request
        self.wfile.write(HTML_GET_RESPONSE)
        self.wfile.write('\n')

        return

    def do_POST(self):
        # Setup the basics of the response
        self.send_response(200)
        self.end_headers()

        # Write the actual HTML response for the GET request
        self.wfile.write(HTML_POST_RESPONSE)
        self.wfile.write('\n')
 
        return
