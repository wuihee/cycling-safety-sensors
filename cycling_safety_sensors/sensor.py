from abc import ABC, abstractmethod


class Sensor(ABC):
    """
    Sensor class defines a common interface for all sensors in the cycling
    safety project.
    """

    @abstractmethod
    def get_distance(self) -> int:
        """
        Retrieve the current distance measured by the sensor.

        Returns:
            int: The distance in cm.
        """
        pass
