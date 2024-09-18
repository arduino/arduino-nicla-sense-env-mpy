# Summary

* [arduino\_nicla\_sense\_env](#arduino_nicla_sense_env)
* [orange\_led](#arduino_nicla_sense_env.orange_led)
  * [OrangeLED](#arduino_nicla_sense_env.orange_led.OrangeLED)
    * [brightness](#arduino_nicla_sense_env.orange_led.OrangeLED.brightness)
    * [brightness](#arduino_nicla_sense_env.orange_led.OrangeLED.brightness)
    * [set\_brightness](#arduino_nicla_sense_env.orange_led.OrangeLED.set_brightness)
    * [error\_status\_enabled](#arduino_nicla_sense_env.orange_led.OrangeLED.error_status_enabled)
    * [error\_status\_enabled](#arduino_nicla_sense_env.orange_led.OrangeLED.error_status_enabled)
    * [set\_error\_status\_enabled](#arduino_nicla_sense_env.orange_led.OrangeLED.set_error_status_enabled)
* [i2c\_device](#arduino_nicla_sense_env.i2c_device)
  * [I2CHelper](#arduino_nicla_sense_env.i2c_device.I2CHelper)
    * [get\_interface](#arduino_nicla_sense_env.i2c_device.I2CHelper.get_interface)
  * [I2CDevice](#arduino_nicla_sense_env.i2c_device.I2CDevice)
    * [\_\_init\_\_](#arduino_nicla_sense_env.i2c_device.I2CDevice.__init__)
    * [device\_address](#arduino_nicla_sense_env.i2c_device.I2CDevice.device_address)
    * [connected](#arduino_nicla_sense_env.i2c_device.I2CDevice.connected)
* [rgb\_led](#arduino_nicla_sense_env.rgb_led)
  * [RGBLED](#arduino_nicla_sense_env.rgb_led.RGBLED)
    * [enable\_indoor\_air\_quality\_status](#arduino_nicla_sense_env.rgb_led.RGBLED.enable_indoor_air_quality_status)
    * [set\_color](#arduino_nicla_sense_env.rgb_led.RGBLED.set_color)
    * [color](#arduino_nicla_sense_env.rgb_led.RGBLED.color)
    * [color](#arduino_nicla_sense_env.rgb_led.RGBLED.color)
    * [brightness](#arduino_nicla_sense_env.rgb_led.RGBLED.brightness)
    * [brightness](#arduino_nicla_sense_env.rgb_led.RGBLED.brightness)
    * [set\_brightness](#arduino_nicla_sense_env.rgb_led.RGBLED.set_brightness)
* [constants](#arduino_nicla_sense_env.constants)
* [outdoor\_air\_quality\_sensor](#arduino_nicla_sense_env.outdoor_air_quality_sensor)
  * [OutdoorAirQualitySensor](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor)
    * [air\_quality\_index](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.air_quality_index)
    * [air\_quality\_index\_interpreted](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.air_quality_index_interpreted)
    * [fast\_air\_quality\_index](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.fast_air_quality_index)
    * [no2](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.no2)
    * [o3](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.o3)
    * [mode](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.mode)
    * [mode](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.mode)
    * [set\_mode](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.set_mode)
    * [mode\_string](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.mode_string)
    * [enabled](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.enabled)
    * [enabled](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.enabled)
    * [set\_enabled](#arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.set_enabled)
* [temperature\_humidity\_sensor](#arduino_nicla_sense_env.temperature_humidity_sensor)
  * [TemperatureHumiditySensor](#arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor)
    * [temperature](#arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.temperature)
    * [humidity](#arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.humidity)
    * [enabled](#arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.enabled)
    * [enabled](#arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.enabled)
    * [set\_enabled](#arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.set_enabled)
* [indoor\_air\_quality\_sensor](#arduino_nicla_sense_env.indoor_air_quality_sensor)
  * [IndoorAirQualitySensor](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor)
    * [sulfur\_odor](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.sulfur_odor)
    * [odor\_intensity](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.odor_intensity)
    * [ethanol](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.ethanol)
    * [co2](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.co2)
    * [tvoc](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.tvoc)
    * [air\_quality](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.air_quality)
    * [air\_quality\_interpreted](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.air_quality_interpreted)
    * [relative\_air\_quality](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.relative_air_quality)
    * [mode](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.mode)
    * [mode](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.mode)
    * [set\_mode](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.set_mode)
    * [mode\_string](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.mode_string)
    * [enabled](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.enabled)
    * [enabled](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.enabled)
    * [set\_enabled](#arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.set_enabled)
* [nicla\_sense\_env](#arduino_nicla_sense_env.nicla_sense_env)
  * [NiclaSenseEnv](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv)
    * [persist\_settings](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.persist_settings)
    * [serial\_number](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.serial_number)
    * [product\_id](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.product_id)
    * [software\_revision](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.software_revision)
    * [temperature\_humidity\_sensor](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.temperature_humidity_sensor)
    * [indoor\_air\_quality\_sensor](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.indoor_air_quality_sensor)
    * [outdoor\_air\_quality\_sensor](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.outdoor_air_quality_sensor)
    * [rgb\_led](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.rgb_led)
    * [orange\_led](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.orange_led)
    * [reset](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.reset)
    * [deep\_sleep](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.deep_sleep)
    * [restore\_factory\_settings](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.restore_factory_settings)
    * [uart\_baud\_rate](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_baud_rate)
    * [uart\_baud\_rate](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_baud_rate)
    * [uart\_csv\_output\_enabled](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_csv_output_enabled)
    * [uart\_csv\_output\_enabled](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_csv_output_enabled)
    * [set\_uart\_csv\_output\_enabled](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_uart_csv_output_enabled)
    * [csv\_delimiter](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.csv_delimiter)
    * [csv\_delimiter](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.csv_delimiter)
    * [set\_csv\_delimiter](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_csv_delimiter)
    * [debugging\_enabled](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.debugging_enabled)
    * [debugging\_enabled](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.debugging_enabled)
    * [set\_debugging\_enabled](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_debugging_enabled)
    * [device\_address](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.device_address)
    * [set\_device\_address](#arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_device_address)

<a id="arduino_nicla_sense_env.orange_led.OrangeLED"></a>

## class `OrangeLED`

```python
class OrangeLED(I2CDevice)
```

This class allows to control the orange LED on the Nicla Sense Env board.

<a id="arduino_nicla_sense_env.orange_led.OrangeLED.brightness"></a>

### `brightness`

```python
@property
def brightness() -> int
```

Gets the brightness of the orange LED.

**Returns**:

- `int` - The brightness of the orange LED. Range is 0 to 255.

<a id="arduino_nicla_sense_env.orange_led.OrangeLED.brightness"></a>

### `brightness`

```python
@brightness.setter
def brightness(led_brightness) -> None
```

Sets the brightness of the orange LED.
Use `set_brightness` with `persist` set to True to make the change persistent.

**Arguments**:

- `led_brightness` _int_ - The brightness of the orange LED. Range is 0 to 63.

<a id="arduino_nicla_sense_env.orange_led.OrangeLED.set_brightness"></a>

### `set_brightness`

```python
def set_brightness(led_brightness: int, persist: bool = False) -> bool
```

Sets the brightness of the orange LED and persists the setting to flash memory.

**Arguments**:

- `led_brightness` _int_ - The brightness of the orange LED. Range is 0 to 255.
- `persist` _bool_ - Whether to persist the setting to flash memory.
  When set to True, the value of `error_status_enabled` will also be persisted.

<a id="arduino_nicla_sense_env.orange_led.OrangeLED.error_status_enabled"></a>

### `error_status_enabled`

```python
@property
def error_status_enabled() -> bool
```

Determines whether the orange LED is used to indicate an error status of one of the sensors.
When a board error condition occurs the LED blinks, independently of the brightness setting.

<a id="arduino_nicla_sense_env.orange_led.OrangeLED.error_status_enabled"></a>

### `error_status_enabled`

```python
@error_status_enabled.setter
def error_status_enabled(enabled: bool) -> None
```

Enables or disables the orange LED to indicate an error status of one of the sensors.
Use `set_error_status_enabled` with `persist` set to True to make the change persistent.

**Arguments**:

- `enabled` _bool_ - Whether to enable or disable the orange LED error status.

<a id="arduino_nicla_sense_env.orange_led.OrangeLED.set_error_status_enabled"></a>

### `set_error_status_enabled`

```python
def set_error_status_enabled(enabled: bool, persist: bool = False) -> bool
```

Enables or disables the orange LED to indicate an error status of one of the sensors and persists the setting to flash memory.

**Arguments**:

- `enabled` _bool_ - Whether to enable or disable the orange LED error status.
- `persist` _bool_ - Whether to persist the setting to flash memory.
  When set to True, the value of `brightness` will also be persisted.

<a id="arduino_nicla_sense_env.i2c_device.I2CHelper"></a>

## class `I2CHelper`

```python
class I2CHelper()
```

A helper class for interacting with I2C devices on supported boards.

<a id="arduino_nicla_sense_env.i2c_device.I2CHelper.get_interface"></a>

### `get_interface`

```python
@staticmethod
def get_interface() -> I2C
```

Returns an instance of the I2C interface for the current board.

**Raises**:

- `RuntimeError` - If the current board is not supported.
  

**Returns**:

- `I2C` - An instance of the I2C interface.

<a id="arduino_nicla_sense_env.i2c_device.I2CDevice"></a>

## class `I2CDevice`

```python
class I2CDevice()
```

Represents an I2C device connected to a bus.

**Attributes**:

- `DEFAULT_DEVICE_ADDRESS` _int_ - The default I2C address of the device.
- `bus` _I2C_ - The I2C bus to use.
- `device_address` _int_ - The I2C address of the device.
  connected (bool):Checks if the device is connected to the I2C bus.

<a id="arduino_nicla_sense_env.i2c_device.I2CDevice.__init__"></a>

### `__init__`

```python
def __init__(bus: I2C | None = None,
             device_address: int | None = DEFAULT_DEVICE_ADDRESS)
```

A initializes the NiclaSenseEnv device.

**Arguments**:

- `bus` _I2C, optional_ - The I2C bus to use. If None, the default bus will be used.
- `device_address` _int, optional_ - The I2C address of the device. Defaults to 0x21.

<a id="arduino_nicla_sense_env.i2c_device.I2CDevice.device_address"></a>

### `device_address`

```python
@property
def device_address() -> int | None
```

Gets the I2C address of the device.

**Returns**:

- `int` - The current I2C address.

<a id="arduino_nicla_sense_env.i2c_device.I2CDevice.connected"></a>

### `connected`

```python
@property
def connected()
```

Checks if the device is connected to the I2C bus.

**Returns**:

- `bool` - True if the device is connected, False otherwise.

<a id="arduino_nicla_sense_env.rgb_led.RGBLED"></a>

## class `RGBLED`

```python
class RGBLED(I2CDevice)
```

This class allows to control the RGB LED on the Nicla Sense Env board.

<a id="arduino_nicla_sense_env.rgb_led.RGBLED.enable_indoor_air_quality_status"></a>

### `enable_indoor_air_quality_status`

```python
def enable_indoor_air_quality_status(brightness: int | None = None,
                                     persist: bool = False) -> bool
```

Makes the RGB LED show the indoor air quality. (Green = Good, Yellow = Medium, Red = Bad)
To do so it sets all RGB LED colors to 0 and sets the brightness to the specified value.

**Arguments**:

- `brightness` _int, optional_ - The brightness of the RGB LED.
  If None, the current brightness will be used.
- `persist` _bool, optional_ - Whether to persist the setting to flash memory.
  When persist is True, the brightness will also be persisted.
  

**Returns**:

- `bool` - True if the operation was successful, False otherwise.

<a id="arduino_nicla_sense_env.rgb_led.RGBLED.set_color"></a>

### `set_color`

```python
def set_color(color: tuple[int, int, int, int | None],
              persist: bool = False) -> bool
```

Sets the RGB LED to the specified color.
Note: A value of 0, 0, 0 will set the color based on the IAQ value from the Indoor Air Quality sensor.

**Arguments**:

- `color` _tuple[int, int, int]_ - The RGB color components red, green, blue and brightness.
  The range for each value is 0 to 255.
- `brightness` _int, optional_ - The brightness of the RGB LED. Range is 0 to 255.
  If None, the current brightness will be used.
- `persist` _bool, optional_ - Whether to persist the setting to flash memory.
  When persist is True, the brightness will also be persisted.

<a id="arduino_nicla_sense_env.rgb_led.RGBLED.color"></a>

### `color`

```python
@property
def color() -> tuple[int, int, int]
```

Gets the RGB LED color.

**Returns**:

  tuple[int, int, int]: The RGB LED color. (red, green, blue)

<a id="arduino_nicla_sense_env.rgb_led.RGBLED.color"></a>

### `color`

```python
@color.setter
def color(color: tuple[int, int, int, int | None]) -> None
```

Sets the RGB LED color.
Use `set_color` with `persist` set to True to make the change persistent.

**Arguments**:

- `colors` _tuple[int, int, int, int]_ - The RGB color components red, green, blue and brightness.

<a id="arduino_nicla_sense_env.rgb_led.RGBLED.brightness"></a>

### `brightness`

```python
@property
def brightness() -> int
```

Gets the brightness of the RGB LED.

**Returns**:

- `int` - The brightness of the RGB LED. Range is 0 to 255.

<a id="arduino_nicla_sense_env.rgb_led.RGBLED.brightness"></a>

### `brightness`

```python
@brightness.setter
def brightness(brightness: int) -> None
```

Sets the brightness of the RGB LED.
Use `set_brightness` with `persist` set to True to make the change persistent.

**Arguments**:

- `brightness` _int_ - The brightness of the RGB LED. Range is 0 to 255.

<a id="arduino_nicla_sense_env.rgb_led.RGBLED.set_brightness"></a>

### `set_brightness`

```python
def set_brightness(brightness: int, persist: bool = False) -> bool
```

Sets the brightness of the RGB LED.

**Arguments**:

- `brightness` _int_ - The brightness of the RGB LED. Range is 0 to 255.
- `persist` _bool, optional_ - Whether to persist the setting to flash memory.
  When persist is True, the color will also be persisted.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor"></a>

## class `OutdoorAirQualitySensor`

```python
class OutdoorAirQualitySensor(I2CDevice)
```

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.air_quality_index"></a>

### `air_quality_index`

```python
@property
def air_quality_index() -> int
```

Gets the outdoor EPA air quality index from the ZMOD4510 sensor.
The" EPA AQI" is strictly following the EPA standard and is based on
the 1-hour or 8-hour average of the O3 concentrations (concentration dependent).

**Returns**:

- `int` - The outdoor air quality index. Range is 0 to 500.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.air_quality_index_interpreted"></a>

### `air_quality_index_interpreted`

```python
@property
def air_quality_index_interpreted() -> str
```

Gets the outdoor air quality index from the ZMOD4510 sensor and interprets it in terms of air quality.

**Returns**:

- `str` - The outdoor air quality index.
  Possible values are: Good, Moderate, Unhealthy for Sensitive Groups, Unhealthy, Very Unhealthy, Hazardous.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.fast_air_quality_index"></a>

### `fast_air_quality_index`

```python
@property
def fast_air_quality_index() -> int
```

Gets the fast outdoor air quality index from the ZMOD4510 sensor.
As the standard averaging leads to a very slow response, especially during testing and evaluation,
"Fast AQI" provides quicker results with a 1-minute averaging.

**Returns**:

- `int` - The fast outdoor air quality index. Range is 0 to 500.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.no2"></a>

### `no2`

```python
@property
def no2() -> float
```

Gets the NO2 concentration from the ZMOD4510 sensor.

**Returns**:

- `float` - The NO2 concentration in ppb.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.o3"></a>

### `o3`

```python
@property
def o3() -> float
```

Gets the O3 concentration from the ZMOD4510 sensor.

**Returns**:

- `float` - The O3 concentration in ppb.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.mode"></a>

### `mode`

```python
@property
def mode() -> int
```

Gets the outdoor air quality sensor (ZMOD4510) mode.
The default mode is POWER_DOWN. This is because the sensor needs several hours to start
outputting valuable data due to the sensor's internal algorithm and chemical compound.

**Returns**:

- `int` - The outdoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, OUTDOOR_AIR_QUALITY.
  This property represents the numeric value of the mode. See OutdoorAirQualitySensorMode for more information.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.mode"></a>

### `mode`

```python
@mode.setter
def mode(sensor_mode: int)
```

Sets the outdoor air quality sensor (ZMOD4510) mode.
Use `set_mode` with `persist` set to True to make the change persistent.

Note on cleaning mode:
The cleaning mode performs a thermal cleaning cycle of the MOx element. It can eliminate some light pollution
residues from production and packaging and improves the stabilization processes in the sensor.
The function heats up the sensor to allow thermal desorption and catalytic combustion of the residues.
The cleaning cycle can be executed only once in the sensor lifetime and shall be started after product assembly.
Please ensure cleaning was completed before power-off/reset and do not interrupt while cleaning.
The cleaning procedure takes 1 minute (blocking).

**Arguments**:

- `sensor_mode` _int_ - The outdoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, OUTDOOR_AIR_QUALITY.
  These values are contained in OutdoorAirQualitySensorMode.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.set_mode"></a>

### `set_mode`

```python
def set_mode(sensor_mode: int, persist=False) -> bool
```

Sets the outdoor air quality sensor mode and persists the setting to flash memory.

**Arguments**:

- `sensor_mode` _int_ - The outdoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, OUTDOOR_AIR_QUALITY.
  These values are contained in OutdoorAirQualitySensorMode.
- `persist` _bool_ - Whether to persist the setting to flash memory.
  When persist is True, the mode setting of IndoorAirQualitySensor and TemperatureHumiditySensor will also be persisted.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.mode_string"></a>

### `mode_string`

```python
@property
def mode_string() -> str | None
```

Gets the outdoor air quality sensor mode as a string.

**Returns**:

- `str` - The outdoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, OUTDOOR_AIR_QUALITY.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.enabled"></a>

### `enabled`

```python
@property
def enabled() -> bool
```

Gets the outdoor air quality sensor (ZMOD4410) enabled status.

**Returns**:

- `bool` - True if the outdoor air quality sensor mode is POWER_DOWN, False otherwise.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.enabled"></a>

### `enabled`

```python
@enabled.setter
def enabled(is_enabled: bool)
```

Enables or disables the outdoor air quality sensor.
Use `set_enabled` with `persist` set to True to make the change persistent.
When disabled the sensor goes in power down mode.
When the sensor is enabled after being disabled, the sensor will go back to the OUTDOOR_AIR_QUALITY mode.

**Arguments**:

- `is_enabled` _bool_ - Whether to enable or disable the outdoor air quality sensor.

<a id="arduino_nicla_sense_env.outdoor_air_quality_sensor.OutdoorAirQualitySensor.set_enabled"></a>

### `set_enabled`

```python
def set_enabled(is_enabled: bool, persist=False) -> bool
```

Enables or disables the outdoor air quality sensor and persists the setting to flash memory.
When disabled the sensor goes in power down mode.
When the sensor is enabled after being disabled, the sensor will go back to the default mode.

**Arguments**:

- `is_enabled` _bool_ - Whether to enable or disable the outdoor air quality sensor.
- `persist` _bool_ - Whether to persist the setting to flash memory.
  When persist is True, the mode setting of IndoorAirQualitySensor and TemperatureHumiditySensor will also be persisted.

<a id="arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor"></a>

## class `TemperatureHumiditySensor`

```python
class TemperatureHumiditySensor(I2CDevice)
```

Represents a HS4001 temperature and humidity sensor connected to an I2C bus.
This class provides properties to read the temperature and humidity from the sensor.

<a id="arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.temperature"></a>

### `temperature`

```python
@property
def temperature() -> float | None
```

Gets the temperature in degrees Celsius from the HS4001 sensor.

**Returns**:

- `float` - The temperature in degrees Celsius.

<a id="arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.humidity"></a>

### `humidity`

```python
@property
def humidity() -> float
```

Gets the humidity from the HS4001 sensor.

**Returns**:

- `float` - The humidity in %RH.

<a id="arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.enabled"></a>

### `enabled`

```python
@property
def enabled() -> bool
```

Gets the temperature sensor enabled status.

**Returns**:

- `bool` - True if the temperature sensor is enabled, False otherwise.

<a id="arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.enabled"></a>

### `enabled`

```python
@enabled.setter
def enabled(is_enabled: bool)
```

Enables or disables the temperature sensor.
Use `set_enabled` with `persist` set to True to make the change persistent.

**Arguments**:

- `is_enabled` _bool_ - Whether to enable or disable the temperature sensor.

<a id="arduino_nicla_sense_env.temperature_humidity_sensor.TemperatureHumiditySensor.set_enabled"></a>

### `set_enabled`

```python
def set_enabled(is_enabled: bool, persist=False) -> bool
```

Enables or disables the temperature sensor and persists the setting to flash memory.

**Arguments**:

- `is_enabled` _bool_ - Whether to enable or disable the temperature sensor.
- `persist` _bool_ - Whether to persist the setting to flash memory.
  When persist is True, the mode setting of IndoorAirQualitySensor and OutdoorAirQualitySensor will also be persisted.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor"></a>

## class `IndoorAirQualitySensor`

```python
class IndoorAirQualitySensor(I2CDevice)
```

Class for interacting with the indoor air quality sensor.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.sulfur_odor"></a>

### `sulfur_odor`

```python
@property
def sulfur_odor() -> bool
```

Gets the sulfur odor status from the ZMOD4410 sensor.

**Returns**:

- `bool` - True if the sulfur odor is detected, False otherwise.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.odor_intensity"></a>

### `odor_intensity`

```python
@property
def odor_intensity() -> float
```

Gets the odor intensity from the ZMOD4410 sensor.

**Returns**:

- `float` - The odor intensity.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.ethanol"></a>

### `ethanol`

```python
@property
def ethanol() -> float
```

Gets the ethanol concentration from the ZMOD4410 sensor.

**Returns**:

- `float` - The ethanol concentration in ppm.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.co2"></a>

### `co2`

```python
@property
def co2() -> float
```

Gets the CO2 concentration from the ZMOD4410 sensor.

**Returns**:

- `float` - The CO2 concentration in ppm.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.tvoc"></a>

### `tvoc`

```python
@property
def tvoc() -> float
```

Gets the TVOC concentration from the ZMOD4410 sensor.

**Returns**:

- `float` - The TVOC concentration in mg/m3.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.air_quality"></a>

### `air_quality`

```python
@property
def air_quality() -> float
```

Gets the indoor air quality from the ZMOD4410 sensor.

**Returns**:

- `float` - The indoor air quality. Range is 0 to 5 where 0 is the best air quality and 5 is the worst.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.air_quality_interpreted"></a>

### `air_quality_interpreted`

```python
@property
def air_quality_interpreted() -> str
```

Gets the indoor air quality from the ZMOD4410 sensor and interprets it in terms of air quality.

**Returns**:

- `str` - The indoor air quality. Possible values are: Very Good, Good, Medium, Poor, Bad.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.relative_air_quality"></a>

### `relative_air_quality`

```python
@property
def relative_air_quality() -> float
```

Gets the relative indoor air quality from the ZMOD4410 sensor.

**Returns**:

- `float` - The relative indoor air quality. Range is 0 to 100.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.mode"></a>

### `mode`

```python
@property
def mode() -> int
```

Gets the indoor air quality sensor mode.

**Returns**:

- `int` - The indoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.
  This property represents the numeric value of the mode. See IndoorAirQualitySensorMode for more information.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.mode"></a>

### `mode`

```python
@mode.setter
def mode(sensor_mode: int)
```

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

**Arguments**:

- `sensor_mode` _int_ - The indoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.
  These values are contained in IndoorAirQualitySensorMode.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.set_mode"></a>

### `set_mode`

```python
def set_mode(sensor_mode: int, persist=False) -> bool
```

Sets the indoor air quality sensor mode and persists the setting to flash memory.

**Arguments**:

- `sensor_mode` _int_ - The indoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.
  These values are contained in IndoorAirQualitySensorMode.
- `persist` _bool_ - Whether to persist the setting to flash memory.
  When persist is True, the mode setting of OutdoorAirQualitySensor and TemperatureHumiditySensor will also be persisted.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.mode_string"></a>

### `mode_string`

```python
@property
def mode_string() -> str | None
```

Gets the indoor air quality sensor mode as a string.

**Returns**:

- `str` - The indoor air quality sensor mode.
  Possible values are: POWER_DOWN, CLEANING, INDOOR_AIR_QUALITY, INDOOR_AIR_QUALITY_LOW_POWER, SULFUR.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.enabled"></a>

### `enabled`

```python
@property
def enabled() -> bool
```

Gets the indoor air quality sensor enabled status.

**Returns**:

- `bool` - True if the indoor air quality sensor mode is POWER_DOWN, False otherwise.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.enabled"></a>

### `enabled`

```python
@enabled.setter
def enabled(is_enabled: bool)
```

Enables or disables the indoor air quality sensor.
Use `set_enabled` with `persist` set to True to make the change persistent.
When the sensor is enabled after being disabled, the sensor will go back to the default mode.

**Arguments**:

- `is_enabled` _bool_ - Whether to enable or disable the indoor air quality sensor.

<a id="arduino_nicla_sense_env.indoor_air_quality_sensor.IndoorAirQualitySensor.set_enabled"></a>

### `set_enabled`

```python
def set_enabled(is_enabled: bool, persist=False) -> bool
```

Enables or disables the indoor air quality sensor and persists the setting to flash memory.

**Arguments**:

- `is_enabled` _bool_ - Whether to enable or disable the indoor air quality sensor.
- `persist` _bool_ - Whether to persist the setting to flash memory.
  When persist is True, the mode setting of OutdoorAirQualitySensor and TemperatureHumiditySensor will also be persisted.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv"></a>

## class `NiclaSenseEnv`

```python
class NiclaSenseEnv(I2CDevice)
```

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.persist_settings"></a>

### `persist_settings`

```python
def persist_settings()
```

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

**Returns**:

- `bool` - True if the write was successful, False otherwise.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.serial_number"></a>

### `serial_number`

```python
@property
def serial_number()
```

Gets the serial number of the device.

**Returns**:

- `str` - The serial number as a string.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.product_id"></a>

### `product_id`

```python
@property
def product_id()
```

Gets the product ID of the device.

**Returns**:

- `int` - The numeric product ID.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.software_revision"></a>

### `software_revision`

```python
@property
def software_revision()
```

Gets the software revision of the device.

**Returns**:

- `int` - The numeric software revision.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.temperature_humidity_sensor"></a>

### `temperature_humidity_sensor`

```python
@property
def temperature_humidity_sensor()
```

Gets the temperature and humidity sensor control interface.

**Returns**:

- `TemperatureHumiditySensor` - The temperature and humidity sensor.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.indoor_air_quality_sensor"></a>

### `indoor_air_quality_sensor`

```python
@property
def indoor_air_quality_sensor()
```

Gets the indoor air quality sensor control interface.

**Returns**:

- `IndoorAirQualitySensor` - The indoor air quality sensor.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.outdoor_air_quality_sensor"></a>

### `outdoor_air_quality_sensor`

```python
@property
def outdoor_air_quality_sensor()
```

Gets the outdoor air quality sensor control interface.

**Returns**:

- `OutdoorAirQualitySensor` - The outdoor air quality sensor.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.rgb_led"></a>

### `rgb_led`

```python
@property
def rgb_led()
```

Gets the RGB LED control interface.

**Returns**:

- `RGBLED` - The RGB LED.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.orange_led"></a>

### `orange_led`

```python
@property
def orange_led()
```

Gets the orange LED control interface.

**Returns**:

- `OrangeLED` - The orange LED.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.reset"></a>

### `reset`

```python
def reset()
```

Performs a reset of the module and sensors.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.deep_sleep"></a>

### `deep_sleep`

```python
def deep_sleep()
```

Puts the board in deep sleep. The board can only be woken up by a hardware reset.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.restore_factory_settings"></a>

### `restore_factory_settings`

```python
def restore_factory_settings()
```

Restores the factory settings. This will reset among other properties the device address to the default value.
See persist_settings() for a complete list of properties that are affected by this method.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_baud_rate"></a>

### `uart_baud_rate`

```python
@property
def uart_baud_rate()
```

Get the current baud rate of the UART communication.
The supported values are: 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200

Returns
---
    int: the current baud rate

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_baud_rate"></a>

### `uart_baud_rate`

```python
@uart_baud_rate.setter
def uart_baud_rate(baud_rate)
```

Set the baud rate of the UART interface.
Use `set_uart_baud_rate` with `persist` set to True to make the change persistent.

**Arguments**:

- `baud_rate` _int_ - the new baud rate.
  The supported values are: 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200
  

**Raises**:

- `ValueError` - if the baud rate is invalid

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_csv_output_enabled"></a>

### `uart_csv_output_enabled`

```python
@property
def uart_csv_output_enabled()
```

Determines if CSV output over UART is enabled.

**Returns**:

- `bool` - Whether CSV output over UART is enabled.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.uart_csv_output_enabled"></a>

### `uart_csv_output_enabled`

```python
@uart_csv_output_enabled.setter
def uart_csv_output_enabled(enabled)
```

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


**Arguments**:

- `enabled` _bool_ - Whether to enable or disable CSV output over UART.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_uart_csv_output_enabled"></a>

### `set_uart_csv_output_enabled`

```python
def set_uart_csv_output_enabled(enabled, persist=False) -> bool
```

Enables or disables CSV output over UART.

**Arguments**:

- `enabled` _bool_ - Whether to enable or disable CSV output over UART.
- `persist` _bool_ - Whether to persist the change to flash memory.
  When set to True, it will also persist the value of `debugging_enabled`.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.csv_delimiter"></a>

### `csv_delimiter`

```python
@property
def csv_delimiter()
```

Gets the delimiter character for CSV output.

**Returns**:

- `str` - The delimiter character. A single printable ASCII character.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.csv_delimiter"></a>

### `csv_delimiter`

```python
@csv_delimiter.setter
def csv_delimiter(delimiter)
```

Sets the delimiter character for CSV output.
Use `set_csv_delimiter` with `persist` set to True to make the change persistent.

**Arguments**:

- `delimiter` _str_ - The new delimiter character. Must be a single printable ASCII character.
  The following characters are not allowed: ,
  , \, ", '

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_csv_delimiter"></a>

### `set_csv_delimiter`

```python
def set_csv_delimiter(delimiter, persist=False) -> bool
```

Sets the delimiter character for CSV output.

**Arguments**:

- `delimiter` _str_ - The new delimiter character. Must be a single printable ASCII character.
  The following characters are not allowed: ,
  , \, ", '
- `persist` _bool_ - Whether to persist the change to flash memory.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.debugging_enabled"></a>

### `debugging_enabled`

```python
@property
def debugging_enabled()
```

Determines if debugging mode is enabled.
When debugging mode is enabled, the board will send additional debug messages over UART.

**Returns**:

- `bool` - Whether debugging mode is enabled.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.debugging_enabled"></a>

### `debugging_enabled`

```python
@debugging_enabled.setter
def debugging_enabled(enabled)
```

Enables or disables debugging mode.
When debugging mode is enabled, the board will send additional debug messages over UART.
Use `set_debugging_enabled` with `persist` set to True to make the change persistent.

**Arguments**:

- `enabled` _bool_ - Whether to enable or disable debugging mode.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_debugging_enabled"></a>

### `set_debugging_enabled`

```python
def set_debugging_enabled(enabled, persist=False) -> bool
```

Enables or disables debugging mode.

**Arguments**:

- `enabled` _bool_ - Whether to enable or disable debugging mode.
- `persist` _bool_ - Whether to persist the change to flash memory.
  When set to True, it will also persist the value of `uart_csv_output_enabled`.

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.device_address"></a>

### `device_address`

```python
@I2CDevice.device_address.setter
def device_address(address)
```

Sets the I2C address of the device.
Use `set_device_address` with `persist` set to True to make the change persistent.

**Arguments**:

- `address` _int_ - The new I2C address. Valid values are 0 to 127.
  

**Raises**:

- `ValueError` - if the address is invalid

<a id="arduino_nicla_sense_env.nicla_sense_env.NiclaSenseEnv.set_device_address"></a>

### `set_device_address`

```python
def set_device_address(address, persist=False) -> bool
```

Sets the I2C address of the device.

**Arguments**:

- `address` _int_ - The new I2C address. Valid values are 0 to 127.
- `persist` _bool_ - Whether to persist the change to flash memory.

