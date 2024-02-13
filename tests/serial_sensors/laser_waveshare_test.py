import serial

from cycling_safety_sensors.serial_sensors.laser_waveshare import (
    LaserWaveshare,
)

from ..serial_mock import BaseSerialMock


class LaserWaveshareSerialMock(BaseSerialMock):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.set_protocol("57 00 ff 00 9e 8f 00 00 ad 08 00 00 03 00 ff 3a")


def test_get_distance(monkeypatch):
    monkeypatch.setattr(serial, "Serial", LaserWaveshareSerialMock)
    sensor = LaserWaveshare("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 2221
