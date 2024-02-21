import pytest
import serial


@pytest.fixture
def serial_mock(monkeypatch):
    def _mock(protocol_data):
        class SerialMock:
            """
            Mock serial.Serial() object.
            """

            def __init__(self, *args, **kwargs) -> None:
                self.protocol_data = protocol_data

            def reset_input_buffer(self) -> None:
                pass

            def write(self, bytes_to_write: bytes) -> None:
                pass

            def read(self, num_bytes: int) -> bytes:
                return [int(b, 16) for b in self.protocol_data.split()]

        monkeypatch.setattr(serial, "Serial", SerialMock)

    return _mock
