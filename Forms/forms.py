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

         # 3. Extract the "message" field from the request data.
        ud = Udacian(parse_qs(data)["name"][0], parse_qs(data)["city"][0], parse_qs(data)["enrollment"][0]
        , parse_qs(data)["nanodegree"][0], parse_qs(data)["status"][0])
        # memory.append(parse_qs(data)["name"][0])
        # memory.append(parse_qs(data)["city"][0])
        # memory.append(parse_qs(data)["enrollment"][0])
        # memory.append(parse_qs(data)["nanodegree"][0])
        # memory.append(parse_qs(data)["status"][0])

        memory.append(ud)

        # response = '''
        # <h1>{0}</h1>
        # <p>{1}</p>
        # <p>{2}</p>
        # <p>{3}</p>
        # <p>{4}</p>
        # '''.format(u)
        response = memory[0]

        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        self.wfile.write(response.encode())

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        self.wfile.write(form.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
