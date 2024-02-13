class BaseSerialMock:
    def __init__(self, port: str, baudrate: int, timeout=1) -> None:
        self._protocol = ""

    def set_protocol(self, protocol_bytes: str) -> None:
        self._protocol = protocol_bytes

    def reset_input_buffer(self) -> None:
        pass

    def read(self, num_bytes: int) -> bytes:
        return [int(b, 16) for b in self._protocol.split()]
