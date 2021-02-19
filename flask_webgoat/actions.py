from pathlib import Path
import subprocess
import uuid
from flask import request

from flask import (
    Blueprint, jsonify, request, jsonify, session
)
from werkzeug.security import check_password_hash
from flask import current_app as app

bp = Blueprint('actions', __name__)


@bp.route('/message', methods=['POST'])
def log_entry():
    auth = session.get('user_info', None)
    if auth is None:
        return jsonify({'error': 'no auth found in session'})
    access_level = auth[2]
    if access_level > 2:
        return jsonify({'error': 'access level < 2 is required for this action'})
    filename_param = request.form.get('filename')
    if filename_param is None:
        return jsonify({'error': 'filename parameter is required'})
    text_param = request.form.get('text')
    if text_param is None:
        return jsonify({'error': 'text parameter is required'})

    user_id = auth[0]
    user_dir = "data/" + str(user_id)
    user_dir_path = Path(user_dir)
    if not user_dir_path.exists():
        user_dir_path.mkdir()

    filename = filename_param + ".txt"
    path = Path(user_dir + "/" + filename)
    with path.open("w", encoding ="utf-8") as f:
        f.write(text_param)
    return jsonify({'success': True})


@bp.route('/grep_processes')
def grep_processes():
    name = request.args.get('name')
    res = subprocess.run(["ps aux | grep " + name + " | awk '{print $11}'"], shell=True, capture_output=True)
    if res.stdout is None:
        return jsonify({'error': 'no stdout returned'})
    out = res.stdout.decode("utf-8")
    names = out.split('\n')
    return jsonify({'success': True, 'names': names})

