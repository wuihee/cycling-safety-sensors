import serial

from cycling_safety_sensors.serial_sensors.laser_waveshare import (
    LaserWaveshare,
)

from ..serial_mock import SerialMock


def test_get_distance(monkeypatch):
    monkeypatch.setattr(serial, "Serial", SerialMock)
    sensor = LaserWaveshare("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 2221
