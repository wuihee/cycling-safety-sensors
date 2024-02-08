from .serial_sensor import ProtocolSettings, SerialSensor

BAUDRATE = 115200
PROTOCOL_LENGTH = 16
PROTOCOL_HEADER = [0x57]


class LaserSen0524DFRbobot(SerialSensor):
    """
    Time of Flight laser sensor 0524 by DFRobot.
    """

    def __init__(self, port: str) -> None:
        """
        Initialize the SEN0524 laser sensor.

        Args:
            port (str): Port which the sensor uses.
        """
        settings = ProtocolSettings(PROTOCOL_LENGTH, PROTOCOL_HEADER, "little")
        super().__init__(port, BAUDRATE, settings)

    def get_distance(self) -> int:
        """
        Retrieves the distance measured by the SEN0524 laser sensor.

        Returns:
            int: Distance measured in mm.
        """
        return super().get_distance(8, 11)
