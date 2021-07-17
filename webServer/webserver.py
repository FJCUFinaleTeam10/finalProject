# ------------------------------------------------------------------------------------------------
# so let's write a custom temporary-HTML renderer
# pretty much copy-paste of this answer: https://stackoverflow.com/a/38945907/3494126
import subprocess
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 7000
HOST = '127.0.0.1'
SERVER_ADDRESS = '{host}:{port}'.format(host=HOST, port=PORT)
FULL_SERVER_ADDRESS = 'http://' + SERVER_ADDRESS


def TemproraryHttpServer(page_content_type, raw_data):
    """
    A simpe, temprorary http web server on the pure Python 3.
    It has features for processing pages with a XML or HTML content.
    """

    class HTTPServerRequestHandler(BaseHTTPRequestHandler):
        """
        An handler of request for the server, hosting XML-pages.
        """

        def do_GET(self):
            """Handle GET requests"""
            # response from page
            self.send_response(200)
            # set up headers for pages
            content_type = 'text/{0}'.format(page_content_type)
            self.send_header('Content-type', content_type)
            self.end_headers()
            # writing data on a page
            self.wfile.write(bytes(raw_data, encoding='utf'))
            return

    if page_content_type not in ['html', 'xml']:
        raise ValueError('This server can serve only HTML or XML pages.')
    page_content_type = page_content_type
    # kill a process, hosted on a localhost:PORT
    subprocess.call(['fuser', '-k', '{0}/tcp'.format(PORT)])
    # Started creating a temprorary http server.
    httpd = HTTPServer((HOST, PORT), HTTPServerRequestHandler)
    # run a temprorary http server
    httpd.serve_forever()


def run_html_server(html_data=None):
    if html_data is None:
        html_data = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        </body>
        </html>
        """
    # open in a browser URL and see a result
    webbrowser.open(FULL_SERVER_ADDRESS)
    # run server
    TemproraryHttpServer('html', html_data)
