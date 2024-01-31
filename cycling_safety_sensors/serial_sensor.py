from abc import abstractclassmethod
from typing import Callable

import serial

from .sensor_base import Sensor


class SerialSensor(Sensor):
    """
    Base class for serial sensors.
    """

    def __init__(
        self, port: int, baudrate: int, read_distance: Callable
    ) -> None:
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.ser.reset_input_buffer()
        self.read_distance = read_distance

    def get_distance(self) -> int:
        """
        Retreive the current distance measured by the sensor.

        Returns:
            int: Distance measured in cm.
        """
        return self.read_distance()
