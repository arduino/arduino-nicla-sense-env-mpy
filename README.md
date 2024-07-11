# 📦 Nicla Sense Env MicroPython Package

This package contains an API to read sensor data from the Nicla Sense Env board and control its behaviour. The board host three different sensors which can be read simultaneously: **ZMOD4410** (Indoor Air Quality), **ZMOD4510** (Outdoor Air Quality), **HS4001** (Temperature & Humidity).

## ✨ Features

This library supports the complete API exposed by the Nicla Sense Env sensor board over I2C.

- 🌈 RGB LED control
- ⚪️ Orange LED control
- 💤 Board control (sleep, reset, factory reset)
- 🔧 Board configuration (e.g. changing the I2C address)
- 🏠 Indoor Air Quality Sensor control
    - Change mode (Power down, cleaning, Indoor Air quality, sulfur detection)
    - Detect sulfur
    - Measure odor intensity
    - Measure ethanol level
    - Measure TVOC
    - Measure CO2
    - Measure air quality
- 🌳 Outdoor Air Quality Sensor control
    - Change mode (Power down, cleaning, Outdoor Air quality)
    - Measure NO2
    - Measure O3
    - Measure air quality
- 🌡 Temperature/Humidity Sensor Control
    - Change mode (Power down, temperature/humidity)
    - Read temperature
    - Read humidity
- 📄 UART CSV output

## 📖 Documentation
For more information on the features of this library and how to use them please read the documentation [here](./docs/).

## ✅ Supported Boards

Any board that can run a modern version of MicroPython is supported.
On non-Arduino boards you will have to specify the I2C interface to be used. e.g. `device = NiclaSenseEnv(I2C(1))`. On Arduino boards this will be detected automatically.

## ⚙️ Installation

The easiest way is to use mpremote and mip: `mpremote connect id:$device_sn mip install github:arduino/arduino-nicla-sense-env-mpy`

## 🧑‍💻 Developer Installation

The easiest way is to clone the repository and then run any example using `mpremote`.
The recommended way is to mount the root directory remotly on the board and then running an example script. e.g.

```
 mpremote connect id:387784598330 mount src run ./examples/board_control.py
```

The specified serial number passed to the `id` attribute can be retrieved using `mpremote connect list`.
The serial number is the value in the second column.

## 🐛 Reporting Issues

If you encounter any issue, please open a bug report [here](https://github.com/arduino/arduino-nicla-sense-env-mpy/issues). 

## 📕 Further Reading
- Indoor Air Quality: 
    - [A Sense of Clean Air](https://www.renesas.com/us/en/blogs/sense-clean-air)
    - [Overview of TVOC and Indoor Air Quality](https://www.renesas.com/us/en/document/whp/overview-tvoc-and-indoor-air-quality)
- Outdoor Air Quality: [Outdoor Air Quality: It’s Not Just About Urban Areas](https://www.renesas.com/us/en/blogs/outdoor-air-quality-its-not-just-about-urban-areas)
    
- Datasheets
    - [ZMOD4410 datasheet](https://www.renesas.com/us/en/document/dst/zmod4410-datasheet)
    - [ZMOD4510 datasheet](https://www.renesas.com/eu/en/document/dst/zmod4510-datasheet)
    - [HS4001 datasheet](https://www.renesas.com/us/en/document/dst/hs40xx-datasheet?r=1575071)


## 💪 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 🤙 Contact

For questions, comments, or feedback on this package, please create an issue on this repository.