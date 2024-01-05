from flask import Flask, jsonify, request

settings_path = './.venv/settings.py'

def read_settings():
    settings = {}
    with open(settings_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if '=' in line:
                key, value = line.strip().split('=')
                settings[key.strip()] = value.strip().strip("'").strip('"')
    return settings

def update_settings(new_settings):
    with open(settings_path, 'w') as f:
        for key, value in new_settings.items():
            f.write(f"{key} = '{value}'\n")

def route(app):
    @app.route('/config', methods=['GET'])
    def get_settings():
        settings = read_settings()
        return jsonify(settings)

    @app.route('/config', methods=['POST'])
    def update_settings_file():
        try:
            new_settings = request.form
            current_settings = read_settings()

            for key, value in new_settings.items():
                if key in current_settings:
                    current_settings[key] = value

            update_settings(current_settings)
            return jsonify({"message": "Settings updated successfully"})
        except Exception as e:
            return jsonify({"error": str(e)})

