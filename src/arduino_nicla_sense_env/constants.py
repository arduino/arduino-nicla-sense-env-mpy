
# Byte order for 2 and 4 byte registers is big-endian, lowest address is LSB, highest address is MSB.
REGISTERS = {
    "status": {"address": 0x00, "type": "uint8", "bytes": 1},  # Board Status Register
    "slave_address": {"address": 0x01, "type": "uint8", "bytes": 1},  # Board Slave Address Register (valid immediately after writing)
    "control": {"address": 0x02, "type": "uint8", "bytes": 1},  # Board Control Register
    "orange_led": {"address": 0x03, "type": "uint8", "bytes": 1},  # Orange LED Control Register
    "rgb_led_red": {"address": 0x04, "type": "uint8", "bytes": 1},  # RGB LED Control Register RED (4x uint8)
    "rgb_led_green": {"address": 0x05, "type": "uint8", "bytes": 1},  # GREEN
    "rgb_led_blue": {"address": 0x06, "type": "uint8", "bytes": 1},  # BLUE
    "rgb_led_intensity": {"address": 0x07, "type": "uint8", "bytes": 1},  # Intensity
    "uart_control": {"address": 0x08, "type": "uint8", "bytes": 1},  # Board UART Control Register
    "csv_delimiter": {"address": 0x09, "type": "uint8", "bytes": 1},  # CSV Delimiter character (ASCII)
    "sw_revision": {"address": 0x0C, "type": "uint8", "bytes": 1},  # Board SW Revision
    "product_id": {"address": 0x0D, "type": "uint8", "bytes": 1},  # Product ID (currently: 0x01)
    "serial_number": {"address": 0x0E, "type": "uint8", "bytes": 1 * 6},  # Serial Number (6x uint8, ZMOD4410 tracking number)
    "sample_counter": {"address": 0x14, "type": "uint32", "bytes": 4},  # HS4001 sample counter
    "temperature": {"address": 0x18, "type": "float", "bytes": 4},  # HS4001 Temperature (degC)
    "humidity": {"address": 0x1C, "type": "float", "bytes": 4},  # HS4001 Humidity (%RH)
    "zmod4510_status": {"address": 0x23, "type": "uint8", "bytes": 1},  # ZMOD4510 status
    "zmod4510_sample_counter": {"address": 0x24, "type": "uint32", "bytes": 4},  # ZMOD4510 sample counter
    "zmod4510_epa_aqi": {"address": 0x28, "type": "uint16", "bytes": 2},  # ZMOD4510 EPA AQI
    "zmod4510_fast_aqi": {"address": 0x2A, "type": "uint16", "bytes": 2},  # ZMOD4510 Fast AQI
    "zmod4510_o3": {"address": 0x2C, "type": "float", "bytes": 4},  # ZMOD4510 O3 (ppb)
    "zmod4510_no2": {"address": 0x30, "type": "float", "bytes": 4},  # ZMOD4510 NO2 (ppb)
    "zmod4510_rmox": {"address": 0x34, "type": "float", "bytes": 4 * 13},  # ZMOD4510 Rmox[0] ... Rmox[12] (Ohm)
    "zmod4410_status": {"address": 0x6B, "type": "uint8", "bytes": 1},  # ZMOD4410 status
    "zmod4410_sample_counter": {"address": 0x6C, "type": "uint32", "bytes": 4},  # ZMOD4410 sample counter
    "zmod4410_iaq": {"address": 0x70, "type": "float", "bytes": 4},  # ZMOD4410 IAQ
    "zmod4410_tvoc": {"address": 0x74, "type": "float", "bytes": 4},  # ZMOD4410 TVOC (mg/m3)
    "zmod4410_eco2": {"address": 0x78, "type": "float", "bytes": 4},  # ZMOD4410 eCO2 (ppm)
    "zmod4410_rel_iaq": {"address": 0x7C, "type": "float", "bytes": 4},  # ZMOD4410 Rel IAQ
    "zmod4410_etoh": {"address": 0x80, "type": "float", "bytes": 4},  # ZMOD4410 EtOH
    "zmod4410_rmox": {"address": 0x84, "type": "float", "bytes": 4 * 13},  # ZMOD4410 Rmox[0] ... Rmox[12] (Ohm)
    "zmod4410_rcda": {"address": 0xB8, "type": "float", "bytes": 4 * 3},  # ZMOD4410 Rcda[0] ... Rcda[2]
    "zmod4410_rhtr": {"address": 0xC4, "type": "float", "bytes": 4},  # ZMOD4410 Rhtr (heater resistance at room temperature)
    "zmod4410_temp": {"address": 0xC8, "type": "float", "bytes": 4},  # ZMOD4410 Temp (temperature in degC used during ambient compensation)
    "zmod4410_intensity": {"address": 0xCC, "type": "float", "bytes": 4},  # ZMOD4410 Intensity (odor intensity)
    "zmod4410_odor_class": {"address": 0xD0, "type": "uint8", "bytes": 1},  # ZMOD4410 Odor class (1 = sulfur odor, 0 = others)
}

DEVICE_I2C_INTERFACES = {
    "Arduino Portenta H7" : { "type" : "hw", "interface" : 3 },
    "Arduino Portenta C33" : { "type" : "hw", "interface" : 0 }
    # "Other board" : { "type" : "sw", "scl" : "P408", "sda" : "P407" }
}
