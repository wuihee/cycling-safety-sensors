from .serial_sensor import SerialSensor, SerialSensorSettings

BAUDRATE = 921600
PROTOCOL_LENGTH = 16
PROTOCOL_HEADER = 87, 0, 255
DISTANCE_INDICES = 8, 11
BYTE_ORDER = "little"


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
        settings = SerialSensorSettings(
            BAUDRATE,
            PROTOCOL_LENGTH,
            PROTOCOL_HEADER,
            DISTANCE_INDICES,
            byte_order=BYTE_ORDER,
        )
        super().__init__(port, settings)
