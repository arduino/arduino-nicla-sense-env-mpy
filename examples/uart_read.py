"""
This example shows how to read data from the UART port on the board.
It is meant to run on a board only connected through UART to the Nicla Sense Env.
This requires the Nicla Sense Env to be powered through the VIN pin.

UART output needs to be enabled on the Nicla Sense Env for this example to work.
You can do so by connecting to the board over I2C to a host board, and running the following code:

device = NiclaSenseEnv()
# Set `persist` to True so the settings are not lost after a reset
device.set_uart_csv_output_enabled(True, persist=True)
"""

from machine import Pin, UART
import time

DEFAULT_DELIMITER = ","
DEFAULT_BAUDRATE = 38400

# Change this to the UART interface you would like to use
uart_interface = 0
uart = UART(uart_interface, baudrate=DEFAULT_BAUDRATE)
uart.init(bits=8, parity=None, stop=1)
led = Pin("LED", Pin.OUT) # Onboard LED to indicate availability of data

csv_field_mapping = {
    0: {"name": "HS4001 sample counter", "type": "uint32"},
    1: {"name": "HS4001 temperature (degC)", "type": "float"},
    2: {"name": "HS4001 humidity (%RH)", "type": "float"},
    3: {"name": "ZMOD4510 status", "type": "uint8"},
    4: {"name": "ZMOD4510 sample counter", "type": "uint32"},
    5: {"name": "ZMOD4510 EPA AQI", "type": "uint16"},
    6: {"name": "ZMOD4510 Fast AQI", "type": "uint16"},
    7: {"name": "ZMOD4510 O3 (ppb)", "type": "float"},
    8: {"name": "ZMOD4510 NO2 (ppb)", "type": "float"},
    9: {"name": "ZMOD4510 Rmox[0]", "type": "float"},
    10: {"name": "ZMOD4510 Rmox[1]", "type": "float"},
    11: {"name": "ZMOD4510 Rmox[2]", "type": "float"},
    12: {"name": "ZMOD4510 Rmox[3]", "type": "float"},
    13: {"name": "ZMOD4510 Rmox[4]", "type": "float"},
    14: {"name": "ZMOD4510 Rmox[5]", "type": "float"},
    15: {"name": "ZMOD4510 Rmox[6]", "type": "float"},
    16: {"name": "ZMOD4510 Rmox[7]", "type": "float"},
    17: {"name": "ZMOD4510 Rmox[8]", "type": "float"},
    18: {"name": "ZMOD4510 Rmox[9]", "type": "float"},
    19: {"name": "ZMOD4510 Rmox[10]", "type": "float"},
    20: {"name": "ZMOD4510 Rmox[11]", "type": "float"},
    21: {"name": "ZMOD4510 Rmox[12]", "type": "float"},
    22: {"name": "ZMOD4410 status", "type": "uint8"},
    23: {"name": "ZMD4410 sample counter", "type": "uint32"},
    24: {"name": "ZMOD4410 IAQ", "type": "float"},
    25: {"name": "ZMOD4410 TVOC (mg/m^3)", "type": "float"},
    26: {"name": "ZMOD4410 eCO2 (ppm)", "type": "float"},
    27: {"name": "ZMOD4410 Rel IAQ", "type": "float"},
    28: {"name": "ZMOD4410 EtOH (ppm)", "type": "float"},
    29: {"name": "ZMOD4410 Rmox[0]", "type": "float"},
    30: {"name": "ZMOD4410 Rmox[1]", "type": "float"},
    31: {"name": "ZMOD4410 Rmox[2]", "type": "float"},
    32: {"name": "ZMOD4410 Rmox[3]", "type": "float"},
    33: {"name": "ZMOD4410 Rmox[4]", "type": "float"},
    34: {"name": "ZMOD4410 Rmox[5]", "type": "float"},
    35: {"name": "ZMOD4410 Rmox[6]", "type": "float"},
    36: {"name": "ZMOD4410 Rmox[7]", "type": "float"},
    37: {"name": "ZMOD4410 Rmox[8]", "type": "float"},
    38: {"name": "ZMOD4410 Rmox[9]", "type": "float"},
    39: {"name": "ZMOD4410 Rmox[10]", "type": "float"},
    40: {"name": "ZMOD4410 Rmox[11]", "type": "float"},
    41: {"name": "ZMOD4410 Rmox[12]", "type": "float"},
    42: {"name": "ZMOD4410 Rcda[0]", "type": "float"},
    43: {"name": "ZMOD4410 Rcda[1]", "type": "float"},
    44: {"name": "ZMOD4410 Rcda[2]", "type": "float"},
    45: {"name": "ZMOD4410 Rhtr", "type": "float"},
    46: {"name": "ZMOD4410 Temp", "type": "float"},
    47: {"name": "ZMOD4410 intensity", "type": "float"},
    48: {"name": "ZMOD4410 odor", "type": "uint8"}
}

def decode_value(value, data_type):
    value = value.strip()
    if not value:
        return None

    try:
        if data_type in ["uint8", "uint16", "uint32"]:
            # Avoid ValueError by converting to float first
            # since float notation is used for integers
            return int(float(value))
        elif data_type == "float":
            return float(value)
        else:
            return value
    except ValueError:
        print(f"WARNING: Could not decode value {value} as {data_type}")
        return value

def parse_line(data, delimiter=DEFAULT_DELIMITER):
    # Convert data to string
    csv_data = data.decode()

    # Strip NULL character from the string
    # This is a workaround for a bug in the firmware that prints a NULL character
    # at the start of debug messages
    csv_data = csv_data.strip('\x00')
    
    # Strip trailing line feed character from the string as
    # the readline() method returns the line including the line feed
    csv_data = csv_data.strip('\n')

    # Skip empty lines
    if not csv_data:
        return None

    # Skip lines that start with INFO: or WARNING:
    if csv_data.startswith("INFO:") or csv_data.startswith("WARNING:"):        
        return None
    
    if csv_data.startswith("ERROR:"):
        raise Exception(csv_data)

    # Convert string to an enumerated list
    enumerated_list = enumerate(csv_data.split(delimiter))
    
    mapped_values = map(lambda enumerated_item: (
                    # enumerated_item[0] is the index of the item in the list of CSV values
                    # enumerated_item[1] is the value of that item
                    csv_field_mapping[enumerated_item[0]]["name"],
                    decode_value(enumerated_item[1], csv_field_mapping[enumerated_item[0]].get("type", ""))
                ), enumerated_list)

    # Filter out empty elements
    filtered_values = dict(filter(lambda item: item[1] is not None, mapped_values))
    return filtered_values

while True:
    if uart.any():
        led.on()
        data = uart.readline()
        value = parse_line(data)
        
        try:
            if value:
                print(value)
        except Exception as e:
            print(f"ERROR: {e}")

    else:
        led.off()
    
    time.sleep(1)
