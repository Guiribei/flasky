from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger-script', methods=['POST'])
def trigger_script():
    try:
        # Trigger the Python script using subprocess
        subprocess.Popen(['python', 'script.py'])
        return 'Success', 200
    except Exception as e:
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)