from flask import Flask, jsonify, request
import time
import threading
import subprocess

def execute_script(once, interval):
    while True:
        if once:
            subprocess.run(["python", "main.py"])
            break
        else:
            subprocess.run(["python", "main.py"])
            time.sleep(interval)

def route(app):
    @app.route('/run', methods=['GET'])
    def get_last_time():
        ret = {}
        with open('./logs/runtime/log.txt', 'r') as file:
            lines = file.readlines()
            ret['timestamp'] = float(lines[-1] if lines else 1704000000)
        return jsonify(ret)
    
    ### POST run, body(once:bool, intervel:number)
    # if once is true, then run main script once
    # else set the intervel of script 
    @app.route('/run', methods=['POST'])
    def run_script():
        try:
            data = request.json
            once = data.get('once')
            interval = data.get('interval')

            script_thread = threading.Thread(target=execute_script, args=(once, interval))
            script_thread.start()

            return jsonify({"message": "Script execution started successfully"})
    
        except Exception as e:
            return jsonify({"error": str(e)})