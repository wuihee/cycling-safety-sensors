# Cycling Safety Sensors

The goal of this module is to create a standardized API for the Cycling Safety project so that sensor data can be easily retreived.

The first time I wrote this code, I thought I was being smart by writing "clean code" and reducing redundancies. However, two months later I needed to implement the code for another sensor and I lost my mind trying to integrate it into the tightly-coupled mess that I created. I abstracted way too hard and tried to be too smart. Therefore, I am refactoring the code for the distance sensors into an indpendent module that hopefully allows me to easily integrate new sensors in the future.

## TODO

- Add commands for laser bb2x sensor.

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
