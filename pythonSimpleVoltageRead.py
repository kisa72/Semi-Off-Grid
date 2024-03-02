from time import sleep
import requests

converter = 0.01425

url = 'http://192.168.0.182/voltage/'

while True:
    server = requests.post(url)
    output = float(server.text)

    voltage = output * converter
    print("Voltage: {0}".format(voltage))

    sleep(60)
