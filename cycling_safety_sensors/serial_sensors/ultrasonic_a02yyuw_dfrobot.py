from .serial_sensor import SerialSensor

PORT = "/dev/ttyS0"
BAUDRATE = 9600
PROTOCOL_LENGTH = 4


class UltrasonicA02YYUWDFRobot(SerialSensor):
    """
    A02YYUW ultrasonic sensor by DFRobot.
    """

    def __init__(self) -> None:
        """
        Initialize the A02YYUWDF sensor.
        """
        super().__init__(PORT, BAUDRATE, PROTOCOL_LENGTH)

    def get_distance(self) -> int:
        """
        Return the distance measured by the A02YYUW sensor.

        Returns:
            int: Distance measured in mm.
        """
        return self.read_distance_value(1, 2, "big")

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Determine if protocol is valid for A02YYUW sensor.

        Args:
            protocol (list[int]): Protocol consisting of list of bytes.

        Returns:
            bool: True if protocol is valid, else False.
        """
        if not protocol:
            return False

        return sum(protocol[:3]) & 0x00FF == protocol[3]
