import pytest

from cycling_safety_sensors.serial_sensors.laser_waveshare import (
    LaserWaveshare,
)

from ..serial_mock import mock_serial


def test_get_distance(mock_serial):
    mock_serial.set_protocol("57 00 ff 00 9e 8f 00 00 ad 08 00 00 03 00 ff 3a")
    sensor = LaserWaveshare("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 2221
    distance = sensor.get_distance()
    assert distance == 2221
