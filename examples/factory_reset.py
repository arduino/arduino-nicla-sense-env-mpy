"""
This example shows how to restore the factory settings of the Nicla Sense Env.
"""

from arduino_nicla_sense_env import NiclaSenseEnv

# Change to your custom address if you have changed it before (e.g. 0x22)
DEVICE_ADDRESS = NiclaSenseEnv.DEFAULT_DEVICE_ADDRESS

device = NiclaSenseEnv(device_address=DEVICE_ADDRESS)

if device.connected:
    print(f"🔌 Device (0x{device.device_address:x}) connected.")
    success = device.restore_factory_settings()
    print(f"🔧 Factory settings restored: {success}")
else:
    print(f"🤷 Device with address 0x{DEVICE_ADDRESS:x} could not be found.")
    print("👀 Scanning for devices...")
    devices = device.bus.scan()
    if len(devices) == 0:
        print("🚫 No devices found. Please double check the wiring.")
    else:
        for addr in devices:
            print(f"🔌 Device found with address 0x{addr:x}")
        print("👉 Check if one of those is the Nicla Sense Env and change the address accordingly.")