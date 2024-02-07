from .serial_sensor import SerialSensor

BAUDRATE = 921600
PROTOCOL_LENGTH = 16
PROTOCOL_HEADER = [87, 0, 255]


class LaserWaveshare(SerialSensor):
    """
    Laser time of flight sensor by WaveShare.
    """

    def __init__(self, port: str) -> None:
        """
        Initialize LaserWaveshare sensor.

        Args:
            port (str): Port which the sensor uses.
        """
        super().__init__(port, BAUDRATE, PROTOCOL_LENGTH, PROTOCOL_HEADER)

    def get_distance(self) -> int:
        """
        Retrieve the current distance measured by the laser sensor.

        Returns:
            int: Distance in cm, otherwise -1 if unable to measure.
        """
        return super().get_distance(8, 11, "little")
