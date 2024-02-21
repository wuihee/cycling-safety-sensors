from cycling_safety_sensors.serial_sensors import LaserBB2XJRT


def test_get_distance(serial_mock):
    serial_mock("AA 00 00 22 00 03 00 00 0B 5A 02 A4 30")
    sensor = LaserBB2XJRT("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 58
