#!/usr/bin/python3

'''
Depends
pymodbus
numpy

Version control
Beta    01-13-2020 bsw      Initial functions, read the micromotion
1.0     02-13-2020          removed this part, it wasn't mine. 
1.0.1   02-13-2020 bsw      Some cleanup and readability, moved file write into block with the actual data, added strict=False to modbus object
1.0.2   03-25-2020 bsw		Little cleanup, looks like a release candidate.
1.0.2   03-26-2020 bsw      Engineering manager was *not* happy: "Can't you write that in LabView?"

# Archive project

'''
 
# setup
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.compat import iteritems
from time import strftime


# Do we need
global volume_flow
volume_flow=0

# removed the plotter, I didn't write that. 

# Set up the modbus client and call an object
# Ucomment this line for Superior Linux Environments
# client = ModbusClient(method='rtu', port='/dev/ttyUSB0', stopbits=1, parity='O', baudrate=1200, bytesize=8, timeout=5, unit=1)
# Uncomment this line for shitty Windows losers, be sure to check your COM port lol
client = ModbusClient(method='rtu', port='COM6', stopbits=1, parity='O', baudrate=1200, bytesize=8, timeout=5, unit=1, strict=False)
client.connect()

# Open the files for writing
filetime=strftime("%m%d%y_%H%M%S")
# This is for Linux
# filename="/home/pi/script/micromotion_" + filetime
# This is for Window$
filename="C:\micromotion\micromotion_" + filetime
f=open(filename, "w")

# This sets the byte order to 4-3-2-1 - uncomment and set to client.write_register(520,1) for 3-41-2, as shipped from the factory
'''
client.write_register(520,0)
result=client.read_holding_registers(520,1,unit=1)
print (result.registers)
'''

# average a list
def Average(list):
    return sum(list)/len(list)

# Main function to read registers and format/show the data
def readitall (i, ys):

# Read the registers from the Micro Motion
 result=client.read_holding_registers(250,2,unit=1)
 decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
 temp = decoder.decode_32bit_float()
 result=client.read_holding_registers(246,2,unit=1)
 decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
 mass = decoder.decode_32bit_float()
 result=client.read_holding_registers(248,2,unit=1)
 decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
 dens = decoder.decode_32bit_float()
 result=client.read_holding_registers(252,2,unit=1)
 decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
 volf = decoder.decode_32bit_float()

# Clean the numbers up for the data file
 temperature_c=(int(temp*10000)/10000)
 density=(int(dens*10000)/10000)
 mass_flow=(int(mass*10000)/10000)
 volume_flow=(int(volf*10000)/10000)

# Write the data to a file
 f.write(strftime("%m/%d/%y %H:%M:%S") + "\t" + str(temperature_c) + "\t" + str(density) + "\t" + str(mass_flow) + "\t" + str(volume_flow) + "\r\n")

# Clean the numbers up to show the user
 temperature_format=str('{:10.4f}'.format(temp))
 density_format=str('{:10.4f}'.format(dens))
 mass_flow_format=str('{:10.4}'.format(mass))
 volume_flow_format=str('{:10.4}'.format(volf))
  
# Pop the numbers on the stack, and display them
 stack.append(volume_flow)
 if len(stack) >= tavg:
     avgflow = Average(stack)
     stack.pop(0)
     average_flow_format=str('{:10.4f}'.format(avgflow))
     print (strftime("%m/%d/%y %H:%M:%S") + "\t" + temperature_format + "\t" + density_format + "\t" + mass_flow_format + "\t" + volume_flow_format + "\t" + average_flow_format)
 else:
     print (strftime("%m/%d/%y %H:%M:%S") + "\t" + temperature_format + "\t" + density_format + "\t" + mass_flow_format + "\t" + volume_flow_format)
 
# Removed this, I didn't write it.

# bye
client.close()
f.close()
exit()
