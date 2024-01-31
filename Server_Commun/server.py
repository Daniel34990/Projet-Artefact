from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

with open("config_ip.yaml", "r") as f:
    config_ip = yaml.load(f, Loader=yaml.FullLoader)
    robot_id = config_ip["robot_id"]
    robots_ips = config_ip["robots_ips"]
    port = config_ip["port"]

robots_status = {robot_id: 'DISCONNECTED' for robot_id in robots_ips.keys()}
current_robot_id = 0


def get_previous_robot_id(robot_id):
    if (robot_id > 0):
        return robot_id - 1
    else:
        return None


@app.route('/request', methods=['POST'])
def handle_request():
    data = request.json
    client_ip = request.remote_addr
    # Handle different request types
    if data.get('type') == 'ALIVE':
        return handle_alive_request(data, client_ip)
    elif data.get('type') == 'START_AUTHORIZATION':
        return handle_startauth_request(data, client_ip)
    elif data.get('type') == 'SUCCESS':
        return handle_success_request(data, client_ip)
    elif data.get('type') == 'LAYOUT':
        return handle_layout_request(data, client_ip)
    elif data.get('fail') == 'FAIL':
        return handle_info_request(data, client_ip)
    elif data.get('type') == 'START':
        return handle_start_request(data, client_ip)
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request type'}), 400


def handle_alive_request(data, client_ip):
    global robots_status
    print(f"Received alive request from: {client_ip} (robot {data['id']})")
    robots_status[data['id']] = 'ALIVE'
    response_data = {'status': 'success', 'info': 'Alive received'}
    return jsonify(response_data)


def handle_startauth_request(data, client_ip):
    global robots_status
    global current_robot_id
    print(f"Received start authorization request from: {client_ip} (robot {data['id']})")
    previous_id = get_previous_robot_id(data['id'])
    if previous_id is not None:
        if current_robot_id == previous_id:
            match robots_status[previous_id]:
                case 'FINISHED':
                    response_data = {'status': 'success', 'code': 'S0', 'message': 'Authorization granted'}
                case 'ALIVE':
                    response_data = {'error': 'success', 'code': 'E0', 'info': 'Waiting for previous robot to finish'}
                case 'DISCONNECTED':
                    response_data = {'status': 'success', 'code': 'S1',
                                     'message': 'Authorization granted as previous robot is disconnected'}
                    current_robot_id = data['id']
                case _:
                    response_data = {'error': 'error', 'code': 'E1', 'info': 'Unknown status : ' + robots_status[previous_id]}
            return jsonify(response_data)
    response_data = {'status': 'success', 'info': 'Some information'}
    return jsonify(response_data)


def handle_start_request(data, client_ip):
    global robots_status
    global current_robot_id
    print(f"Received start request from: {client_ip} (robot {data['id']})")
    robots_status[data['id']] = 'STARTED'
    current_robot_id = data['id']
    response_data = {'status': 'success', 'info': 'Information received'}
    return jsonify(response_data)


def handle_message_request(data, client_ip):
    # Your logic to handle message requests
    print(f"Received message: {data['content']}")
    return jsonify({'status': 'success', 'message': 'Message received successfully'})


def handle_info_request(data, client_ip):
    # Your logic to handle info requests
    print(f"Received info request from: {data['source']}")
    response_data = {'status': 'success', 'info': 'Some information'}
    return jsonify(response_data)


def handle_success_request(data, client_ip):
    global robots_status
    # Your logic to handle success requests
    print(f"Received success request from robot {data['id']}")
    robots_status[data['id']] = 'FINISHED'
    response_data = {'status': 'success', 'info': 'Some information'}
    return jsonify(response_data)

def handle_layout_request(data, client_ip):
    # Your logic to handle layout requests
    print(f"Received layout request from robot {data['id']}")
    response_data = {'status': 'success', 'info': 'Some information'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
