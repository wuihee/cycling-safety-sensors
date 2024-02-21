import serial

from cycling_safety_sensors.serial_sensors import UltrasonicA02YYUWDFRobot

from ..serial_mock import SerialMock

SerialMock.protocol = "FF 07 A1 A7"


def test_get_distance(monkeypatch):
    monkeypatch.setattr(serial, "Serial", SerialMock)
    sensor = UltrasonicA02YYUWDFRobot("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 1953
    assert distance == 1953
