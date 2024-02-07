from .serial_sensor import SerialSensor

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
        super().__init__(port, BAUDRATE, PROTOCOL_LENGTH, PROTOCOL_HEADER)

    def get_distance(self) -> int:
        """
        Retrieves the distance measured by the SEN0524 laser sensor.

        Returns:
            int: Distance measured in mm.
        """
        return super().get_distance(8, 11, "little")

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Return if protocol is valid for the SEN0524 laser sensor.

        Args:
            protocol (list[int]): Protocol consisting of a list of bytes read
                `                 from the serial port.

        Returns:
            bool: Returns true if protocol is valid, else False.
        """
        return super().is_valid_protocol(protocol)
