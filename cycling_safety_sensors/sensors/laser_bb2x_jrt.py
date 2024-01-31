class LaserBB2XJRT:
    def __init__(self):
        pass

    def get_distance(self, protocol):
        distance_bytes = protocol[6:9]
        hex_string = "".join(hex(byte)[2:].zfill(2) for byte in distance_bytes)
        return int(hex_string, base=16)
