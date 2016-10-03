import serial
import time

ssc32 = serial.Serial('/dev/rfcomm0', 115200);

ssc32.write("#0 P1500 T500\r")
ssc32.write("#1 P1720 T500\r")
ssc32.write("#2 P660 T500\r")
ssc32.write("#3 P2200 T500\r")
ssc32.write("#4 P1500 T500\r")

time.sleep(5.0)

ssc32.write("#0 P1500 T500\r")
ssc32.write("#1 P1720 T500\r")
ssc32.write("#2 P660 T500\r")
ssc32.write("#3 P100 T500\r")
ssc32.write("#4 P1500 T500\r")

time.sleep(5.0)

ssc32.write("#0 P1500 T500\r")
ssc32.write("#1 P1720 T500\r")
ssc32.write("#2 P660 T500\r")
ssc32.write("#3 P2200 T500\r")
ssc32.write("#4 P1500 T500\r")

ssc32.close()
