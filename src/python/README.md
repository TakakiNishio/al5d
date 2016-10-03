#AL5D moving descriptions

---------------------------------------------------------------

1. Bluetooth connection

```bash
student@vaio:~$ sudo hcitool scan 
[sudo] password for student: 
Scanning ...
	00:06:66:06:9A:F2	FireFly-9AF2
	28:CF:E9:12:21:62	Mac mini di Marzia 
student@vaio:~$ sudo rfcomm bind /dev/rfcomm0 00:06:66:06:9A:F2
student@vaio:~$ ls -l /dev/rfcomm0
crw-rw---- 1 root dialout 216, 0 Sep 26 11:29 /dev/rfcomm0

student@vaio:~$ sudo chmod 777 /dev/rfcomm0
```

---------------------------------------------------------------

2. Python commands

```bash
student@vaio:~$ python
>>> import serial
>>> ssc32 = serial.Serial('/dev/rfcomm0', 115200);
>>> ssc32.write("#0 P1600 T500\r")  
```

ssc32.write("#(motor's port No.) P1(position) T(moving time)\r") 

---------------------------------------------------------------