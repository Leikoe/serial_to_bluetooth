from typing import List

import serial
from robot import Robot
from link_one_robot import *
from proto import protocol_robot_catie_2022_pb2

# default is 6
MAX_ROBOTS = input("MAX_ROBOTS (defaults to 6): \n")
if MAX_ROBOTS == "":
    MAX_ROBOTS = 6
else:
    MAX_ROBOTS = int(MAX_ROBOTS)

last_kick = { _id: time.time() for _id in range(MAX_ROBOTS) }

rsk_comm_ports = get_rsk_comm_ports()
robots_connections = setup_robot_connections(rsk_comm_ports)
#user_turns_robot(robots_connections)

with serial.Serial('/dev/pts/4', 115200, timeout=1) as ser:
    buffer = b''
    p = protocol_robot_catie_2022_pb2.IAToMainBoard()

    while True:
        c: bytes = ser.read()
        buffer += c

        
        try:
            p.ParseFromString(buffer)

            if p.HasField("robot_id") and p.HasField("normal_speed") and p.HasField("tangential_speed") and p.HasField("angular_speed"):
                print(p)
                print(p.robot_id)
                if p.robot_id in robots_connections:
                    print(f"sent control({p.normal_speed}, {p.tangential_speed}, {p.angular_speed})")
                    robots_connections[p.robot_id].control(p.normal_speed, p.tangential_speed, p.angular_speed)
                    # if actions & (1 << 1) != 0 and last_kick[rid] + 1 < time.time():
                    #     robots_connections[rid].kick(power=1)
                    #     last_kick[rid] = time.time()

                # print(p)

                # reset buffer
                buffer = b''
                p.Clear()
            else:
                print(buffer)
        except:
            pass

