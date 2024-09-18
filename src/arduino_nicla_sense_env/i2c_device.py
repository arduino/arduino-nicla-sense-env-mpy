from machine import I2C
from time import sleep_us
import os
import struct
from .constants import DEVICE_I2C_INTERFACES, REGISTERS

class I2CHelper:
    """
    A helper class for interacting with I2C devices on supported boards.
    """

    @staticmethod
    def get_interface() -> I2C:
        """
        Returns an instance of the I2C interface for the current board.

        Raises:
            RuntimeError: If the current board is not supported.

        Returns:
            I2C: An instance of the I2C interface.
        """
        board_name = os.uname().machine.split(' with ')[0]
        interface_info = DEVICE_I2C_INTERFACES.get(board_name, None)

        if interface_info is None:
            raise RuntimeError(f"I2C interface couldn't be determined automatically for '{board_name}'.")

        if interface_info["type"] == "hw":
            return I2C(interface_info["interface"])

        if interface_info["type"] == "sw":
            from machine import SoftI2C, Pin
            return SoftI2C(scl=Pin(interface_info["scl"]) , sda=Pin(interface_info["sda"]))            


class I2CDevice:
    """
    Represents an I2C device connected to a bus.

    Attributes:
        DEFAULT_DEVICE_ADDRESS (int): The default I2C address of the device.
        bus (I2C): The I2C bus to use.
        device_address (int): The I2C address of the device.
        connected (bool):Checks if the device is connected to the I2C bus.
    """

    # The default I2C address of Nicla Sense Env
    DEFAULT_DEVICE_ADDRESS = 0x21

    def __init__(self, bus: I2C | None = None, device_address: int | None = DEFAULT_DEVICE_ADDRESS):
        """
        A initializes the NiclaSenseEnv device.

        Parameters:
            bus (I2C, optional): The I2C bus to use. If None, the default bus will be used.
            device_address (int, optional): The I2C address of the device. Defaults to 0x21.
        """
        
        if bus is None:
            self.bus = I2CHelper.get_interface()
        else:
            self.bus = bus
        
        self._device_address = device_address

    def _write_to_register(self, register: dict, data: int | float):
        """
        Writes data to the specified register over I2C.

        Parameters:
            register (dict): The register to write to.
            data (int/float): The data to write to the register.
                Number is converted into a byte array based on the register type and number of bytes.
                The endianness is big-endian, lowest address is LSB, highest address is MSB.
        """
        if data is None:
            raise ValueError("Data being written to registers cannot be None")

        if register["type"] == "float":
            # Convert float to 32 bit data
            converted_data = struct.pack('f', data)
        elif register["type"] == "uint8" and register["bytes"] == 1:
            # Convert integer to 8 bit data
            converted_data = data.to_bytes(1, 'big')
        elif register["type"] == "uint16" and register["bytes"] == 2:
            # Convert integer to 16 bit data
            converted_data = data.to_bytes(2, 'big')
        elif register["type"] == "uint32" and register["bytes"] == 4:
            # Convert integer to 32 bit data
            converted_data = data.to_bytes(4, 'big')
        else:
            raise ValueError("Unsupported register type")

        #print("Writing to device address 0x%x register 0x%x: 0x%x (%s)" %(self.device_address, register["address"], data, bin(data)))
        self.bus.writeto_mem(self.device_address, register["address"], converted_data)

    def _read_from_register(self, register: dict):
        """
        Reads data from the specified register over I2C.

        Parameters:
            register (dict): The register to read from.

        Returns:
            int/float: The data read from the register. 
            Data is converted automatically based on the register type and number of bytes.
        """

        raw_data = self.bus.readfrom_mem(self.device_address, register["address"], register["bytes"])        
        
        if register["type"] == "float":
            # Convert 32 bit data to float
            return struct.unpack('f', raw_data)[0]
        elif register["type"] == "uint8" and register["bytes"] == 1:
            # Convert 8 bit data to integer
            return int.from_bytes(raw_data, 'big')
        elif register["type"] == "uint16" and register["bytes"] == 2:
            # Convert 16 bit data to integer
            return int.from_bytes(raw_data, 'big')
        elif register["type"] == "uint32" and register["bytes"] == 4:
            # Convert 32 bit data to integer
            return int.from_bytes(raw_data, 'big')
        
        return raw_data
    
    def _persist_register(self, register: dict) -> bool:
        """
        Persists the value of the given register address to the flash memory.

        Parameters:
            register (dict): The register to persist.

        Returns:
            bool: True if the write was successful, False otherwise.
        """
        self._write_to_register(REGISTERS["defaults_register"], register["address"] | (1 << 7))
        
        # Read bit 7 to check if the write is complete. When the write is complete, bit 7 will be 0.
        # Try 10 times with increasing delay between each try
        for i in range(10):
            defaults_register_data = self._read_from_register(REGISTERS["defaults_register"])
            if not defaults_register_data & (1 << 7):
                return True
            print("⌛️ Waiting for flash write to complete...")
            # Exponential sleep duration
            sleep_us(100 * (2 ** i))

        return False

    @property
    def device_address(self) -> int | None:
        """
        Gets the I2C address of the device.

        Returns:
            int: The current I2C address.
        """
        return self._device_address

    @device_address.setter
    def device_address(self, address: int):
        # Needs to be implemented in subclasses.
        raise NotImplementedError("device_address setter not implemented")

    @property
    def connected(self):
        """
        Checks if the device is connected to the I2C bus.

        Returns:
            bool: True if the device is connected, False otherwise.
        """
        for addr in self.bus.scan():
            if addr == self.device_address:
                return True
        return False