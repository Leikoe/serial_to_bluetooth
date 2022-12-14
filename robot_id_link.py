import pydbus

# OS-dependant variables
BLUETOOTH_BUS = 'org.bluez'
BLUEZ_DEVICE_KEY = 'org.bluez.Device1'

# Assume that RSK robots are already paired & mounted on Bluetooth
def link_robot() -> bool:
    pass


"""
Get the robots currently paired & mounted with Bluetooth
Returns a list of full communication path names, such as '/dev/rfcommK'

Uses BlueZ and SystemBus object from pydbus module
"""


def get_paired_robots(name_filter: str) -> list:

    my_robots = []

    # Setup search of RSK robots
    bus = pydbus.SystemBus()
    bluez_manager = bus.get(BLUETOOTH_BUS, '/')
    bluetooth_devices = bluez_manager.GetManagedObjects()

    # Iterate over all available Bluetooth devices
    # First, define an iterator over all keys of the 'bluetooth_devices' dict
    keys_iterator = iter(bluetooth_devices.keys())
    try:
        while True:
            dev_key = next(keys_iterator)
            device = bluetooth_devices[dev_key]
            is_paired = device[BLUEZ_DEVICE_KEY]['Paired'] # TODO : is the 'Paired' keyword dependant of OS ?
            if name_filter in device[BLUEZ_DEVICE_KEY]['Name'] and is_paired:
                my_robots.append(device[BLUEZ_DEVICE_KEY])
    except StopIteration:
        return my_robots


if __name__ == '__main__':
    robs = get_paired_robots('RSK')
    print(robs)