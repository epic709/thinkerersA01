import BaseHTTPServer

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_HEAD(s):
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
  def do_GET(s):
    s.do_HEAD()
    s.wfile.write("<html>")
    s.wfile.write("<head><title>Pi Server</title></head>")
    s.wfile.write("<body>")
    s.wfile.write("<p>Welcome!</p>")
    s.wfile.write("<p>You accessed: %s</p>" % s.path)
    s.wfile.write("<p><img src="~/images/Raspi_Colour_R.png">Test image</img></p>")
    s.wfile.write("</body>")
    s.wfile.write("</html>")

httpd = BaseHTTPServer.HTTPServer(('', 80), MyHandler)
print "Server started"
try:
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()
print "Server stopped"

