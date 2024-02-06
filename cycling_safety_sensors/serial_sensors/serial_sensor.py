from abc import abstractmethod

import serial

from ..sensor import Sensor


class SerialSensor(Sensor):
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

    def read_protocol(self) -> list[int]:
        """
        Attempt to read the protocol from the serial port.

        Returns:
            list[int]: List of bytes consisting of a standard protocol.
        """
        return [int(b, 16) for b in self.ser.read(self.protocol_length)]

    def read_distance_value(self, start: int, end: int, byteorder: str) -> int:
        """
        Reads distance value from protocol.

        Args:
            start (int): Starting byte position.
            end (int): End byte position.
            byteorder (str): "big" or "little" for big-endian and little-endian
                             respectively.

        Returns:
            int: Distance measured.
        """
        protocol = self.read_protocol()
        if not self.is_valid_protocol(protocol):
            return -1

        distance_bytes = protocol[start : end + 1]
        return int.from_bytes(distance_bytes, byteorder=byteorder)

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
        pass
