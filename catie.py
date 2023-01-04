from typing import List

import serial
from robot import Robot
from link_one_robot import *
from proto import protocol_robot_catie_2022_pb2

IAToMainBoard_size = 34

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

with serial.Serial('/dev/ttys004', 115200, timeout=1) as ser:
    read_buffer = b'' * IAToMainBoard_size
    p = protocol_robot_catie_2022_pb2.IAToMainBoard()
    start_of_frame = False
    length = 0
    c: bytes

    while True:
        # print(read_buffer)
        if not start_of_frame:
            c = ser.read()
            if 0 < int.from_bytes(c, "little") <= IAToMainBoard_size: # Get packet length
                start_of_frame = True
                length = int.from_bytes(c, "little")
                read_buffer = b'' * IAToMainBoard_size
                print(f"Receiving : {length}")
            elif c == 0:# When length is 0 it is the default protobuf packet
                start_of_frame = False
                length = 0
                read_buffer = b'' * IAToMainBoard_size
                # radio_packet[0] = 0
                # TODO: SEND PACKET
        else:
            read_buffer += ser.read(1)
            if len(read_buffer) == length:
                start_of_frame = False

                # event_queue.call(printf, "Parsing !\n");

                # Try to decode protobuf response
                ai_message = protocol_robot_catie_2022_pb2.IAToMainBoard()

                try:
                    print(read_buffer)
                    # Now we are ready to decode the message.
                    status = ai_message.ParseFromString(read_buffer)

                    if ai_message.robot_id in robots_connections:
                        print(f"sent control({ai_message.normal_speed}, {ai_message.tangential_speed}, {ai_message.angular_speed})")
                        robots_connections[p.robot_id].control(ai_message.normal_speed, ai_message.tangential_speed, ai_message.angular_speed)
                        # if actions & (1 << 1) != 0 and last_kick[rid] + 1 < time.time():
                        #     robots_connections[rid].kick(power=1)
                        #     last_kick[rid] = time.time()

                except Exception as e:
                    print(e)

                read_buffer = b'' * IAToMainBoard_size
