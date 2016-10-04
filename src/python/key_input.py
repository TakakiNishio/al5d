import serial
import time

ssc32 = serial.Serial('/dev/rfcomm0', 115200);

#print ssc32

time.sleep(2.0)

ssc32.write("#0 P1500 T800\r")
ssc32.write("#1 P1720 T800\r")
ssc32.write("#2 P660 T800\r")
ssc32.write("#3 P2200 T800\r")
ssc32.write("#4 P1500 T800\r")

print"imput each servo angles"
print "t0 (t0(0) = 1500):"
t0 = raw_input('>>>  ')
print "t1 (t1(0) = 1720):"
t1 = raw_input('>>>  ')
print "t2 (t2(0) = 660):"
t2 = raw_input('>>>  ')
print "t3 (t3(0) = 2200):"
t3 = raw_input('>>>  ')
print "t4 (t4(0) = 1500):"
t4 = raw_input('>>>  ')
print "speed (s(0) = 800):"
#s = 500
s = raw_input('>>>  ')

#t0 = '#0 P' + t0 + ' T' + str(s) + '\r'
t0 = '#0 P' + t0 + ' T' + s + '\r'
t1 = '#1 P' + t1 + ' T' + s + '\r'
t2 = '#2 P' + t2 + ' T' + s + '\r'
t3 = '#3 P' + t3 + ' T' + s + '\r'
t4 = '#4 P' + t4 + ' T' + s + '\r'

ssc32.write(t0)
ssc32.write(t1)
ssc32.write(t2)
ssc32.write(t3)
ssc32.write(t4)

ssc32.close()
