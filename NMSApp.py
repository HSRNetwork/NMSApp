import string

import napalm_base
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

driver = napalm_base.get_network_driver('ios')
username = 'ins'
password = 'ins'


@app.route('/')
def welcome():
    routers = ['152.96.9.77', '152.96.9.79', '152.96.9.90', '152.96.9.91']
    return render_template('index.html', routers=routers)


@app.route('/interface_status/<router>')
def status(router):
    device = driver(hostname=router, username=username, password=password)
    device.open()
    interfaces = device.get_interfaces()
    interfaces_ip = device.get_interfaces_ip()
    device.close()

    for name in interfaces_ip:
        try:
            interfaces[name]['ipv'] = interfaces_ip[name]['ipv4']
        except KeyError:
            interfaces[name]['ipv'] = 'no ip address'

    return render_template('status.html', router=router, interfaces=interfaces)


@app.route('/show_config/<router>')
def show_config(router):
    device = driver(hostname=router, username=username, password=password)
    device.open()
    config = device.get_config()['startup'].split(string.punctuation)
    return render_template('show_config.html', router=router, config=config)


if __name__ == '__main__':
    app.run()
