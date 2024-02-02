from abc import ABC, abstractmethod

import serial


class SerialSensorBase(ABC):
    """
    Base class for sensors.
    """

    def __init__(self, port: int, baudrate: int, protocol_length: int) -> None:
        """
        Initialize SerialSensorBase.

        Args:
            port (int): Port which sensor uses.
            baudrate (int): Baudrate of sensor.
            protocol_length (int): The length of the sensor's protocol i.e.
                                   number of bytes.
        """
        self.protocol_length = protocol_length
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.ser.reset_input_buffer()

    @abstractmethod
    def get_distance(self, protocol: list[int]) -> int:
        """
        Retreive the current distance measured by the sensor.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.

        Returns:
            int: The distance in cm.
        """

    @abstractmethod
    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Check if given protocol is valid.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.

        Returns:
            bool: Returns true if valid, otherwise false.
        """
