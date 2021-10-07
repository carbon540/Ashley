# settings.py

# Iterates through settings to feed to feed to transmit and receive
# spreading_factor, signal_bandwidth, coding_rate, enable_crc

class settings(self):
    def __init__(self) -> None:
        super().__init__()
        # Spreading factor controls
        spreading_factor = (6, 7, 8, 9, 10, 11, 12)

        # Signal bandwidth describes
        bw_bins = (7800, 10400, 15600, 20800, 31250, 41700, 62500, 125000, 250000)
        
        # Coding rate
        coding_rate = (5, 6, 7, 8)

        # Enable crc ....
        enable_crc = (True, False)
    
    def count():
        count = len(1)
        return count

    def read(ordinal):
        return ordinal