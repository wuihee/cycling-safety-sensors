# Cycling Safety Sensors

The goal of this module is to create a standardized API for the Cycling Safety project so that sensor data can be easily retreived.

## Overview

- **Design**: Use strategy design pattern to reduce redundancy and create modular code that can be easily updated for new sensors.
- Categorize sensors by their technology - currently I only have serial and i2c sensors.
- **Naming Convention**: sensor technology, sensor name, manufacturer. E.g. lidar_lidarlitev4_garmin.py.
