from abc import ABC, abstractclassmethod


class Sensor(ABC):
    """
    Base class for sensors.
    """

    @abstractclassmethod
    def get_distance(self) -> int:
        """
        Retreive the current distance measured by the sensor.

        Returns:
            int: The distance in cm.
        """
        pass
