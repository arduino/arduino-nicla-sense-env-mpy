from .i2c_device import I2CDevice
from .constants import REGISTERS

class RGBLED(I2CDevice):
    """
    This class allows to control the RGB LED on the Nicla Sense Env board.
    """

    def enable_indoor_air_quality_status(self, brightness: int | None = None, persist: bool = False) -> bool:
        """
        Makes the RGB LED show the indoor air quality. (Green = Good, Yellow = Medium, Red = Bad)
        To do so it sets all RGB LED colors to 0 and sets the brightness to the specified value.
        Call store_settings_in_flash() on NiclaSenseEnv instance after enabling the indoor air quality status to make the change persistent.

        Parameters
        ----
            brightness (int, optional): 
                The brightness of the RGB LED.
                If None, the current brightness will be used.
            persist (bool, optional):
                Whether to persist the setting to flash memory.
                When persist is True, the brightness will also be persisted.
        """
        return self.set_color(0, 0, 0, brightness, persist)

    def set_color(self, color:tuple[int, int, int], brightness: int | None = None, persist: bool = False) -> bool:
        """
        Sets the RGB LED to the specified color. 
        Note: A value of 0, 0, 0 will set the color based on the IAQ value from the Indoor Air Quality sensor.
        Call store_settings_in_flash() on NiclaSenseEnv instance after changing the RGB LED color to make the change persistent.

        Parameters
        ----
            color (tuple[int, int, int]):
                The RGB color components red, green, blue
                The range for each color component is 0 to 255.            
            brightness (int, optional): 
                The brightness of the RGB LED. Range is 0 to 255.
                If None, the current brightness will be used.
            persist (bool, optional):
                Whether to persist the setting to flash memory.
                When persist is True, the brightness will also be persisted.
        """
        self._write_to_register(REGISTERS["rgb_led_red"], color[0])
        self._write_to_register(REGISTERS["rgb_led_green"], color[1])
        self._write_to_register(REGISTERS["rgb_led_blue"], color[2])
        
        if brightness is not None:            
            self._write_to_register(REGISTERS["rgb_led_intensity"], brightness)

        if persist:
            return self._persist_register(REGISTERS["rgb_led_red"]) and \
                   self._persist_register(REGISTERS["rgb_led_green"]) and \
                   self._persist_register(REGISTERS["rgb_led_blue"]) and \
                   self._persist_register(REGISTERS["rgb_led_intensity"])
        return True

    @property
    def color(self) -> tuple[int, int, int]:
        """
        Gets the RGB LED color.

        Returns
        ----
            tuple[int, int, int]: The RGB LED color. (red, green, blue)
        """
        red = self._read_from_register(REGISTERS["rgb_led_red"])
        green = self._read_from_register(REGISTERS["rgb_led_green"])
        blue = self._read_from_register(REGISTERS["rgb_led_blue"])
        return (red, green, blue)
    
    @color.setter
    def color(self, color: tuple[int, int, int]) -> None:
        """
        Sets the RGB LED color.
        Call store_settings_in_flash() on NiclaSenseEnv instance after changing the RGB LED color to make the change persistent.

        Parameters
        ----
            colors (tuple[int, int, int]): 
                The RGB color components red, green, blue
        """
        self.set_color(color)

    @property
    def brightness(self) -> int:
        """
        Gets the brightness of the RGB LED.

        Returns
        ----
            int: The brightness of the RGB LED. Range is 0 to 255.
        """
        return self._read_from_register(REGISTERS["rgb_led_intensity"])

    @brightness.setter
    def brightness(self, brightness: int) -> None:
        """
        Sets the brightness of the RGB LED.
        Call store_settings_in_flash() on NiclaSenseEnv instance after changing the RGB LED brightness to make the change persistent.

        Parameters
        ----
            brightness (int): 
                The brightness of the RGB LED. Range is 0 to 255.
        """
        if brightness < 0 or brightness > 255:
            raise ValueError("Brightness must be between 0 and 255")
        self._write_to_register(REGISTERS["rgb_led_intensity"], brightness)

    def set_brightness(self, brightness: int, persist: bool = False) -> bool:
        """
        Sets the brightness of the RGB LED.
        Call store_settings_in_flash() on NiclaSenseEnv instance after changing the RGB LED brightness to make the change persistent.

        Parameters
        ----
            brightness (int): 
                The brightness of the RGB LED. Range is 0 to 255.
            persist (bool, optional):
                Whether to persist the setting to flash memory.
                When persist is True, the color will also be persisted.
        """
        self.brightness = brightness
        
        if persist:
            return self._persist_register(REGISTERS["rgb_led_intensity"])
        return True