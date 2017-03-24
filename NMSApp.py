from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def hello_world():
    routers = ['152.96.9.201', '152.96.9.202', '152.96.9.203']
    return render_template('index.html', routers=routers)


@app.route('/interface_status/<router>')
def status(router):
    # TODO get status of all interfaces
    interfaces = {'items':
        [
            {
                "kind": "object#interface",
                "type": "ethernet",
                "if-name": "gigabitEthernet1",
                "description": "management interface",
                "ip-address": "129.10.10.10",
                "subnet-mask": "255.255.254.0"
            }
        ]
    }

    return render_template('status.html', router=router, interfaces=interfaces)


@app.route('/show_config/<router>')
def show_config(router):
    # TODO get running config of device
    config = ['hostname router.ins.hsr.ch',
              'interface GigabitEthernet1',
              '  ip address 10.1.1.1 255.0.0.0']
    return render_template('show_config.html', router=router, config=config)


if __name__ == '__main__':
    app.run()
