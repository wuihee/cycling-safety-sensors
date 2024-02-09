from .serial_sensor import SerialSensor, SerialSensorSettings

BAUDRATE = 9600
PROTOCOL_LENGTH = 4
PROTOCOL_HEADER = tuple()
DISTANCE_INDICES = 1, 3


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
        settings = SerialSensorSettings(
            BAUDRATE,
            PROTOCOL_LENGTH,
            PROTOCOL_HEADER,
            DISTANCE_INDICES,
        )
        super().__init__(port, settings)
