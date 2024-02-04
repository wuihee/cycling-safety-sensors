from .serial_sensor import SerialSensor

PORT = "/dev/ttys0"
BAUDRATE = 921600
PROTOCOL_LENGTH = 16


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
        protocol = self.read_protocol()
        if not self.is_valid_protocol(protocol):
            return -1
