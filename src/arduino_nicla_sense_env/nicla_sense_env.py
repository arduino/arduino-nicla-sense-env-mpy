from time import sleep_us

from .temperature_humidity_sensor import TemperatureHumiditySensor
from .indoor_air_quality_sensor import IndoorAirQualitySensor
from .outdoor_air_quality_sensor import OutdoorAirQualitySensor
from .rgb_led import RGBLED
from .orange_led import OrangeLED
from .i2c_device import I2CDevice
from .constants import REGISTERS

class NiclaSenseEnv(I2CDevice):

    def __init__(self, bus=None, device_address=I2CDevice.DEFAULT_DEVICE_ADDRESS):
        super().__init__(bus, device_address)
        self._temperature_humidity_sensor = None
        self._indoor_air_quality_sensor = None
        self._outdoor_air_quality_sensor = None

    def persist_settings(self):
        """
        Writes the current configuration to the flash memory.
        Stores board register 0x00 ... 0x0B in flash to be default after reset
        This affects the following properties:
        - UART baud rate
        - UART CSV output enabled
        - CSV delimiter
        - UART Debugging enabled
        - I2C Device address
        - Indoor air quality sensor mode
        - Outdoor air quality sensor mode
        - Temperature sensor enabled
        - Orange LED brightness
        - Orange LED error status enabled
        - RGB LED brightness
        - RGB LED color

        Make sure all these properties are in the desired state before calling this method.

        Returns:
            bool: True if the write was successful, False otherwise.
        """
        # Set bit 7 to 1 to write the current config to the flash memory
        control_register_data = self._read_from_register(REGISTERS["control"])

        if control_register_data is None:
            raise RuntimeError("💣 Could not read from control register. This should not happen!")

        self._write_to_register(REGISTERS["control"], control_register_data | (1 << 7))

        # Read bit 7 to check if the write is complete. When the write is complete, bit 7 will be 0.
        # Try 10 times with increasing delay between each try
        for i in range(10):
            control_register_data = self._read_from_register(REGISTERS["control"])
            if not control_register_data & (1 << 7):
                return True
            # Even a value of 1 us seems to work but we start with 100 us to be safe.
            print("⌛️ Waiting for flash write to complete...")
            # Exponential sleep duration
            sleep_us(100 * (2 ** i))
        return False

    @property
    def serial_number(self):
        """
        Gets the serial number of the device.

        Returns:
            str: The serial number as a string.
        """
        raw_data = self._read_from_register(REGISTERS["serial_number"])
        # Construct serial number by concatenating each of the 6 bytes as a string
        return "".join([str(sn_byte) for sn_byte in raw_data])
    
    @property
    def product_id(self):
        """
        Gets the product ID of the device.

        Returns:
            int: The numeric product ID.
        """
        return self._read_from_register(REGISTERS["product_id"])
    
    @property
    def software_revision(self):
        """
        Gets the software revision of the device.

        Returns:
            int: The numeric software revision.
        """
        return self._read_from_register(REGISTERS["sw_revision"])

    @property
    def temperature_humidity_sensor(self):
        """
        Gets the temperature and humidity sensor control interface.

        Returns:
            TemperatureHumiditySensor: The temperature and humidity sensor.
        """
        if not self._temperature_humidity_sensor:
            self._temperature_humidity_sensor = TemperatureHumiditySensor(self.bus, self.device_address)
        return self._temperature_humidity_sensor

    @property
    def indoor_air_quality_sensor(self):
        """
        Gets the indoor air quality sensor control interface.

        Returns:
            IndoorAirQualitySensor: The indoor air quality sensor.
        """
        if not self._indoor_air_quality_sensor:
            self._indoor_air_quality_sensor = IndoorAirQualitySensor(self.bus, self.device_address)
        return self._indoor_air_quality_sensor

    @property
    def outdoor_air_quality_sensor(self):
        """
        Gets the outdoor air quality sensor control interface.

        Returns:
            OutdoorAirQualitySensor: The outdoor air quality sensor.
        """
        if not self._outdoor_air_quality_sensor:
            self._outdoor_air_quality_sensor = OutdoorAirQualitySensor(self.bus, self.device_address)
        return self._outdoor_air_quality_sensor

    @property
    def rgb_led(self):
        """
        Gets the RGB LED control interface.

        Returns:
            RGBLED: The RGB LED.
        """
        return RGBLED(self.bus, self.device_address)

    @property
    def orange_led(self):
        """
        Gets the orange LED control interface.

        Returns:
            OrangeLED: The orange LED.
        """
        return OrangeLED(self.bus, self.device_address)

    def reset(self):
        """
        Performs a reset of the module and sensors.
        """
        current_register_data = self._read_from_register(REGISTERS["status"])
        self._write_to_register(REGISTERS["status"], current_register_data | (1 << 7))

    def deep_sleep(self):
        """
        Puts the board in deep sleep. The board can only be woken up by a hardware reset.
        """
        current_register_data = self._read_from_register(REGISTERS["status"])
        self._write_to_register(REGISTERS["status"], current_register_data | (1 << 6))

    def restore_factory_settings(self):
        """
        Restores the factory settings. This will reset among other properties the device address to the default value.
        See persist_settings() for a complete list of properties that are affected by this method.
        """

        board_control_register_data = self._read_from_register(REGISTERS["control"])
        # Set bit 5 to 1 while keeping the other bits unchanged
        self._write_to_register(REGISTERS["control"], board_control_register_data | (1 << 5))
        sleep_us(100) # Wait for the default I2C address recovery to take effect (if changed)
        self._device_address = self.DEFAULT_DEVICE_ADDRESS

        # Try 10 times with increasing delay between each try
        for i in range(10):
            # Read bit 5 to check if the reset is complete. When the reset is complete, bit 5 will be 0.
            board_control_register_data = self._read_from_register(REGISTERS["control"])
            
            if board_control_register_data != None and (not board_control_register_data & (1 << 5)):
                return self.persist_settings()
            print("⌛️ Waiting for factory reset to complete...")
            # Exponential sleep duration
            sleep_us(100 * (2 ** i))
        return False

    @property
    def uart_baud_rate(self):
        """
        Get the current baud rate of the UART communication.
        The supported values are: 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200

        Returns
        ---
            int: the current baud rate
        """
        # Read bit 0 - 2 from uart_control register
        data = self._read_from_register(REGISTERS["uart_control"]) & 7
        # Return mapped value
        return {
            0: 1200,
            1: 2400,
            2: 4800,
            3: 9600,
            4: 19200,
            5: 38400,
            6: 57600,
            7: 115200,
        }.get(data, None)

    @uart_baud_rate.setter
    def uart_baud_rate(self, baud_rate):
        """
        Set the baud rate of the UART interface.
        Use `set_uart_baud_rate` with `persist` set to True to make the change persistent.

        Args:
            baud_rate (int): the new baud rate.
                The supported values are: 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200

        Raises:
            ValueError: if the baud rate is invalid
        """
        # Get the mapped value
        baud_rate = {
            1200: 0,
            2400: 1,
            4800: 2,
            9600: 3,
            19200: 4,
            38400: 5,
            57600: 6,
            115200: 7,
        }.get(baud_rate, None)

        if baud_rate is None:
            raise ValueError("Invalid baud rate")

        uart_control_register_data = self._read_from_register(REGISTERS["uart_control"])
        # Check if value is already the same
        if uart_control_register_data & 0b111 == baud_rate:
            return
        # Set bit 0 - 2 to the new baud rate
        self._write_to_register(REGISTERS["uart_control"], (uart_control_register_data & 0b11111000) | baud_rate)
    
    def set_uart_baud_rate(self, baud_rate, persist=False) -> bool:
        self.uart_baud_rate = baud_rate
        if persist:
            return self._persist_register(REGISTERS["uart_control"])
        return True

    @property
    def uart_csv_output_enabled(self):
        """
        Determines if CSV output over UART is enabled.
        
        Returns:
            bool: Whether CSV output over UART is enabled.
        """
        # Read bit 1 from uart_control register
        data = self._read_from_register(REGISTERS["control"])
        return bool(data & 0b10)

    @uart_csv_output_enabled.setter
    def uart_csv_output_enabled(self, enabled):
        """
        Enables or disables CSV output over UART.
        Use `set_uart_csv_output_enabled` with `persist` set to True to make the change persistent.

        The column names and their order are:
        HS4001 sample counter, HS4001 temperature (degC), HS4001 humidity (%RH), ZMOD4510 status, ZMOD4510 sample counter, 
        ZMOD4510 EPA AQI, ZMOD4510 Fast AQI, ZMOD4510 O3 (ppb), ZMOD4510 NO2 (ppb), ZMOD4510 Rmox[0], ZMOD4510 Rmox[1], ZMOD4510 Rmox[2], 
        ZMOD4510 Rmox[3], ZMOD4510 Rmox[4], ZMOD4510 Rmox[5], ZMOD4510 Rmox[6], ZMOD4510 Rmox[7], ZMOD4510 Rmox[8], ZMOD4510 Rmox[9], ZMOD4510 Rmox[10], 
        ZMOD4510 Rmox[11], ZMOD4510 Rmox[12], ZMOD4410 status, ZMD4410 sample counter, ZMOD4410 IAQ, ZMOD4410 TVOC (mg/m^3), ZMOD4410 eCO2 (ppm), 
        ZMOD4410 Rel IAQ, ZMOD4410 EtOH (ppm), ZMOD4410 Rmox[0], ZMOD4410 Rmox[1], ZMOD4410 Rmox[2], ZMOD4410 Rmox[3], ZMOD4410 Rmox[4], ZMOD4410 Rmox[5], 
        ZMOD4410 Rmox[6], ZMOD4410 Rmox[7], ZMOD4410 Rmox[8], ZMOD4410 Rmox[9], ZMOD4410 Rmox[10], ZMOD4410 Rmox[11], ZMOD4410 Rmox[12], ZMOD4410 Rcda[0], 
        ZMOD4410 Rcda[1], ZMOD4410 Rcda[2], ZMOD4410 Rhtr, ZMOD4410 Temp, ZMOD4410 intensity, ZMOD4410 odor
        The csv formatted line is sent when a sensor finishes a measurement. 
        Only the columns for this sensor will be filled, the other columns will be empty.


        Args:
            enabled (bool): Whether to enable or disable CSV output over UART.
        """
        board_control_register_data = self._read_from_register(REGISTERS["control"])

        # Check if existing value is already the same
        if bool(board_control_register_data & 2) == enabled:
            return

        # Set bit 1 to 1 if enabled or 0 if disabled while keeping the other bits unchanged
        self._write_to_register(REGISTERS["control"], (board_control_register_data & 0b11111101) | (int(enabled) << 1))
        
    def set_uart_csv_output_enabled(self, enabled, persist=False) -> bool:
        """
        Enables or disables CSV output over UART.

        Args:
            enabled (bool): Whether to enable or disable CSV output over UART.
            persist (bool): Whether to persist the change to flash memory.
                When set to True, it will also persist the value of `debugging_enabled`.
        """
        self.uart_csv_output_enabled = enabled
        if persist:
            return self._persist_register(REGISTERS["control"])
        return True

    @property
    def csv_delimiter(self):
        """
        Gets the delimiter character for CSV output.

        Returns:
            str: The delimiter character. A single printable ASCII character.
        """
        # Read the ASCII code of the delimiter character from csv_delimiter register
        data = self._read_from_register(REGISTERS["csv_delimiter"])
        return chr(data)

    @csv_delimiter.setter
    def csv_delimiter(self, delimiter):
        """
        Sets the delimiter character for CSV output.
        Use `set_csv_delimiter` with `persist` set to True to make the change persistent.

        Args:
            delimiter (str): The new delimiter character. Must be a single printable ASCII character.
                The following characters are not allowed: \r, \n, \, ", '
        """
        if self.csv_delimiter == delimiter:
            return

        prohibited_delimiters = ["\r", "\n", "\\", "\"", "\'"]
        if len(delimiter) != 1:
            raise ValueError("Delimiter must be a single character")
        if ord(delimiter) < 32 or ord(delimiter) > 126:
            raise ValueError("Delimiter must be a printable ASCII character")
        if delimiter in prohibited_delimiters:
            raise ValueError("Delimiter is not allowed")    

        # Use ASCII code of the delimiter character
        self._write_to_register(REGISTERS["csv_delimiter"], ord(delimiter))

    def set_csv_delimiter(self, delimiter, persist=False) -> bool:
        """
        Sets the delimiter character for CSV output.

        Args:
            delimiter (str): The new delimiter character. Must be a single printable ASCII character.
                The following characters are not allowed: \r, \n, \, ", '
            persist (bool): Whether to persist the change to flash memory.
        """
        self.csv_delimiter = delimiter
        if persist:
            return self._persist_register(REGISTERS["csv_delimiter"])    
        return True
    
    @property
    def debugging_enabled(self):
        """
        Determines if debugging mode is enabled.
        When debugging mode is enabled, the board will send additional debug messages over UART.
        
        Returns:
            bool: Whether debugging mode is enabled.
        """
        # Read bit 0 from control register
        data = self._read_from_register(REGISTERS["control"])
        return bool(data & 1)
    
    @debugging_enabled.setter
    def debugging_enabled(self, enabled):
        """
        Enables or disables debugging mode.
        When debugging mode is enabled, the board will send additional debug messages over UART.
        Use `set_debugging_enabled` with `persist` set to True to make the change persistent.

        Args:
            enabled (bool): Whether to enable or disable debugging mode.
        """
        board_control_register_data = self._read_from_register(REGISTERS["control"])

        # Check if existing value is already the same
        if bool(board_control_register_data & 1) == enabled:
            return

        # Set bit 0 to 1 if enabled or 0 if disabled while keeping the other bits unchanged
        self._write_to_register(REGISTERS["control"], board_control_register_data & 0b11111110 | int(enabled))

    def set_debugging_enabled(self, enabled, persist=False) -> bool:
        """
        Enables or disables debugging mode.

        Args:
            enabled (bool): Whether to enable or disable debugging mode.
            persist (bool): Whether to persist the change to flash memory.
                When set to True, it will also persist the value of `uart_csv_output_enabled`.
        """
        self.debugging_enabled = enabled
        if persist:
            return self._persist_register(REGISTERS["control"])
        return True

    @I2CDevice.device_address.setter
    def device_address(self, address):
        """
        Sets the I2C address of the device.
        Use `set_device_address` with `persist` set to True to make the change persistent.

        Args:
            address (int): The new I2C address. Valid values are 0 to 127.

        Raises:
            ValueError: if the address is invalid
        """
        # Ensure that the address is in the valid range (0 to 127)
        if address < 0 or address > 127:
            raise ValueError("Address must be between 0 and 127")
        
        address_register_data = self._read_from_register(REGISTERS["slave_address"])

        # Check if existing address is already the same
        if address_register_data & 127 == address:
            return

        # Set the new address by overwriting bit 0 - 6
        self._write_to_register(REGISTERS["slave_address"], (address_register_data & 0b10000000) | address)
        sleep_us(100) # Wait for the new address to take effect
        self._device_address = address

    def set_device_address(self, address, persist=False) -> bool:
        """
        Sets the I2C address of the device.

        Args:
            address (int): The new I2C address. Valid values are 0 to 127.
            persist (bool): Whether to persist the change to flash memory.
        """
        self.device_address = address
        if persist:
            return self._persist_register(REGISTERS["slave_address"])
        return True