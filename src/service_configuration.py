#!/usr/bin/env python3

import random
import time
from tqdm import tqdm
import os

configuration_number = "g087#RW"
version = "0.1.0"

def simulate_calculations():
    print("Service package 1: version {}".format(version))
    print("Service package 1: starting configuration...")
    time.sleep(0.5)

    for i in range(0, 100, 10):
        print("Progress: {}%".format(i), flush=True)
        time.sleep(0.3)


def simulate_progress_bar():
    print("Running system checks...")
    for _ in tqdm(range(100), desc="Checking", ascii=True):
        time.sleep(0.05)


def perform_network_check():
    print("Performing network checks...")
    os.system("ifconfig | grep -w inet")
    print("Service package 1: configuration complete!")
    print("Service package 1: configuration checksum: {}".format(configuration_number))

if __name__ == "__main__":
    simulate_calculations()
    simulate_progress_bar()
    perform_network_check()

