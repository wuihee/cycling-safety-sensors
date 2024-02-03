from serial.tools import list_ports


def find_serial_port() -> str:
    """
    Find the serial port the current sensor.

    Returns:
        str: The serial port found.
    """
    ports = list(list_ports.comports())
    for port in ports:
        if "CH340" in port.description or "USB Serial" in port.description:
            return port.device
