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
        return self.ser.read(self.protocol_length)

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
