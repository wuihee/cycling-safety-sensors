from .serial_sensor import SerialSensor

PORT = "/dev/ttyS0"
BAUDRATE = 9600
PROTOCOL_LENGTH = 4


class UltrasonicA02YYUWDFRobot(SerialSensor):
    """
    A02YYUWDF ultrasonic sensor by DFRobot.
    """

    def __init__(self) -> None:
        """
        Initialize the A02YYUWDF sensor.
        """
        super().__init__(PORT, BAUDRATE, PROTOCOL_LENGTH)

    def get_distance(self) -> int:
        pass
