from .i2c_device import I2CDevice
from .constants import REGISTERS

class WhiteLED(I2CDevice):
    """
    This class allows to control the white LED on the Nicla Sense Env board.
    """

    @property
    def brightness(self) -> int:
        """
        Gets the brightness of the white LED.

        Returns
        ----
            int: The brightness of the white LED. Range is 0 to 63.
        """
        # Read bits 0 - 5 from white_led register
        data = self._read_from_register(REGISTERS["white_led"])
        return data & 63

    @brightness.setter
    def brightness(self, led_brightness = 63) -> None:
        """
        Sets the brightness of the white LED.
        Call store_settings_in_flash() on NiclaSenseEnv instance after changing the white LED brightness to make the change persistent.

        Parameters
        ----
            led_brightness (int): 
                The brightness of the white LED. Range is 0 to 63.
        """
        if led_brightness < 0 or led_brightness > 63:
            raise ValueError("Brightness must be between 0 and 63")
        current_register_data = self._read_from_register(REGISTERS["white_led"])
        # Overwrite bits 0 - 5 with the new value by clearing the bits and then setting them
        self._write_to_register(REGISTERS["white_led"], (current_register_data & 0b11000000) | led_brightness)        

    @property
    def error_status_enabled(self) -> bool:
        """
        Determines whether the white LED is used to indicate an error status of one of the sensors.
        """
        # Read bit 7 from white_led register
        data = self._read_from_register(REGISTERS["white_led"])
        return bool(data & (1 << 7))
    
    @error_status_enabled.setter
    def error_status_enabled(self, enabled: bool) -> None:
        """
        Enables or disables the white LED to indicate an error status of one of the sensors.
        Call store_settings_in_flash() on NiclaSenseEnv instance after enabling/disabling the white LED error status to make the change persistent.

        Parameters
        ----
            enabled (bool): 
                Whether to enable or disable the white LED error status.
        """
        current_register_data = self._read_from_register(REGISTERS["white_led"])
        # Set bit 7 to 1 if enabled or 0 if disabled while keeping the other bits unchanged
        # by clearing bit 7 and then setting it to the desired value
        self._write_to_register(REGISTERS["white_led"], current_register_data & 0b01111111 | (int(enabled) << 7))
