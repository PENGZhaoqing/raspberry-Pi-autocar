# -*- coding: utf-8 -*
from flask import Flask, render_template, request, abort
from car import Car
from config import WEB_PORT

app = Flask(__name__)

car = Car()

handle_map = {
    'forward': car.forward,
    'left': car.left,
    'right': car.right,
    'backward': car.backward,
    'backward': car.backward,
    'leftspin': car.leftspin,
    'rightspin': car.rightspin,
}

@app.route('/', methods=['GET'])
def main_page():
    return render_template("index.html")


@app.route('/handle', methods=['GET'])
def handle():
    try:
        # 获取GET参数
        operation = request.args.get('type', '')
    except ValueError:
        abort(404)  # 返回 404
    else:
        if operation in handle_map.iterkeys():
            handle_map[operation](50)
        elif operation == 'pause':
            car.stop()
        elif operation == 'reset':
            car.shutdown()
        else:
            abort(404)
    return 'ok'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=WEB_PORT, debug=False)
