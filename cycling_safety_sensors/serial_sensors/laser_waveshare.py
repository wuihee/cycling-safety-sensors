from .serial_sensor import SerialSensor

PORT = "/dev/ttys0"
BAUDRATE = 921600
PROTOCOL_LENGTH = 16
PROTOCOL_HEADER = 87, 0, 255


class LaserWaveshare(SerialSensor):
    """
    Laser time of flight sensor by WaveShare.
    """

    def __init__(self) -> None:
        """
        Initialize LaserWaveshare sensor.
        """
        super().__init__(PORT, BAUDRATE, PROTOCOL_LENGTH)

    def get_distance(self) -> int:
        """
        Retrieve the current distance measured by the laser sensor.

        Returns:
            int: Distance in cm, otherwise -1 if unable to measure.
        """
        return self.read_distance_value(8, 10, "little")

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Determine if protocol is valid for the Laser Wavershare sensor.

        Args:
            protocol (list[int]): Protocol consisting of a list of bytes.

        Returns:
            bool: True if protocol is valid, false otherwise.
        """
        if not protocol or protocol[:3] != PROTOCOL_HEADER:
            return False

        return sum(protocol[:-1]) % 256 == protocol[-1]
