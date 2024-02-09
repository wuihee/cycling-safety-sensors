from dataclasses import dataclass

import serial

from ..sensor import Sensor


@dataclass
class SerialSensorSettings:
    baudrate: int
    protocol_length: int
    protocol_header: tuple[int]
    distance_indices: tuple[int]
    checksum_start_index: int = 0
    byte_order: str = "big"


class SerialSensor(Sensor):
    """
    Base class for sensors.
    """

    def __init__(self, port: str, settings: SerialSensorSettings) -> None:
        """
        Initialize SerialSensorBase.

        Args:
            port (str): Port which sensor uses.
            baudrate (int): Baudrate of sensor.
            protocol_settings (ProtocolSettings):
        """
        self.settings = settings
        self.ser = serial.Serial(port, self.settings.baudrate, timeout=1)
        self.ser.reset_input_buffer()

    def read_protocol(self) -> list[int]:
        """
        Attempt to read the protocol from the serial port.

        Returns:
            list[int]: List of bytes consisting of a standard protocol.
        """
        return list(self.ser.read(self.settings.protocol_length))

    def get_distance(self) -> int:
        """
        Reads distance value from protocol.

        Returns:
            int: Distance measured.
        """
        protocol = self.read_protocol()
        if not self.is_valid_protocol(protocol):
            return -1

        start, end = self.settings.distance_indices
        return int.from_bytes(
            protocol[start:end], byteorder=self.settings.byte_order
        )

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Check if given protocol is valid.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.
            start_byte (int): Position of starting byte to sum for checksum.

        Returns:
            bool: Returns true if valid, otherwise false.
        """
        if not protocol:
            return False

        current_header = tuple(protocol[: self.settings.protocol_length])
        if current_header != self.settings.protocol_header:
            return False

        checksum = sum(protocol[self.settings.checksum_start_index : -1])
        return checksum % 256 == protocol[-1]
