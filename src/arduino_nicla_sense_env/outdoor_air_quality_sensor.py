from .i2c_device import I2CDevice
from .constants import REGISTERS

# ZMOD4510 modes
class OutdoorAirQualitySensorMode:
    POWER_DOWN = 0
    CLEANING = 1
    OUTDOOR_AIR_QUALITY = 2
    DEFAULT = POWER_DOWN

class OutdoorAirQualitySensor(I2CDevice):

    @property
    def air_quality_index(self) -> int:
        """
        Gets the outdoor EPA air quality index from the ZMOD4510 sensor.
        The" EPA AQI" is strictly following the EPA standard and is based on 
        the 1-hour or 8-hour average of the O3 concentrations (concentration dependent).

        Returns:
            int: The outdoor air quality index. Range is 0 to 500.
        """
        return self._read_from_register(REGISTERS["zmod4510_epa_aqi"])

    @property
    def air_quality_index_interpreted(self) -> str:
        """
        Gets the outdoor air quality index from the ZMOD4510 sensor and interprets it in terms of air quality.

        Returns:
            str: The outdoor air quality index. 
            Possible values are: Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, Hazardous.
        """
        air_quality_value = self.air_quality_index
        if air_quality_value <= 50:
            return "Good"
        elif air_quality_value <= 100:
            return "Moderate"
        elif air_quality_value <= 150:
            return "Unhealthy for Sensitive Groups"
        elif air_quality_value <= 200:
            return "Unhealthy"
        elif air_quality_value <= 300:
            return "Very Unhealthy"
        else:
            return "Hazardous"

    @property
    def fast_air_quality_index(self) -> int:
        """
        Gets the fast outdoor air quality index from the ZMOD4510 sensor.
        As the standard averaging leads to a very slow response, especially during testing and evaluation, 
        "Fast AQI" provides quicker results with a 1-minute averaging.

        Returns
        ----
            int: The fast outdoor air quality index. Range is 0 to 500.
        """
        return self._read_from_register(REGISTERS["zmod4510_fast_aqi"])
    
    @property
    def no2(self) -> float:
        """
        Gets the NO2 concentration from the ZMOD4510 sensor.

        Returns
        ----
            float: The NO2 concentration in ppb.
        """
        return self._read_from_register(REGISTERS["zmod4510_no2"])
    
    @property
    def o3(self) -> float:
        """
        Gets the O3 concentration from the ZMOD4510 sensor.

        Returns
        ----
            float: The O3 concentration in ppb.
        """
        return self._read_from_register(REGISTERS["zmod4510_o3"])
    
    @property
    def mode(self) -> int:
        """
        Gets the outdoor air quality sensor (ZMOD4510) mode.
        The default mode is POWER_DOWN. This is because the sensor needs several hours to start 
        outputting valuable data due to the sensor's internal algorithm and chemical compound.

        Returns
        ----
            int: The outdoor air quality sensor mode.
            Possible values are: POWER_DOWN, CLEANING, OUTDOOR_AIR_QUALITY.
            This property represents the numeric value of the mode. See OutdoorAirQualitySensorMode for more information.
        """
        data = self._read_from_register(REGISTERS["status"])
        # Read bits 4 and 5
        return (data >> 4) & 3

    @mode.setter
    def mode(self, sensor_mode: int):
        """
        Sets the outdoor air quality sensor (ZMOD4510) mode.
        Call store_settings_in_flash() on NiclaSenseEnv instance after changing the outdoor air quality sensor mode to make the change persistent.

        Note on cleaning mode:
        The cleaning mode performs a thermal cleaning cycle of the MOx element. It can eliminate some light pollution 
        residues from production and packaging and improves the stabilization processes in the sensor. 
        The function heats up the sensor to allow thermal desorption and catalytic combustion of the residues. 
        The cleaning cycle can be executed only once in the sensor lifetime and shall be started after product assembly. 
        Please ensure cleaning was completed before power-off/reset and do not interrupt while cleaning.
        The cleaning procedure takes 1 minute (blocking).

        Parameters
        ----
            sensor_mode (int): 
                The outdoor air quality sensor mode.
                Possible values are: POWER_DOWN, CLEANING, OUTDOOR_AIR_QUALITY.
                These values are contained in OutdoorAirQualitySensorMode.
        """
        current_register_data = self._read_from_register(REGISTERS["status"])

        # Check if existing value (bit 4 - 5) is already the same
        if current_register_data & 0b110000 == sensor_mode:
            return

        # Overwrite bits 4 and 5 with the new value
        self._write_to_register(REGISTERS["status"], (current_register_data & 0b11001111) | (sensor_mode << 4))

    @property
    def mode_string(self) -> str | None:
        """
        Gets the outdoor air quality sensor mode as a string.

        Returns
        ----
            str: The outdoor air quality sensor mode.
            Possible values are: POWER_DOWN, CLEANING, OUTDOOR_AIR_QUALITY.
        """
        value = self.mode
        # Find the property name in the OutdoorAirQualitySensorMode class
        for key, val in OutdoorAirQualitySensorMode.__dict__.items():
            if val == value:
                return key
        return None

    @property
    def enabled(self) -> bool:
        """
        Gets the outdoor air quality sensor (ZMOD4410) enabled status.

        Returns
        ----
            bool: True if the outdoor air quality sensor mode is POWER_DOWN, False otherwise.
        """
        mode = self.mode
        return mode != OutdoorAirQualitySensorMode.POWER_DOWN

    @enabled.setter
    def enabled(self, is_enabled: bool):
        """
        Enables or disables the outdoor air quality sensor.
        Call store_settings_in_flash() on NiclaSenseEnv instance after enabling/disabling the outdoor air quality sensor to make the change persistent.
        When the sensor is enabled after being disabled, the sensor will go back to the default mode.

        Parameters
        ----
            is_enabled (bool): 
                Whether to enable or disable the outdoor air quality sensor.
        """
        # Ignore request if the sensor is already in desired state to maintain the current mode
        if is_enabled == self.enabled:
            return
        if is_enabled:
            self.mode = OutdoorAirQualitySensorMode.DEFAULT
        else:
            self.mode = OutdoorAirQualitySensorMode.POWER_DOWN
