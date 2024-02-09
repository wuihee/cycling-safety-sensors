from .serial_sensor import SerialSensor, SerialSensorSettings

BAUDRATE = 115200
PROTOCOL_LENGTH = 13
PROTOCOL_HEADER = (130,)
DISTANCE_INDICES = 6, 10
CHECKSUM_START_INDEX = 1
GET_DISTANCE_COMMAND = b"\xaa\x00\x00\x20\x00\x01\x00\x02\x23"


class LaserBB2XJRT(SerialSensor):
    """
    BB2X time of flight laser distance module by JRT Chengdu.
    """

    def __init__(self, port: str) -> None:
        """
        Initialize the LaserBB2XJRT sensor.

        Args:
            port (str): Port which the sensor uses.
        """
        settings = SerialSensorSettings(
            BAUDRATE,
            PROTOCOL_LENGTH,
            PROTOCOL_HEADER,
            DISTANCE_INDICES,
            CHECKSUM_START_INDEX,
        )
        super().__init__(port, settings)

    def get_distance(self) -> int:
        """
        Return the current distance measured by the Laser BB2x JRT.

        Returns:
            int: The distance measured in cm, or -1 if unable to measure.
        """
        self.ser.write(GET_DISTANCE_COMMAND)
        return super().get_distance()
