from cycling_safety_sensors.oak_camera import CameraWithSensor
from cycling_safety_sensors.serial_sensors import LaserSen0524DFRobot

sensor = LaserSen0524DFRobot("/dev/ttyAMA0")
camera_with_sensor = CameraWithSensor(
    sensor,
    xml_path="./yolo/yolov6t_coco_416x416.xml",
    bin_path="./yolo/yolov6t_coco_416x416.bin",
)

if __name__ == "__main__":
    camera_with_sensor.start()
