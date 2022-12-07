import subprocess
import time

from robot import Robot

"""
Returns all communications ports starting with 'rfcomm'
By default in the script mount.sh, all robots are mounted on the port rfcommX,
where X is an arbitrary number
"""


def get_rsk_comm_ports() -> list[str]:
    out = subprocess.run(['ls', '/dev/'], stdout=subprocess.PIPE)
    ls_output = out.stdout.decode('utf-8')
    ls_output = ls_output.split('\n')
    rsk_comm_ports = list(filter(lambda n: 'rfcomm' in n, ls_output))
    return rsk_comm_ports


"""
Given a list of communications ports, initialize the software
connection on each port and return a dictionary containing :
- The Robot object, which is the connection (as declared in RSK API)
- The robot's ID as a string (TODO: make it a number, by checking if input is valid)
"""


def setup_robot_connections(rsk_comm_ports: list[str]) -> dict[str, Robot]:
    robots_connections: dict[str, Robot] = {}
    for comm_port in rsk_comm_ports:
        r = Robot('/dev/' + comm_port)
        time.sleep(2)   # Let the robot wake up calmly
        r.control(0, 0, 20)
        time.sleep(1)   # Let it turn for 1 second
        r.control(0, 0, 0)

        # Ask user which ID he wants to name the little robot
        r_id = input('What ID do you want to the robot who just turned around ?')
        robots_connections[r_id] = r

    return robots_connections


"""
Asks the user which robot he wants to move, and makes it do
a little turn on the right (or the left, I don't know the difference)
"""


def user_turns_robot(robots_con: dict[str, Robot]) -> None:
    for _ in range(len(robots_con)):
        print(f"Available keys : {robots_con.keys()}")
        r_id = input("Which robot do you want to test ? ")
        robots_con[r_id].control(0, 0, 15)
        time.sleep(2)
        robots_con[r_id].control(0, 0, 0)
    return


def main():
    rsk_comm_ports = get_rsk_comm_ports()
    robots_connections = setup_robot_connections(rsk_comm_ports)
    user_turns_robot(robots_connections)
    exit(0)


if __name__ == '__main__':
    main()
