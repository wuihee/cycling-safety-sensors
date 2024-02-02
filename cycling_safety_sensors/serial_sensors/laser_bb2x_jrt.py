from ..sensor_base import SerialSensorBase


class LaserBB2XJRT(SerialSensorBase):
    def __init__(self, port: int, baudrate: int, protocol_length: int) -> None:
        super().__init__(port, baudrate, protocol_length)

    def get_distance(self, protocol: list[int]) -> int:
        """
        Return the current distance measured by the Laser BB2x JRT.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.

        Returns:
            int: The distance measured in cm.
        """
        distance_bytes = protocol[6:9]
        hex_string = "".join(hex(byte)[2:].zfill(2) for byte in distance_bytes)
        return int(hex_string, base=16)

    def is_valid_protocol(self, protocol: list[int]) -> bool:
        """
        Check if a protocol is valid.

        Args:
            protocol (list[int]): Current protocol consisting of a list of
                                  bytes read from the serial port.

        Returns:
            bool: True if protocol is valid, otherwise false.
        """
        # TODO: Store value 170 in a constant variable.
        if not protocol or protocol[0] != 170:
            return False

        return sum(protocol[1:-1] % 256 == protocol[-1])
