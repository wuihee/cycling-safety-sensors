# Cycling Safety Sensors

The goal of this module is to create a standardized API for the Cycling Safety project so that sensor data can be easily retreived.

## Usage

Each sensor can be imported from its respective module and data is read with the `get_distance()` method.

```python
from serial.serial_sensors import LaserBB2XJRT

sensor = LaserBB2XJRT("/dev/ttyS0")
distance = sensor.get_distance()
print(f"The distance measured is {distance}")
```

## Sensor Available

- Serial Sensors
  - Laser by Waveshare
  - Laser BB2X by Chengdu JRT
  - Laser SEN0524 by DFRobot
  - Ultrasonic A02YYUW by DFRobot
- I2C Sensors
  - LiDAR Lite v4 by Garmin

## Overview

- **Design**: Use a common interface to reduce redundancy and create modular code that can be easily updated for new sensors.
- **Naming Convention**: sensor technology, sensor name, manufacturer. E.g. lidar_lidarlitev4_garmin.py.

### Design Process

- I knew I wanted to try creating a common interface for the sensors. This wasn't difficult.
- Serial sensors needed:
  - Parameters: `port`, `baudrate`, `protocol_length`
  - `get_distance()` method: Retrieve current distance measured.
  - `is_protocol_valid()`: Validate current protocol.
- All serial sensors need to go through the same process to read distance measurements:
  1. Read a set number of bytes from the serial port.
  2. Extract the bytes representing the distance.
- Therefore, I used the Template Method strategy pattern to create an abstract base class `SerialSensor` which provided the template for this process. Each serial sensor would just have to inherit from `SerialSensor`, define the port, baudrate, and number of bytes to read and everything would be taken care of.
