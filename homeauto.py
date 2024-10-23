from flask import Flask, render_template, request
import RPi.GPIO as GPIO

# GPIO Setup
LED_PIN = 17  # Pin to control LED (previous setup)
RELAY_PIN = 27  # Pin to control relay (connected to IN1 of the relay module)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<state>')
def led_control(state):
    if state == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED is ON"
    elif state == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED is OFF"
    else:
        return "Invalid command"

@app.route('/relay/<state>')
def relay_control(state):
    if state == "on":
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Activates relay (turns bulb ON)
        return "Bulb is ON"
    elif state == "off":
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Deactivates relay (turns bulb OFF)
        return "Bulb is OFF"
    else:
        return "Invalid command"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)