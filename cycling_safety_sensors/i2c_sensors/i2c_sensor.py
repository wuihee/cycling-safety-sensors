import smbus2

from ..sensor import Sensor


class I2CSensor(Sensor):
    """
    Base class for I2C sensors.
    """

    def __init__(self, bus_number: int, address: int) -> None:
        """
        Initialize the I2C sensor interface.

        Args:
            bus_number (int): I2C bus number.
            address (int): I2C address of sensor.
        """
        self.bus = smbus2.SMBus(bus_number)
        self.address = address
