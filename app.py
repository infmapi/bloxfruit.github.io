from flask import Flask, render_template
import psutil
import time

app = Flask(__name__)

def is_roblox_running():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'Roblox' in proc.info['name']:
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roblox_status')
def roblox_status():
    if is_roblox_running():
        return 'Running'
    else:
        return 'Not Running'

if __name__ == '__main__':
    app.run(debug=True)
