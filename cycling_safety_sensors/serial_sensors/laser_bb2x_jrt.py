from ..utils import find_serial_port
from .serial_sensor import SerialSensor

PORT = find_serial_port()
BAUDRATE = 115200
PROTOCOL_LENGTH = 13
VALID_CHECKSUM_BYTE = 130


class LaserBB2XJRT(SerialSensor):
    """
    BB2X time of flight laser distance module by JRT Chengdu.
    """

    def __init__(self) -> None:
        """
        Initialize the LaserBB2XJRT sensor.
        """
        super().__init__(PORT, BAUDRATE, PROTOCOL_LENGTH)

    def get_distance(self) -> int:
        """
        Return the current distance measured by the Laser BB2x JRT.

        Returns:
            int: The distance measured in cm, or -1 if unable to measure.
        """

        protocol = self.read_protocol()
        if self.is_valid_protocol(protocol):
            distance_bytes = protocol[6:9]
            hex_string = "".join(
                hex(byte)[2:].zfill(2) for byte in distance_bytes
            )
            return int(hex_string, base=16)

        return -1

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Check if a protocol is valid.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.

        Returns:
            bool: True if protocol is valid, otherwise false.
        """
        if not protocol or protocol[0] != VALID_CHECKSUM_BYTE:
            return False

        return sum(protocol[1:-1] % 256 == protocol[-1])
