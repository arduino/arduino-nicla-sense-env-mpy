from .i2c_device import I2CDevice
from .constants import REGISTERS

# ZMOD4410 modes
class IndoorAirQualitySensorMode:
    POWER_DOWN = 0
    CLEANING = 1
    INDOOR_AIR_QUALITY = 2
    INDOOR_AIR_QUALITY_LOW_POWER = 3
    PBAQ = 4
    SULFUR = 5
    DEFAULT = INDOOR_AIR_QUALITY


class IndoorAirQualitySensor(I2CDevice):
    """
    Class for interacting with the indoor air quality sensor.

    Properties
    ----
        sulfur_odor (bool): 
            True if the sulfur odor is detected, False otherwise.
        odor_intensity (float): 
            The odor intensity.
        ethanol (float): 
            The ethanol concentration in ppm.
        co2 (float): 
            The CO2 concentration in ppm.
        tvoc (float): 
            The TVOC concentration in mg/m3.
        air_quality (float): 
            The indoor air quality. Range is 0 to 5.
        air_quality_interpreted (str): 
            The indoor air quality.
        relative_air_quality (float): 
            The relative indoor air quality. Range is 0 to 100.
        mode (int): 
            The indoor air quality sensor mode.
        mode_string (str): 
            The indoor air quality sensor mode.
        enabled (bool): 
            True if the indoor air quality sensor mode is POWER_DOWN, False otherwise.
    """

    @property
    def sulfur_odor(self) -> bool:
        """
        Gets the sulfur odor status from the ZMOD4410 sensor.

        Returns:
            bool: True if the sulfur odor is detected, False otherwise.
        """
        return self._read_from_register(REGISTERS["zmod4410_odor_class"]) == 1
    
    @property
    def odor_intensity(self) -> float:
        """
        Gets the odor intensity from the ZMOD4410 sensor.

        Returns:
            float: The odor intensity.
        """
        return self._read_from_register(REGISTERS["zmod4410_intensity"])
    
    @property
    def ethanol(self) -> float:
        """
        Gets the ethanol concentration from the ZMOD4410 sensor.

        Returns:
            float: The ethanol concentration in ppm.        
        """
        return self._read_from_register(REGISTERS["zmod4410_etoh"])
    
    @property
    def co2(self) -> float:
        """
        Gets the CO2 concentration from the ZMOD4410 sensor.

        Returns:
            float: The CO2 concentration in ppm.
        """
        return self._read_from_register(REGISTERS["zmod4410_eco2"])
    
    @property
    def tvoc(self) -> float:
        """
        Gets the TVOC concentration from the ZMOD4410 sensor.

        Returns:
            float: The TVOC concentration in mg/m3.
        """
        return self._read_from_register(REGISTERS["zmod4410_tvoc"])
    
    @property
    def air_quality(self) -> float:
        """
        Gets the indoor air quality from the ZMOD4410 sensor.

        Returns:
            float: The indoor air quality. Range is 0 to 5 where 0 is the best air quality and 5 is the worst.
        """
        return self._read_from_register(REGISTERS["zmod4410_iaq"])

    @property
    def air_quality_interpreted(self) -> str:
        """
        Gets the indoor air quality from the ZMOD4410 sensor and interprets it in terms of air quality.

        Returns:
            str: The indoor air quality. Possible values are: Very Good, Good, Medium, Poor, Bad.
        """

        iaq_value = self.air_quality
        if iaq_value <= 1.99:
            return "Very Good"
        elif iaq_value <= 2.99:
            return "Good"
        elif iaq_value <= 3.99:
            return "Medium"
        elif iaq_value <= 4.99:
            return "Poor"
        else:
            return "Bad"

    @property
    def relative_air_quality(self) -> float:
        """
        Gets the relative indoor air quality from the ZMOD4410 sensor.

        Returns:
            float: The relative indoor air quality. Range is 0 to 100.
        """
        return self._read_from_register(REGISTERS["zmod4410_rel_iaq"])


    @property
    def mode(self) -> int:
        """
        Gets the indoor air quality sensor mode.
        
        Returns:
            int: The indoor air quality sensor mode.
            Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.
            This property represents the numeric value of the mode. See IndoorAirQualitySensorMode for more information.            
        """
        data = self._read_from_register(REGISTERS["status"])
        # Read three bits: 1 - 3.
        return (data >> 1) & 0b111
        
    @mode.setter
    def mode(self, sensor_mode: int):
        """
        Sets the indoor air quality sensor mode.
        Use `set_mode` with `persist` set to True to make the change persistent.

        Note on cleaning mode:
        The cleaning mode performs a thermal cleaning cycle of the MOx element. It can eliminate some light pollution 
        residues from production and packaging and improves the stabilization processes in the sensor. 
        The function heats up the sensor to allow thermal desorption and catalytic combustion of the residues. 
        The cleaning cycle can be executed only once in the sensor lifetime and shall be started after product assembly. 
        Please ensure cleaning was completed before power-off/reset and do not interrupt while cleaning.
        The cleaning procedure takes 1 minute (blocking).
        
        Note on PBAQ mode:
        The PBAQ mode is a special mode to perform highly accurate and consistent air quality readings.
        It measures the total volatile organic compounds (TVOC) and equivalent ethanol (EtOH) concentration 
        to meet Public Building Air Quality (PBAQ) standards.

        Note on low power IAQ mode:
        This mode offers a much lower power consumption while keeping accurate and consistent sensor readings.
        For more accurate readings, use the default indoor air quality mode.

        Args:
            sensor_mode (int): The indoor air quality sensor mode.
                Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.
                These values are contained in IndoorAirQualitySensorMode.
        """
        current_register_data = self._read_from_register(REGISTERS["status"])

        # Check if existing value is already the same (bits 1 - 3)
        if current_register_data & 0b1110 == sensor_mode:
            return

        # Overwrite bits 1 - 3 with the new value by clearing the bits and then setting them    
        self._write_to_register(REGISTERS["status"], (current_register_data & 0b11110001) | (sensor_mode << 1))

    def set_mode(self, sensor_mode: int, persist = False) -> bool:
        """
        Sets the indoor air quality sensor mode and persists the setting to flash memory.

        Args:
            sensor_mode (int): The indoor air quality sensor mode.
                Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.
                These values are contained in IndoorAirQualitySensorMode.
            persist (bool): Whether to persist the setting to flash memory.
                When persist is True, the mode setting of OutdoorAirQualitySensor and TemperatureHumiditySensor will also be persisted.
        """
        self.mode = sensor_mode
        if persist:
            return self._persist_register(REGISTERS["status"])
        return True

    @property
    def mode_string(self) -> str | None:
        """
        Gets the indoor air quality sensor mode as a string.

        Returns:
            str: The indoor air quality sensor mode.
            Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.
        """
        value = self.mode
        # Find the property name in the IndoorAirQualitySensorMode class
        for key, val in IndoorAirQualitySensorMode.__dict__.items():
            if val == value:
                return key
        return None

    @property
    def enabled(self) -> bool:
        """
        Gets the indoor air quality sensor enabled status.

        Returns:
            bool: True if the indoor air quality sensor mode is POWER_DOWN, False otherwise.
        """
        mode = self.mode
        return mode != IndoorAirQualitySensorMode.POWER_DOWN

    @enabled.setter
    def enabled(self, is_enabled: bool):
        """
        Enables or disables the indoor air quality sensor.
        Use `set_enabled` with `persist` set to True to make the change persistent.
        When the sensor is enabled after being disabled, the sensor will go back to the default mode.

        Args:
            is_enabled (bool): Whether to enable or disable the indoor air quality sensor.
        """
        # Ignore request if the sensor is already in desired state to maintain the current mode
        if is_enabled == self.enabled:
            return
        if is_enabled:
            self.mode = IndoorAirQualitySensorMode.DEFAULT
        else:
            self.mode = IndoorAirQualitySensorMode.POWER_DOWN

    def set_enabled(self, is_enabled: bool, persist = False) -> bool:
        """
        Enables or disables the indoor air quality sensor and persists the setting to flash memory.

        Args:
            is_enabled (bool): Whether to enable or disable the indoor air quality sensor.
            persist (bool): Whether to persist the setting to flash memory.
                When persist is True, the mode setting of OutdoorAirQualitySensor and TemperatureHumiditySensor will also be persisted.
        """
        self.enabled = is_enabled
        if persist:
            return self._persist_register(REGISTERS["status"])
        return True