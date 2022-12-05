import time
from typing import List

import serial
from struct import *

MASTER_PACKET_FORMAT = "=BBHHHBH"
PACKET_SIZE = calcsize(MASTER_PACKET_FORMAT)
MAX_ROBOTS = 6

with serial.Serial('/dev/pts/0', 38400, timeout=1) as ser:
    com_robots: List[bytes] = [b''] * MAX_ROBOTS

    state: int = 0
    temp: bytes = b''
    pos: int = 0

    while True:
        c: bytes = ser.read()

        # reset byte string since we append and not override like the cpp
        if pos == 0:
            temp = b''

        if state == 0:
            if c == b'\xaa':
                state += 1

        elif state == 1:
            if c == b'\x55':
                state += 1
            else:
                state = 0

        elif pos < PACKET_SIZE:
            temp += c
            pos += 1

        else:
            if c == b'\xff':
                rid, actions, x_speed, y_speed, t_speed, kickPower, order_id = unpack(MASTER_PACKET_FORMAT,
                                                                                      temp[:PACKET_SIZE])
                print(f"""
##############################################"
{temp}

robot_id: {rid},
actions: {actions},

x_speed: {x_speed},
y_speed: {y_speed},
t_speed: {t_speed},

kickPower: {kickPower},
order_id: {order_id}
##############################


                """)

            state = 0
            pos = 0
            print(temp)
