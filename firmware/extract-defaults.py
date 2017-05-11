#!/usr/bin/env python3

import struct

base = 0x18000
firmwares = [open("mcu%d.bin" % i, "rb").read() for i in range(3)]

params = [
    [ struct.unpack("<h", firmwares[mcu][base+num*2:base+(num+1)*2])[0]
      for mcu in range(3) ]
    for num in range(128)
]

print(params)

# Sample output from version 1.15
# [[-1, -1, -1], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [500, 500, 500], [500, 500, 500], [1, 1, 1], [90, 90, 90], [1, 1, 1], [600, 600, 600], [100, 100, 100], [1000, 1000, 1000], [30000, 30000, 30000], [30000, 30000, 30000], [1650, 1650, 1650], [1650, 1650, 1650], [63, 63, 63], [1, 1, 1], [500, 500, 500], [500, 500, 500], [18000, 18000, 8000], [200, 200, 50], [0, 0, 0], [0, 0, 0], [9, 9, 9], [10, 10, 10], [0, 1, 2], [1000, 1000, 1000], [1024, 1024, 1024], [4096, 4096, 4096], [1, 1, 1], [7, 7, 7], [16384, 16384, 16384], [0, 0, 0], [200, 200, 200], [20, 20, 20], [20000, 20000, 20000], [0, 0, 0], [30, 30, 30], [0, 0, 0], [0, 0, 0], [100, 100, 100], [0, 0, 0], [0, 0, 0], [4000, 4000, 4000], [0, 0, 0], [20, 20, 20], [2500, 2500, 2500], [1, 1, 1], [10, 10, 10], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1000, 1000, 1000], [3, 3, 3], [10, 10, 10], [0, 0, 0], [1024, 1024, 1024], [1024, 1024, 1024], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [22000, 22000, 22000], [50, 50, 50], [2000, 2000, 2000], [5000, 5000, 5000], [200, 200, 200], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [1000, 1000, 1000], [1000, 1000, 1000], [1000, 1000, 1000], [437, 437, 437], [0, 0, 0], [0, 0, 0], [900, 900, 900], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [115, 115, 115]]
