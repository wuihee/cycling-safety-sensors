# Cycling Safety Sensors

The goal of this module is to create a standardized API for the Cycling Safety project so that sensor data can be easily retreived.

## TODO

- [ ] Include BB2X Unit Tests
- [ ] Add code for I2C sensors and LiDAR Lite v4.

## Installation

### Pip

```bash
pip install git+https://github.com/wuihee/cycling-safety-sensors.git
```

### Poetry

```bash
poetry add git+https://github.com/wuihee/cycling-safety-sensors.git
```

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
  - [Laser by Waveshare](https://www.waveshare.com/wiki/TOF_Laser_Range_Sensor)
  - Laser BB2X by Chengdu JRT
  - Laser SEN0524 by DFRobot
  - Ultrasonic A02YYUW by DFRobot
- I2C Sensors
  - LiDAR Lite v4 by Garmin
