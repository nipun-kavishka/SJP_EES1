from MCP3008 import MCP3008
import time

adc = MCP3008()

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;

while True:
    value = adc.read( channel = 0 ) # You can of course adapt the channel to be read out
    #print("Applied voltage: %.2f" % (value / 1023.0 * 3.3) )
    print(str(value) + "\t")
    print(map(value,0,950,0,90))
    time.sleep(0.5)
    
