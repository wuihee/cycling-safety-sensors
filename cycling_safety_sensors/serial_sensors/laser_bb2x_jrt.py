from ..utils import find_serial_port
from .serial_sensor import SerialSensor

PORT = find_serial_port()
BAUDRATE = 115200
PROTOCOL_LENGTH = 13
PROTOCOL_HEADER = [130]
GET_DISTANCE_COMMAND = b"\xaa\x00\x00\x20\x00\x01\x00\x02\x23"


class LaserBB2XJRT(SerialSensor):
    """
    BB2X time of flight laser distance module by JRT Chengdu.
    """

    def __init__(self) -> None:
        """
        Initialize the LaserBB2XJRT sensor.
        """
        super().__init__(PORT, BAUDRATE, PROTOCOL_LENGTH, PROTOCOL_HEADER)

    def get_distance(self) -> int:
        """
        Return the current distance measured by the Laser BB2x JRT.

        Returns:
            int: The distance measured in cm, or -1 if unable to measure.
        """
        self.ser.write(GET_DISTANCE_COMMAND)
        return super().get_distance(6, 10)

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Check if a protocol is valid.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.

        Returns:
            bool: True if protocol is valid, otherwise false.
        """
        return super().is_valid_protocol(protocol, 1)
