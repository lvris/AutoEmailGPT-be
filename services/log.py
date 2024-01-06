from flask import Flask, jsonify, request
import os

logs_path = './logs/feedback'

def get_subfolders_titles(directory):
    subfolders_titles = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            subfolders_titles.append(str(dir))
    return subfolders_titles

def get_md_file_content(directory, subfolder):
    subfolder_path = os.path.join(directory, subfolder)
    md_files = [file for file in os.listdir(subfolder_path) if file.endswith('.md')]
    ret = {}
    if len(md_files) == 1:
        md_file_path = os.path.join(subfolder_path, md_files[0])
        with open(md_file_path, 'r', encoding='utf-8') as file:
            ret['content'] = file.read()
        ret['name'] = str(md_files[0])
    else:
        ret['content'] = "No or multiple markdown files found in the subfolder."
        ret['name'] = "Error"
    return ret

def route(app):
    @app.route('/log', methods=['GET'])
    def get_log_list():
        log_list = get_subfolders_titles(logs_path)
        return jsonify(log_list)

    @app.route('/log', methods=['POST'])
    def get_log_content():
        try:
            data = request.json
            subject = data.get('subject')
            print(subject)
            ret = get_md_file_content(logs_path, subject)
            return jsonify(ret)
    
        except Exception as e:
            return jsonify({"error": str(e)})