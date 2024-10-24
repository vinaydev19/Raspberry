https://github.com/timwaizenegger/raspberrypi-examples/blob/master/actor-led-7segment-4numbers/actor-led-7segment-4numbers.zip












# Raspberry Pi Practical Exercises

This repository contains practical exercises using Raspberry Pi to interface various hardware components and perform different tasks. Each practical involves connecting specific hardware, setting up the necessary libraries, and executing Python scripts. Below are the details of each practical and the steps required to complete them.

---

## Practical 02: Displaying Time on 4-Digit 7-Segment Display

### Aim:
To display the current time on a 4-digit 7-segment display using Raspberry Pi.

### Hardware Required:
- Raspberry Pi
- 4-Digit 7-Segment Module
- Connecting Wires

### Connections:
| Seven Segment Module Pin | Raspberry Pi Pin  |
|--------------------------|-------------------|
| Clk                      | 40           |
| DIO                      | 38           |
| Vcc                      | 2      |
| Ground                   | 6       |

### Steps:
1. Download the required libraries by visiting this [GitHub repository](https://github.com/timwaizenegger/raspberrypi-examples/tree/master/actor-led-7segment-4numbers).
2. Download and unzip the `actor-led-7segment-4numbers.zip` file.
3. Open the Thonny Python IDE on Raspberry Pi and navigate to the folder containing the code.
4. Write and save the provided code in the `actor-led-7segment-4numbers` folder.
5. Run the code to display the time on the 7-segment display.

---

## Practical 03: Interfacing 16x2 LCD with Raspberry Pi

### Aim:
To interface a 16x2 LCD display with Raspberry Pi and show different messages.

### Hardware Required:
- Raspberry Pi
- 16x2 LCD Module
- 10K Potentiometer
- Connecting Wires

### Connections:
| LCD Pin | Raspberry Pi Pin   |
|---------|--------------------|
| 1       | (Pin 6)        |
| 2       | (Pin 2)         |
| 4       | (Pin 37)   |
| 5       | (Pin 9)        |
| 6       | (Pin 35)   |
| 11      | (Pin 22)   |
| 12      | (Pin 18)   |
| 13      | (Pin 15)   |
| 14      | (Pin 13)   |
| 15      | (Pin 17)        |
| 16      | (Pin 20)       |

**Potentiometer Connections**:
| Potentiometer Pin | Raspberry Pi/LCD Pin     |
|-------------------|--------------------------|
| 1                 | 5V (Pin 4)               |
| 2                 | LCD Pin 3                |
| 3                 | GND (Pin 39)             |

### Steps:
1. Activate the virtual environment: 
   ```bash
   source myenv/bin/activate
