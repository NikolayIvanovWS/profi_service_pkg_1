#!/usr/bin/env python3

import random
import time

configuration_number = "*Sn253N"
version = "0.0.2"

def simulate_calculations():
    print("Service package 1: version {}".format(version))
    print("Service package 1: starting configuration...")
    time.sleep(0.5)

    for i in range(0, 100, 10):
        print("Progress: {}%".format(i), flush=True)
        time.sleep(0.3)

    print("Service package 1: configuration complete!")
    print("Service package 1: configuration checksum: {}".format(configuration_number))

def generate_random_data():
    print("Generating important data...")
    for _ in range(3):
        print("".join(chr(random.randint(33, 126)) for _ in range(30)), flush=True)
        time.sleep(0.2)

if __name__ == "__main__":
    simulate_calculations()
    generate_random_data()

