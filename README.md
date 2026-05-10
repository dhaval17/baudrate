# Baudrate Detector

Python script to determine the baudrate of a serial device automatically or manually.

## Overview

`baudratepy3.py` is a utility that helps identify the correct baud rate for serial communication devices. It can automatically detect the baud rate by analyzing incoming data from a serial port, or allow manual testing of different baud rates.

## Features

- **Automatic Detection**: Intelligently detects baud rate by analyzing character patterns (whitespace, punctuation, vowels)
- **Manual Mode**: Manually cycle through supported baud rates using keyboard controls
- **Character Analysis**: Uses linguistic heuristics to validate correct baud rate detection
- **Minicom Integration**: Automatically generates and saves Minicom configuration files
- **Cross-Platform**: Supports both Unix/Linux and Windows systems

## Supported Baud Rates

- 9600
- 19200
- 38400
- 57600
- 115200

## Usage

### Basic Usage

```bash
python3 baudratepy3.py -p /dev/ttyUSB0 -a
```

### Command-Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-p <serial port>` | Specify the serial port to use | `/dev/ttyUSB0` |
| `-t <seconds>` | Timeout period for switching baudrates in auto-detect mode | `5` |
| `-c <num>` | Minimum ASCII character threshold for auto-detect mode | `25` |
| `-n <name>` | Save resulting configuration as `<name>` and auto-start minicom | `None` |
| `-a` | Enable auto-detect mode | Disabled |
| `-b` | Display supported baud rates and exit | - |
| `-q` | Suppress data output from serial port | - |
| `-h` | Display help message | - |

## Examples

### Auto-detect baud rate on /dev/ttyUSB0
```bash
python3 baudratepy3.py -p /dev/ttyUSB0 -a
```

### Manual mode (use keyboard to cycle through baud rates)
```bash
python3 baudratepy3.py -p /dev/ttyUSB0
```

### Auto-detect with custom timeout and threshold
```bash
python3 baudratepy3.py -p /dev/ttyUSB0 -a -t 10 -c 30
```

### Auto-detect and save Minicom configuration
```bash
python3 baudratepy3.py -p /dev/ttyUSB0 -a -n mydevice
```

### View supported baud rates
```bash
python3 baudratepy3.py -b
```

### Quiet mode (no data output)
```bash
python3 baudratepy3.py -p /dev/ttyUSB0 -a -q
```

## How It Works

### Auto-Detect Mode (`-a`)
1. Opens the serial port and begins reading data at each baud rate
2. Analyzes incoming characters for:
   - Whitespace characters (spaces, tabs, newlines)
   - Punctuation marks (., ,, :, ;, ?, !)
   - Vowels (a-z, A-Z)
3. If the character count exceeds the threshold AND contains all three categories, the baud rate is considered correct
4. If no valid characters are detected within the timeout period, automatically tries the next baud rate
5. Detection completes when a valid baud rate is found

### Manual Mode
1. Opens the serial port at the default baud rate
2. Press **U/u/↑** to cycle up through baud rates
3. Press **D/d/↓** to cycle down through baud rates
4. Press **Ctrl+C** to quit

## Interactive Features

- **Keyboard Navigation**: 
  - `U`, `u`, `↑`: Next baud rate (up)
  - `D`, `d`, `↓`: Previous baud rate (down)
  - `Ctrl+C`: Quit

## Requirements

- Python 3.x
- `pyserial` library

Install dependencies:
```bash
pip install pyserial
```

## Author

Craig Heffner
http://www.devttys0.com
