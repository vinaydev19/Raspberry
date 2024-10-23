import time
import matplotlib.pyplot as plt
from drawnow import drawnow
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS
from smbus2 import SMBus
import board
import busio

# Initialize I2C bus manually
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 instance
ads = ADS.ADS1115(i2c)

# Gain setting for the ADS1115
GAIN = 1
val = []
cnt = 0
max_points = 50  # Maximum number of points to display in the plot

plt.ion()  # Enable interactive mode for Matplotlib

# Create the figure function for drawing the plot
def makeFig():
    plt.clf()  # Clear the current figure to avoid overlap
    plt.ylim(-5000, 5000)  # Set y-axis limits according to expected values
    plt.title('Oscilloscope - ADC Readings')
    plt.grid(True)
    plt.ylabel('ADC Outputs')
    plt.xlabel('Sample Number')
    plt.plot(val, 'ro-', label='Channel 0')  # Plot the values in red with markers
    plt.legend(loc='lower right')

# Start continuous ADC readings on channel 0
print('Reading ADS1115 channel 0')

try:
    while True:
        # Read the ADC value from channel 0
        chan = AnalogIn(ads, ADS.P0)  # Reading from channel 0 with the specified gain
        value = chan.value
        print(f'Channel 0: {value}')
        
        # Append the ADC value to the list for plotting
        val.append(int(value))

        # Update the plot with the new data
        drawnow(makeFig)
        plt.pause(0.1)  # Pause for a short moment to update the plot

        # Maintain a fixed number of values for display
        if len(val) > max_points:
            val.pop(0)  # Remove the oldest value from the list to keep it within the limit

        # Sleep for a short period before the next reading (adjust if necessary)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("Exiting the program...")

finally:
    plt.ioff()  # Disable interactive mode to finalize the plot
    plt.show()  # Show the final plot after exiting the loop