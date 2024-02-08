from .serial_sensor import ProtocolSettings, SerialSensor

BAUDRATE = 9600
PROTOCOL_LENGTH = 4
PROTOCOL_HEADER = []


class UltrasonicA02YYUWDFRobot(SerialSensor):
    """
    A02YYUW ultrasonic sensor by DFRobot.
    """

    def __init__(self, port: str) -> None:
        """
        Initialize the A02YYUWDF sensor.

        Args:
            port (str): Port which the sensor uses.
        """
        settings = ProtocolSettings(PROTOCOL_LENGTH, PROTOCOL_HEADER)
        super().__init__(port, BAUDRATE, settings)

    def get_distance(self) -> int:
        """
        Return the distance measured by the A02YYUW sensor.

        Returns:
            int: Distance measured in mm.
        """
        return super().get_distance(1, 3)
