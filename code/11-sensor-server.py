import glob
import time
import BaseHTTPServer
import RPi.GPIO as GPIO

LDR_PIN = 23

GPIO.setmode(GPIO.BCM)

base_dir = '/sys/bus/w1/devices/'
device_prefix = '28-*'
device_folder = glob.glob(base_dir + device_prefix)[0]
device_file = device_folder + '/w1_slave'

def read_temp():
  with open(device_file, 'r') as f:
    lines = f.readlines()
  if lines[0].strip().endswith('YES'):
    i = lines[1].rfind('=')
    if i != -1:
      temp = lines[1][i+1:]
      return float(temp) / 1000.0
  else:
    return read_temp()

def ldr_value():
  value = 0
  GPIO.setup(LDR_PIN, GPIO.OUT)
  GPIO.setup(LDR_PIN, GPIO.LOW)
  time.sleep(0.1)
  start = time.time()
  GPIO.setup(LDR_PIN, GPIO.IN)
  while (GPIO.input(LDR_PIN) == GPIO.LOW):
    value += 1
  finish = time.time()
  duration = 1000 * (finish - start)
  return duration

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
    s.wfile.write("<p>Current light: %s.</p>" % ldr_value())
    s.wfile.write("<p>Current temperature: %s.</p>" % read_temp())
    s.wfile.write('<p><a href="/">Refresh</a></p>')
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

GPIO.cleanup()

