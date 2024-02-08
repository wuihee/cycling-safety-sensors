from dataclasses import dataclass

import serial

from ..sensor import Sensor


@dataclass
class ProtocolSettings:
    """
    ProtocolSetup defines a few parameters for the protocol of each sensor.
    """

    length: int
    header: list[int]
    byte_order: str = "big"


class SerialSensor(Sensor):
    """
    Base class for sensors.
    """

    def __init__(
        self, port: str, baudrate: int, protocol_settings: ProtocolSettings
    ) -> None:
        """
        Initialize SerialSensorBase.

        Args:
            port (str): Port which sensor uses.
            baudrate (int): Baudrate of sensor.
            protocol_settings (ProtocolSettings):
        """
        self.settings = protocol_settings
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.ser.reset_input_buffer()

    def read_protocol(self) -> list[int]:
        """
        Attempt to read the protocol from the serial port.

        Returns:
            list[int]: List of bytes consisting of a standard protocol.
        """
        return [int(b, 16) for b in self.ser.read(self.settings.length)]

    def get_distance(self, start: int, end: int) -> int:
        """
        Reads distance value from protocol.

        Args:
            start (int): Starting byte position.
            end (int): End byte position.

        Returns:
            int: Distance measured.
        """
        protocol = self.read_protocol()
        if not self.is_valid_protocol(protocol):
            return -1

        distance_bytes = protocol[start:end]
        return int.from_bytes(
            distance_bytes, byteorder=self.settings.byte_order
        )

    def is_valid_protocol(self, protocol: list[int], start_byte=0) -> bool:
        """
        Check if given protocol is valid.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.
            start_byte (int): Position of starting byte to sum for checksum.

        Returns:
            bool: Returns true if valid, otherwise false.
        """
        if (
            not protocol
            or not protocol[: len(self.settings.length)]
            == self.settings.header
        ):
            return False

        return sum(protocol[start_byte:-1]) % 256 == protocol[-1]
