import serial
import time

ssc32 = serial.Serial('/dev/rfcomm0', 115200);

interval = 2.0

#motion0
ssc32.write("#0 P1505 T700\r")
ssc32.write("#1 P1720 T700\r")
ssc32.write("#2 P663 T700\r")
ssc32.write("#3 P2292 T700\r")
ssc32.write("#4 P1500 T700\r")

time.sleep(interval)

#motion1
ssc32.write("#0 P1505 T700\r")
ssc32.write("#1 P1720 T700\r")
ssc32.write("#2 P663 T700\r")
ssc32.write("#3 P2292 T700\r")
ssc32.write("#4 P920 T700\r")

time.sleep(interval)

#motion2
ssc32.write("#0 P1505 T700\r")
ssc32.write("#1 P1360 T700\r")
ssc32.write("#2 P500 T700\r")
ssc32.write("#3 P2152 T700\r")
ssc32.write("#4 P920 T700\r")

time.sleep(interval)

#motion3
ssc32.write("#0 P1505 T700\r")
ssc32.write("#1 P1260 T700\r")
ssc32.write("#2 P550 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P920 T700\r")

time.sleep(interval)

#motion4
ssc32.write("#0 P1505 T700\r")
ssc32.write("#1 P1260 T700\r")
ssc32.write("#2 P550 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P1900 T700\r")

time.sleep(interval)

#motion5
ssc32.write("#0 P1505 T700\r")
ssc32.write("#1 P1410 T700\r")
ssc32.write("#2 P875 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P1900 T700\r")

time.sleep(interval)

#motion6
ssc32.write("#0 P2180 T700\r")
ssc32.write("#1 P1410 T700\r")
ssc32.write("#2 P875 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P1900 T700\r")

time.sleep(interval)

#motion7
ssc32.write("#0 P2180 T700\r")
ssc32.write("#1 P1375 T700\r")
ssc32.write("#2 P620 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P1900 T700\r")

time.sleep(interval)

#motion8
ssc32.write("#0 P2180 T700\r")
ssc32.write("#1 P1180 T700\r")
ssc32.write("#2 P690 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P1900 T700\r")

time.sleep(interval)

#motion9
ssc32.write("#0 P2180 T700\r")
ssc32.write("#1 P1180 T700\r")
ssc32.write("#2 P690 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P1230 T700\r")

time.sleep(interval)

#motion10
ssc32.write("#0 P2180 T700\r")
ssc32.write("#1 P1375 T700\r")
ssc32.write("#2 P620 T700\r")
ssc32.write("#3 P2282 T700\r")
ssc32.write("#4 P1230 T700\r")

time.sleep(interval)

#motion11
ssc32.write("#0 P1505 T1000\r")
ssc32.write("#1 P1260 T1000\r")
ssc32.write("#2 P620 T1000\r")
ssc32.write("#3 P2282 T1000\r")
ssc32.write("#4 P1300 T1000\r")

time.sleep(interval)

#motion12
ssc32.write("#0 P1505 T800\r")
ssc32.write("#1 P1720 T800\r")
ssc32.write("#2 P663 T800\r")
ssc32.write("#3 P2292 T800\r")
ssc32.write("#4 P1500 T800\r")

ssc32.close()
