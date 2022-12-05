import time
from typing import List

import serial
from struct import *

BYTE_ORDER = "little"
MASTER_PACKET_FORMAT = ">cchhhch"
PACKET_SIZE = calcsize(MASTER_PACKET_FORMAT)
MAX_ROBOTS = 6

byte_to_int = lambda x: int.from_bytes(x, BYTE_ORDER)

with serial.Serial('/dev/pts/0', 38400, timeout=1) as ser:
    # print(ser.read(100))
    # exit()

    com_usb_nb_robots: int = None
    # com_should_transmit = [None] * MAX_ROBOTS
    com_robots: List[bytes] = [b''] * MAX_ROBOTS
    # com_has_status = [None] * MAX_ROBOTS
    # com_usb_reception = -1

    state: int = 0
    temp: bytes = b''
    pos: int = 0

    while True:
        c: bytes = ser.read()
        print(c)

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

        elif state == 2:
            com_usb_nb_robots = byte_to_int(c)
            pos = 0
            if com_usb_nb_robots <= MAX_ROBOTS:
                state += 1
            else:
                state = 0

        elif pos < com_usb_nb_robots * (1 + PACKET_SIZE):
            temp += c
            # temp[pos] = c
            pos += 1
            # print(f"{pos} < {com_usb_nb_robots * (1+PACKET_SIZE)}")
            # print(temp)

        else:
            if c == b'\xff':
                # print("END")
                for k in range(com_usb_nb_robots):
                    robot_id = temp[k * (PACKET_SIZE + 1)]
                    print(robot_id)
                    if robot_id < MAX_ROBOTS:
                        rid, actions, x_speed, y_speed, t_speed, kickPower, order_id = unpack(MASTER_PACKET_FORMAT,
                                                                                              temp[k * (
                                                                                                          1 + PACKET_SIZE) + 1: k * (
                                                                                                          1 + PACKET_SIZE) + 1 + PACKET_SIZE])
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

            # for n in range(PACKET_SIZE):
            #     com_robots[robot_id][n] = temp[k * (1 + PACKET_SIZE) + 1 + n]
            #
            # com_should_transmit[robot_id] = True

            # com_poll()
            # for k in range(MAX_ROBOTS):
            #     com_has_status[k] = False
            # com_master_pos = -1
            # com_usb_reception = time.time()
            state = 0
            print(f"Nb robots: {com_usb_nb_robots}, c={c}")
            print(temp)
