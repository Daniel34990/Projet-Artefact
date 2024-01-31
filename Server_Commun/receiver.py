import requests
import json
import time
import yaml

SERVER_IP = '137.194.173.6'
PORT = 8000
REQUEST_URL = f'http://{SERVER_IP}:{PORT}/request'

with open("config_ip.yaml", "r") as f:
    config_ip = yaml.load(f, Loader=yaml.FullLoader)
    robot_id = config_ip["robot_id"]
    robots_ips = config_ip["robots_ips"]
    port = config_ip["port"]

def send_alive_request(content):
    data = {'type': 'ALIVE', 'id': robot_id}
    response = requests.post(REQUEST_URL, json=data)
    handle_response(response)

def send_authorization_request(content):
    data = {'type': 'START_AUTHORIZATION', 'id': robot_id}
    response = requests.post(REQUEST_URL, json=data)
    handle_response(response)

def send_start_request(content):
    data = {'type': 'START', 'id': robot_id}
    response = requests.post(REQUEST_URL, json=data)
    handle_response(response)

def send_success_request(content):
    data = {'type': 'SUCCESS', 'id': robot_id}
    response = requests.post(REQUEST_URL, json=data)
    handle_response(response)

def send_layout_request(content):
    data = {'type': 'LAYOUT', 'id': robot_id}
    response = requests.post(REQUEST_URL, json=data)
    handle_response(response)

def send_fail_request(source):
    data = {'type': 'FAIL', 'id': robot_id}
    response = requests.post(REQUEST_URL, json=data)
    handle_response(response)

def handle_response(response):
    if response.status_code == 200:
        print("Request successful")
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    time.sleep(1)  # Give time for the requests to complete before exiting
    send_alive_request("Some information")
    time.sleep(1)
    send_authorization_request("Some information")
    time.sleep(1)
    send_start_request("Some information")
    time.sleep(1)
    send_success_request("Some information")
    time.sleep(1)

