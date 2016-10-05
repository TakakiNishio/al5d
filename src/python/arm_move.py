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

    theta0 = float(deg[0]*(m.pi/180))
    theta1 = float(deg[1]*(m.pi/180))
    theta2 = float(deg[2]*(m.pi/180))
    theta3 = float(deg[3]*(m.pi/180))
    theta_sum01 = theta0 + theta1
    theta_sum = theta0 + theta1 + theta2 + theta3
    #---------------------------------------------
    a1 = l1 * np.cos(theta0)
    b1 = a1 + l2 * np.cos(theta_sum01)
    c1 = b1 + l3 * np.cos(theta_sum)
    #---------------------------------------------
    a2 = l1 * np.sin(theta0)
    b2 = a1 + l2 * np.sin(theta_sum01)
    c2 = b1 + l3 * np.sin(theta_sum)

    A = [[0 for i in range(3)] for j in range(3)]
    A[0][0] = np.cos(theta_sum)
    A[0][1] = -np.sin(theta_sum)
    A[0][2] = c1
    A[1][0] = np.sin(theta_sum)
    A[1][1] = np.cos(theta_sum)
    A[1][2] = c2
    A[2][0] = 0
    A[2][1] = 0
    A[2][2] = 1
    #print A

    S = [[0 for i in range(3)] for j in range(3)]
    S[0][0] = (c1+x0)*np.cos(theta0)
    S[0][1] = (c1+x0)*np.sin(theta0)
    S[0][2] = c2 + z0
    S[1][0] = (b1+x0)*np.cos(theta0)
    S[1][1] = (b1+x0)*np.cos(theta0)
    S[1][2] = b2 + z0
    S[2][0] = (a1+x0)*np.cos(theta0)
    S[2][1] = (a1+x0)*np.cos(theta0)
    S[2][2] = a2 + z0
    #print S

    error_flag = 0

    for i in range(0,3):
        if S[i][2] < 20:
            if i == 1:
                print "!!Position Error: The elbow position is out from the workspace."
                error_flag = 1
            elif i == 2:
                print "!!Position Error: The wrist position is out from the workspace."
                error_flag = 1
            elif i == 3:
                print "!!Position Error: The gripper position is out from the workspace."
                error_flag = 1

        if S[i][1] < 0 and -100 < S[i][0] < 100 and S[i][2] < 120:
            if i == 1:
                print "!!Position Error: The elbow position is out from the workspace. Avoid a collision with electrical parts!"
                error_flag = 1
            elif i == 2:
                print "!!Position Error: The wrist position is out from the workspace. Avoid a collision with electrical parts!"
                error_flag = 1
            elif i == 3:
                print "!!Position Error: The gripper position is out from the workspace. Avoid a collision with electrical parts!"
                error_flag = 1

    if grip <= 0.05 or grip >= 30:
        print "!!Gripper Erorr: Non-permitted gripper position"
        error_flag = 1

    return error_flag


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

    print "connected. press 0 + Enter to move the arm: "
    init_bottun = raw_input('>>>  ')

    if init_bottun == '0':

        initialize = init_arm(ssc32)
        theta = []
        print "imput each joint angle in deg."
        print "theta_base:"
        theta.append(float(raw_input('>>>  ')))
        print "theta_shoulder:"
        theta.append(float(raw_input('>>>  ')))
        print "theta_elbow:"
        theta.append(float(raw_input('>>>  ')))
        print "theta_wrist:"
        theta.append(float(raw_input('>>>  ')))
        print "imput gripper dist(0.05 < dist < 30)."
        pos_g = float(raw_input('>>>  '))

        position = deg2pos(theta, pos_g)

        print "input angle[deg]: " + str(theta)
        print "psition: " + str(position)

        error = position_checker(theta, pos_g)

        if error == 1:
            print "operation stopped."
        elif error == 0:
            print "robot will move."
            time.sleep(2.0)
            s = serial_send(position,2000)

            #print s

    else:
        print "operation canceled."

    ssc32.close()
