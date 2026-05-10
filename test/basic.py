#!/usr/bin/env python3
# Run basic tests

import os
import sys
import time
import argparse
import serial


def check_sudo_permission():
    """Check if the script is being run with sudo privileges."""
    if os.geteuid() != 0:
        print("Error: This script must be run with sudo privileges!")
        print("Usage: sudo python3 basic.py [--baudrate BAUDRATE] [--device DEVICE]")
        sys.exit(1)
    print("✓ Sudo permission verified")


def send_test_data(device, baudrate, interval=10, test_data="AAAA1234"):
    """
    Send test data to the serial device at regular intervals.
    
    Args:
        device (str): Serial device path (e.g., /dev/ttyUSB0)
        baudrate (int): Baudrate for serial communication
        interval (int): Interval in seconds between sends (default: 10)
        test_data (str): Test data to send (default: AAAA1234)
    """
    try:
        print(f"Opening serial device {device} at {baudrate} baud...")
        ser = serial.Serial(device, baudrate, timeout=1)
        print(f"✓ Connected to {device}")
        
        print(f"Starting to send test data every {interval} seconds...")
        print(f"Test data: {test_data}\n")
        
        try:
            while True:
                ser.write(test_data.encode() + b'\n')
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Sent: {test_data}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n✓ Test stopped by user")
        finally:
            ser.close()
            print("✓ Serial connection closed")
            
    except serial.SerialException as e:
        print(f"Error: Failed to open serial device {device}")
        print(f"Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Basic baudrate test - sends test data to serial device"
    )
    parser.add_argument(
        "--baudrate",
        type=int,
        default=9600,
        help="Baudrate for serial communication (default: 9600)"
    )
    parser.add_argument(
        "--device",
        type=str,
        default="/dev/ttyUSB1",
        help="Serial device path (default: /dev/ttyUSB1)"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=10,
        help="Interval in seconds between test data sends (default: 10)"
    )
    parser.add_argument(
        "--data",
        type=str,
        default="AAAA1234",
        help="Test data to send (default: AAAA1234)"
    )
    
    args = parser.parse_args()
    
    # Check sudo permission
    check_sudo_permission()
    
    # Validate device path format
    if not args.device.startswith("/dev/ttyUSB"):
        print(f"Warning: Device {args.device} does not match expected pattern /dev/ttyUSB*")
    
    # Send test data
    send_test_data(args.device, args.baudrate, args.interval, args.data)


if __name__ == "__main__":
    main()
