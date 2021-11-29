from MCP3008 import MCP3008
import time

adc = MCP3008()

def readSensor():
     value = adc.read( channel = 0 )
     return value