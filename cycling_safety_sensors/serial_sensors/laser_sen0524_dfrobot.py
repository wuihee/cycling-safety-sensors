from .serial_sensor import SerialSensor

PORT = "/dev/ttyAMA0"
BAUDRATE = 115200
PROTOCOL_LENGTH = 16


class LaserSen0524DFRbobot(SerialSensor):
    """
    Time of Flight laser sensor 0524 by DFRobot.
    """

    def __init__(self) -> None:
        super().__init__(PORT, BAUDRATE, PROTOCOL_LENGTH)

    def get_distance(self) -> int:
        return self.read_distance_value(8, 10, "little")

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        pass
