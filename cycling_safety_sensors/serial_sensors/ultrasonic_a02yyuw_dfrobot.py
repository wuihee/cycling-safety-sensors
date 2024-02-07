from .serial_sensor import SerialSensor

PORT = "/dev/ttyS0"
BAUDRATE = 9600
PROTOCOL_LENGTH = 4
PROTOCOL_HEADER = []


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
        return super().get_distance(1, 3)

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Determine if protocol is valid for A02YYUW sensor.

        Args:
            protocol (list[int]): Protocol consisting of list of bytes.

        Returns:
            bool: True if protocol is valid, else False.
        """
        return super().is_valid_protocol(protocol, PROTOCOL_HEADER)
