import glob

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

try:
  while True:
    print(read_temp())
except KeyboardInterrupt:
  pass

