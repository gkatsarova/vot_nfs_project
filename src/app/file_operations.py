import os
from flask import jsonify, request
from flask_jwt_extended import jwt_required
from . import app

NFS_SHARE_PATH = '/mnt/nfs-share' 

@app.route('/file/upload', methods=['POST'])
@jwt_required() 
def upload_file():
    file = request.files.get('file')
    if file:
        file_path = os.path.join(NFS_SHARE_PATH, file.filename)
        file.save(file_path)
        return jsonify({"message": f"File {file.filename} uploaded successfully"}), 201
    return jsonify({"message": "No file provided"}), 400

@app.route('/file/<file_name>', methods=['GET'])
@jwt_required()
def get_file(file_name):
    file_path = os.path.join(NFS_SHARE_PATH, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            content = f.read()
        return jsonify({"file_content": content.decode('utf-8', 'ignore')}), 200
    return jsonify({"message": "File not found"}), 404

@app.route('/file/<file_name>', methods=['PUT'])
@jwt_required()
def update_file(file_name):
    file = request.files.get('file')
    if file:
        file_path = os.path.join(NFS_SHARE_PATH, file_name)
        if os.path.exists(file_path):
            file.save(file_path)
            return jsonify({"message": f"File {file_name} updated successfully"}), 200
        return jsonify({"message": "File not found"}), 404
    return jsonify({"message": "No file provided"}), 400

@app.route('/file/<file_name>', methods=['DELETE'])
@jwt_required()
def delete_file(file_name):
    file_path = os.path.join(NFS_SHARE_PATH, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": f"File {file_name} deleted successfully"}), 200
    return jsonify({"message": "File not found"}), 404
