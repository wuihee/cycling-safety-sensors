class SerialMock:
    def __init__(self, port: str, baudrate: int, timeout=1) -> None:
        self.protocol = "57 00 ff 00 9e 8f 00 00 ad 08 00 00 03 00 ff 3a"

    def reset_input_buffer(self) -> None:
        pass

    def read(self, bytes: int) -> list[int]:
        return [int(b, 16) for b in self.protocol.split()]
