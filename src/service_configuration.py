#!/usr/bin/env python3

import random
import time

configuration_number = "1xM18650"
version = "0.0.1"

def simulate_calculations():
    print("Service package 1: version {}".format(version))
    print("Service package 1: starting configuration...")
    time.sleep(0.5)

    for i in range(1, 101, 10):
        print("Progress: {}%".format(i), flush=True)
        time.sleep(0.3)

    print("Service package 1: configuration complete!")
    print("Service package 1: configuration checksum: {}".format(configuration_number))

if __name__ == "__main__":
    simulate_calculations()
