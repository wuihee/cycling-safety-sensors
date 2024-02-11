import pytest

from cycling_safety_sensors.serial_sensors.laser_waveshare import (
    LaserWaveshare,
)


@pytest.fixture
def mock_serial(monkeypatch):
    mock = pytest.MagicMock()
    monkeypatch.setattr("serial.Serial", mock)
    return mock


def test_get_distance(mock_serial):
    mock_serial.return_value.read.return_value = ""
    sensor = LaserWaveshare("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 16
