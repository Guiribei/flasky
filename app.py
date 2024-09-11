from flask import Flask, render_template, redirect, url_for, session
import subprocess
import json
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger-script', methods=['POST'])
def trigger_script():
    try:

        result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
        
        if result.returncode != 0:
            raise Exception(result.stderr)

        json_data = json.loads(result.stdout)
        
        session['json_data'] = json_data
        
        return redirect(url_for('success'))
    
    except Exception as e:
        e = str(e)
        lista = e.split('Exception:')
        session['error_message'] = lista[1]
        return redirect(url_for('error'))

@app.route('/success')
def success():
    if 'json_data' in session:
        data = session['json_data']['users']
        return render_template('success.html', data=data)
    else:
        return "No data available. Run the script first.", 404

@app.route('/error')
def error():
    if 'error_message' in session:
        error_message = session['error_message']
        return render_template('error.html', error_message=error_message)
    else:
        return "No error message available.", 404

if __name__ == '__main__':
    app.run(debug=True)