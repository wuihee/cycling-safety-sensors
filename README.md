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
  - [Laser SEN0524 by DFRobot](https://wiki.dfrobot.com/_A02YYUW_Waterproof_Ultrasonic_Sensor_SKU_SEN0311)
  - [Ultrasonic A02YYUW by DFRobot](https://wiki.dfrobot.com/SKU_SEN0524_ToF_Outdoor_Laser_Ranging_Module_15m#target_4)
- I2C Sensors
  - [LiDAR Lite v4 by Garmin](https://support.garmin.com/en-US/?partNumber=010-02022-00&tab=manuals)
