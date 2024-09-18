from .i2c_device import I2CDevice
from .constants import REGISTERS

class OrangeLED(I2CDevice):
    """
    This class allows to control the orange LED on the Nicla Sense Env board.
    """

    @property
    def brightness(self) -> int:
        """
        Gets the brightness of the orange LED.

        Returns:
            int: The brightness of the orange LED. Range is 0 to 255.
        """
        # Read bits 0 - 5 from orange_led register
        data = self._read_from_register(REGISTERS["orange_led"])
        brightness = data & 63
        # Map brightness from 0-63 to 0-255
        return round((brightness * 255) / 63)

    @brightness.setter
    def brightness(self, led_brightness) -> None:
        """
        Sets the brightness of the orange LED.
        Use `set_brightness` with `persist` set to True to make the change persistent.

        Parameters:
            led_brightness (int): The brightness of the orange LED. Range is 0 to 63.
        """
        if led_brightness < 0 or led_brightness > 255:
            raise ValueError("Brightness must be between 0 and 255")
        
        # Map brightness from 0-255 to 0-63
        mapped_brightness = round((led_brightness * 63) / 255)
        current_register_data = self._read_from_register(REGISTERS["orange_led"])
        # Overwrite bits 0 - 5 with the new value by clearing the bits and then setting them
        self._write_to_register(REGISTERS["orange_led"], (current_register_data & 0b11000000) | mapped_brightness)        

    def set_brightness(self, led_brightness: int, persist: bool = False) -> bool:
        """
        Sets the brightness of the orange LED and persists the setting to flash memory.

        Parameters:
            led_brightness (int): The brightness of the orange LED. Range is 0 to 255.
            persist (bool): Whether to persist the setting to flash memory.
                When set to True, the value of `error_status_enabled` will also be persisted.
        """
        self.brightness = led_brightness
        if persist:
            return self._persist_register(REGISTERS["orange_led"])
        return True

    @property
    def error_status_enabled(self) -> bool:
        """
        Determines whether the orange LED is used to indicate an error status of one of the sensors.
        When a board error condition occurs the LED blinks, independently of the brightness setting.
        """
        # Read bit 7 from orange_led register
        data = self._read_from_register(REGISTERS["orange_led"])
        return bool(data & (1 << 7))
    
    @error_status_enabled.setter
    def error_status_enabled(self, enabled: bool) -> None:
        """
        Enables or disables the orange LED to indicate an error status of one of the sensors.
        Use `set_error_status_enabled` with `persist` set to True to make the change persistent.

        Parameters:
            enabled (bool): Whether to enable or disable the orange LED error status.
        """
        current_register_data = self._read_from_register(REGISTERS["orange_led"])
        # Set bit 7 to 1 if enabled or 0 if disabled while keeping the other bits unchanged
        # by clearing bit 7 and then setting it to the desired value
        self._write_to_register(REGISTERS["orange_led"], current_register_data & 0b01111111 | (int(enabled) << 7))

    def set_error_status_enabled(self, enabled: bool, persist: bool = False) -> bool:
        """
        Enables or disables the orange LED to indicate an error status of one of the sensors and persists the setting to flash memory.

        Parameters:
            enabled (bool): Whether to enable or disable the orange LED error status.
            persist (bool): Whether to persist the setting to flash memory.
                When set to True, the value of `brightness` will also be persisted.
        """
        self.error_status_enabled = enabled
        if persist:
            return self._persist_register(REGISTERS["orange_led"])
        return True