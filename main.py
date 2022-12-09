import time
from typing import List

import serial
from struct import *
from robot import Robot
from link_one_robot import *


MASTER_PACKET_FORMAT = "=BBhhhBh"
PACKET_SIZE = calcsize(MASTER_PACKET_FORMAT)

# default is 6
MAX_ROBOTS = input("MAX_ROBOTS (defaults to 6): \n")
if MAX_ROBOTS == "":
    MAX_ROBOTS = 6
else:
    MAX_ROBOTS = int(MAX_ROBOTS)

last_kick = { _id: time.time() for _id in range(MAX_ROBOTS) }

rsk_comm_ports = get_rsk_comm_ports()
robots_connections = setup_robot_connections(rsk_comm_ports)
# user_turns_robot(robots_connections)

with serial.Serial('/dev/pts/6', 38400, timeout=1) as ser:
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
#                 print(f"""
# ##############################################"
# {temp}

# robot_id: {rid},
# actions: {actions},

# x_speed: {x_speed},
# y_speed: {y_speed},
# t_speed: {t_speed},

# kickPower: {kickPower},
# order_id: {order_id}
# ##############################


#                 """)

            rid = str(rid)
            if rid in robots_connections:
                robots_connections[rid].control(x_speed/1000.0, y_speed/1000.0, t_speed/1000.0)
                if actions & (1 << 1) != 0 and last_kick + 1 < time.time():
                    print("KICKING GGGGGG")
                    robots_connections[rid].kick(power=1)
                    last_kick[rid] = time.time()

            state = 0
            pos = 0
