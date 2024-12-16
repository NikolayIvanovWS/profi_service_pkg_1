#!/usr/bin/env python3

import random
import time
from tqdm import tqdm
import os
import platform
import psutil

configuration_number = "109x4tg"
version = "1.0.0"

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

def get_raspberry_pi_info():
    try:
        with open("/proc/device-tree/model", "r") as model_file:
            model = model_file.read().strip()
    except FileNotFoundError:
        model = "Unknown Model (not a Raspberry Pi?)"

    os_info = platform.platform()

    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp_file:
            cpu_temp = float(temp_file.read().strip()) / 1000.0 
    except FileNotFoundError:
        cpu_temp = None

    memory = psutil.virtual_memory()
    total_memory = memory.total / 1024**2  
    used_memory = memory.used / 1024**2

    print(f"--- Raspberry Pi Info ---")
    print(f"Model: {model}")
    print(f"OS: {os_info}")
    if cpu_temp is not None:
        print(f"CPU Temperature: {cpu_temp:.2f}°C")
    else:
        print("CPU Temperature: Not available")
    print(f"Memory: {used_memory:.2f}MB used / {total_memory:.2f}MB total")
    print("--------------------------")

def finalize():
    print("Service package 1: successfully configured!")
    print("Service package 1: configuration checksum: {}".format(configuration_number))

if __name__ == "__main__":
    simulate_calculations()
    simulate_progress_bar()
    perform_network_check()
    get_raspberry_pi_info()
    finalize()
