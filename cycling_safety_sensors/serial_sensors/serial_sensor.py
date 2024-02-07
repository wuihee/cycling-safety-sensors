import serial

from ..sensor import Sensor


class SerialSensor(Sensor):
    """
    Base class for sensors.
    """

    def __init__(
        self,
        port: str,
        baudrate: int,
        protocol_length: int,
        protocol_header: list[int] = [],
    ) -> None:
        """
        Initialize SerialSensorBase.

        Args:
            port (str): Port which sensor uses.
            baudrate (int): Baudrate of sensor.
            protocol_length (int): The length of the sensor's protocol i.e.
                                   number of bytes.
            protocol_header (list[int], optional): Fixed protocol header.
                                                   Defaults to [].
        """
        self.protocol_length = protocol_length
        self.protocol_header = protocol_header
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.ser.reset_input_buffer()

    def read_protocol(self) -> list[int]:
        """
        Attempt to read the protocol from the serial port.

        Returns:
            list[int]: List of bytes consisting of a standard protocol.
        """
        return [int(b, 16) for b in self.ser.read(self.protocol_length)]

    def get_distance(self, start: int, end: int, byteorder="big") -> int:
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

        distance_bytes = protocol[start:end]
        return int.from_bytes(distance_bytes, byteorder=byteorder)

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
            or not protocol[: len(self.protocol_header)]
            == self.protocol_header
        ):
            return False

        return sum(protocol[start_byte:-1]) % 256 == protocol[-1]
