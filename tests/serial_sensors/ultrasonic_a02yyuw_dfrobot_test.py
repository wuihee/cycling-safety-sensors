from cycling_safety_sensors.serial_sensors import UltrasonicA02YYUWDFRobot


def test_get_distance(serial_mock):
    serial_mock("FF 07 A1 A7")
    sensor = UltrasonicA02YYUWDFRobot("/dev/ttyS0")
    distance = sensor.get_distance()
    assert distance == 1953
