import serial
import time
import numpy as np
import math as m


def init_arm(board):

    board.write("#0 P1500 T2000\r")
    board.write("#1 P1720 T2000\r")
    board.write("#2 P660 T2000\r")
    board.write("#3 P2200 T2000\r")
    board.write("#4 P1500 T2000\r")

    ok = 1

    return ok


def position_checker(deg,grip):

    #link length
    l1 = 120
    l2 = 128
    l3 = 75

    #base position
    z0 =67
    x0 = 15

    theta1 = float(deg[0]*(m.pi/180))

    return theta1


def deg2pos(deg,grip):

    #-------------------
    base_0 = 2420
    base_90 = 1500
    base_180 = 580
    #-------------------
    shoulder_0 = 620
    shoulder_90 = 1390
    shoulder_180 = 2160
    #-------------------
    elbow_0 = 615
    elbow_90 = 1500
    elbow_180 = 2385
    #-------------------
    wrist_0 = 2450
    wrist_90 = 1550
    wrist_180 = 650
    #-------------------

    pos = []

    pos.append(int((float((base_90-base_0))/90*deg[0] + base_0)))
    pos.append(int((float((shoulder_90-shoulder_0))/90*deg[1] + shoulder_0)))
    pos.append(int((float((elbow_90-elbow_0))/90*(deg[2]+90) + elbow_0)))
    pos.append(int((float((wrist_90-wrist_0))/90*(deg[3]+90) + wrist_0)))
    pos.append(int(float(-40*grip)+2250))
    return pos


def serial_send(pos,tct):

    s = []

    s.append('#0 P' + str(pos[0]) + ' T' + str(tct) + '\r')
    s.append('#1 P' + str(pos[1]) + ' T' + str(tct) + '\r')
    s.append('#2 P' + str(pos[2]) + ' T' + str(tct) + '\r')
    s.append('#3 P' + str(pos[3]) + ' T' + str(tct) + '\r')
    s.append('#4 P' + str(pos[4]) + ' T' + str(tct) + '\r')

    ssc32.write(s[0])
    ssc32.write(s[1])
    ssc32.write(s[2])
    ssc32.write(s[3])
    ssc32.write(s[4])
    ssc32.close()

    return s



if __name__ == '__main__':

    ssc32 = serial.Serial('/dev/rfcomm0', 115200);
    time.sleep(3.0)

    initialize = init_arm(ssc32)

    theta = []

    print"imput each joint angle in deg."
    print "theta_base:"
    theta.append(float(raw_input('>>>  ')))
    print "theta_shoulder:"
    theta.append(float(raw_input('>>>  ')))
    print "theta_elbow:"
    theta.append(float(raw_input('>>>  ')))
    print "theta_wrist:"
    theta.append(float(raw_input('>>>  ')))
    print"imput gripper dist(0.05-30)."
    pos_g = float(raw_input('>>>  '))

    n = position_checker(theta, pos_g)
    print n

    position = deg2pos(theta, pos_g)

    print "input angle[deg]: " + str(theta)
    print "psition: " + str(position)

    s = serial_send(position,2000)

    #print s

    ssc32.close()
