"""
This example shows how to change the I2C address of the Nicla Sense Env board.
"""
from arduino_nicla_sense_env import NiclaSenseEnv
from time import sleep

CURRENT_I2C_ADDRESS = NiclaSenseEnv.DEFAULT_DEVICE_ADDRESS
CUSTOM_I2C_ADDRESS = 0x22

def check_connection(device):
    if device.connected:
        print(f"🔌 Device (0x{device.device_address:x}) is connected.")
    else:
        print(f"🤷 Device (0x{device.device_address:x}) could not be found. Please double check the wiring.")

device = NiclaSenseEnv(device_address=CURRENT_I2C_ADDRESS)
check_connection(device)

print(f"🔧 Changing device address to 0x{CUSTOM_I2C_ADDRESS:x}...")
device.set_device_address(CUSTOM_I2C_ADDRESS, persist=True)
check_connection(device)

print("🔄 Resetting device to check if change is persistent...")
device.reset()
sleep(2)
check_connection(device)