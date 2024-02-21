from cycling_safety_sensors.serial_sensors import LaserSen0524DFRbobot


def test_get_distance(serial_mock):
    serial_mock("57 00 ff 00 9e 8f 00 00 ad 08 00 00 03 00 ff 3a")
    sensor = LaserSen0524DFRbobot("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 2221
