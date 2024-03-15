from .serial_sensor import SerialSensor, SerialSensorSettings

BAUDRATE = 115200
PROTOCOL_LENGTH = 16
PROTOCOL_HEADER = (87,)
DISTANCE_INDICES = 8, 11
BYTE_ORDER = "little"


class LaserSen0524DFRobot(SerialSensor):
    """
    Time of Flight laser sensor 0524 by DFRobot.
    """

    def __init__(self, port: str) -> None:
        """
        Initialize the SEN0524 laser sensor.

        Args:
            port (str): Port which the sensor uses.
        """
        settings = SerialSensorSettings(
            BAUDRATE,
            PROTOCOL_LENGTH,
            PROTOCOL_HEADER,
            DISTANCE_INDICES,
            byte_order=BYTE_ORDER,
        )
        super().__init__(port, settings)
