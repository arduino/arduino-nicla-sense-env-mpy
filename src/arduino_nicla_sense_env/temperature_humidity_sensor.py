from .i2c_device import I2CDevice
from .constants import REGISTERS

class TemperatureHumiditySensor(I2CDevice):
    """
    Represents a HS4001 temperature and humidity sensor connected to an I2C bus.
    This class provides properties to read the temperature and humidity from the sensor.

    Properties
    -------
    temperature(self)
        Gets the temperature in degrees Celsius from the HS4001 sensor.
    humidity(self)
        Gets the humidity from the HS4001 sensor.
    """

    @property
    def temperature(self) -> float | None:
        """
        Gets the temperature in degrees Celsius from the HS4001 sensor.

        Returns:
            float: The temperature in degrees Celsius.
        """
        _temperature = self._read_from_register(REGISTERS["temperature"])
        # A value of 0x00 00 96 c3 (unpacked -300) indicates that the temperature sensor is not ready
        # This was discovered by trial and error
        if _temperature == -300:
            return None
        return _temperature

    @property
    def humidity(self) -> float:
        """
        Gets the humidity from the HS4001 sensor.

        Returns
        ----
            float: The humidity in %RH.
        """
        return self._read_from_register(REGISTERS["humidity"])
    

    @property
    def enabled(self) -> bool:
        """
        Gets the temperature sensor enabled status.

        Returns
        ----
            bool: True if the temperature sensor is enabled, False otherwise.
        """
        data = self._read_from_register(REGISTERS["status"])
        return bool(data & 1)

    @enabled.setter
    def enabled(self, is_enabled: bool):
        """
        Enables or disables the temperature sensor.
        Call store_settings_in_flash() on NiclaSenseEnv instance after enabling/disabling the temperature sensor to make the change persistent.

        Parameters
        ----
            is_enabled (bool): 
                Whether to enable or disable the temperature sensor.
        """
        current_register_data = self._read_from_register(REGISTERS["status"])

        # Check if existing value is already the same
        if bool(current_register_data & 1) == is_enabled:
            return

        # Clear bit 0 and then set it to the desired value
        self._write_to_register(REGISTERS["status"], (current_register_data & 0b11111110) | int(is_enabled))

    def set_enabled(self, is_enabled: bool, persist = False) -> bool:
        """
        Enables or disables the temperature sensor and persists the setting to flash memory.

        Parameters
        ----
            is_enabled (bool): 
                Whether to enable or disable the temperature sensor.
            persist (bool): 
                Whether to persist the setting to flash memory.
                When persist is True, the mode setting of IndoorAirQualitySensor and OutdoorAirQualitySensor will also be persisted.
        """
        self.enabled = is_enabled
        if persist:
            return self._persist_register(REGISTERS["status"])
        return True