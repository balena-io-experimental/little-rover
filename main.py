from flask import Flask, request
import time
import explorerhat
app = Flask(__name__)


@app.route('/')
def display_ui():
    return '''
        <html>
            <head>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
                <style>
                    td {
                        text-align: center;
                        font-size: 48pt;
                    }
                </style>
            </head>
            <body>
                <table>
                    <tr>
                        <td>&nbsp;</td>
                        <td><a onclick="$.get('/api/', { motorleft:100, motorright:100 });">^^</a></td>
                        <td>&nbsp;</td>
                    </tr>
                    <tr>
                        <td>&nbsp;</td>
                        <td><a onclick="$.get('/api/', { motorleft:100, motorright:100, reset:100 });">^</a></td>
                        <td>&nbsp;</td>
                    </tr>
                    <tr>
                        <td><a onclick="$.get('/api/', { motorleft:-100, motorright:100, reset:30 });">&lt;</a></td>
                        <td><a onclick="$.get('/api/', { motorleft:0, motorright:0, reset:100 });">x</a></td>
                        <td><a onclick="$.get('/api/', { motorleft:100, motorright:-100, reset:30 });">&gt;</a></td>
                    </tr>
                    <tr>
                        <td>&nbsp;</td>
                        <td>
                            <a onclick="$.get('/api/', { motorleft:-100, motorright:-100, reset:100 });">v</a>
                        </td>
                        <td>&nbsp;</td>
                    </tr>
                </table>
                <p>
                    My UI isn't pretty, but my repo is on <a href="https://github.com/resin-io-playground/little-rover" target="_blank">GitHub</a>, and I (and all my siblings) are managed really easily thanks to <a href="http://resin.io" target="_blank">resin.io</a>
                    <ul>
                        <li>Update an entire fleet via one git push</li>
                        <li>View a bundle of really useful info from one page</li>
                        <li>Logs and SSH across a VPN out of the box</li>
                    </ul>
                </p>
            </body>
        </html>
    '''

@app.route('/api/')
def set_motors():
    explorerhat.motor.one.speed(int(request.args.get('motorleft')))
    explorerhat.motor.two.speed(int(request.args.get('motorright')))
    if bool(request.args.get('reset')):
        time.sleep(float(request.args.get('reset'))/100)
        explorerhat.motor.one.speed(0)
        explorerhat.motor.two.speed(0)
    return 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
