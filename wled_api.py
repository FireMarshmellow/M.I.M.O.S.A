import requests
import time

ip_list = ['<Wled IP 1>', '<Wled IP 2>'] # Add your WLED IP addres/s here.

def send_request(target_ip, start_num, stop_num, color):
    url = f"http://{target_ip}/json/state" # construct URL using the target IP address
    state = {"seg": [{"id": 0, "start": start_num, "stop": stop_num, "col": [color]}]}
    response = requests.post(url, json=state)

def lights(position, pi):
    start_num = int(position) - 1

    send_request(ip_list[pi], start_num, int(position), [255, 255, 255]) # Convert color value to [0, 0, 0, 255] to only use white part of LED (RGBW LEDs only).

    time.sleep(5) # Change how long the LED stays on for.

    send_request(ip_list[pi], 0, 60, [0, 255, 0])
