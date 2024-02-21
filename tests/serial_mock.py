class SerialMock:
    """
    Mock serial.Serial() object.
    """

    protocol = ""

    def __init__(self, *args, **kwargs) -> None:
        pass

    def reset_input_buffer(self) -> None:
        pass

    def read(self, num_bytes: int) -> bytes:
        return [int(b, 16) for b in SerialMock.protocol.split()]
