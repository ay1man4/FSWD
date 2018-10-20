#
# Udacian activity to practice get and post http
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from udacian import Udacian

memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()

         # 3. Extract all parameters to dictionay d from the request data.
        d = parse_qs(data)
        ud = Udacian(d['name'][0], d['city'][0], d['enrollment'][0], d['nanodegree'][0], d['status'][0])
        
        # Add new udacian to memory
        memory.append(ud)

        # redirect user to home page
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()
        
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Join all udacians stored in memory to single string (one udacian per line)
        s = "\n".join(str(u) for u in memory)

        # replace {} in form with udacians string
        form_with_history = form.format(s)
        
        # Now, write the response body.
        self.wfile.write(form_with_history.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
