import json
from flask import Flask
from flask_cors import CORS
from models.switch import Switch
from modules.dummy import DummySwitch, DummyConnect


app = Flask(__name__)
CORS(app)

@app.route('/api/command/show_interfaces_status/<string:hostname>')
def command(hostname):
    device = DeviceConnect(hostname)
    return json.dumps(device.send_command('show interface status'))


@app.route('/api/gather/<string:hostname>')
def gather(hostname):
    device = Switch(hostname)
    device.update_connection()
    return json.dumps(device.__dict__).encode('utf8')


@app.route('/api/dummy/command/show_interfaces_status/<string:hostname>')
def dummy_interfaces(hostname):
    dummydevice = DummyConnect(hostname)
    return json.dumps(dummydevice.send_command('show interface status'))


@app.route('/api/dummy/gather/<string:hostname>')
def dummy_gather(hostname):
    dummydevice = DummySwitch(hostname)
    dummydevice.update_connection()
    return json.dumps(dummydevice.__dict__).encode('utf8')

#{"hostname": "se2165sw01", "domainname": "clients.skanska.se", "ip": "10.38.158.203", "fqdn": "se2165sw01.clients.skanska.se", "reachable": true}

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
