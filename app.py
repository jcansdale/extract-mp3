from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        url = request.form['url']
        # Ensure the file exists and is accessible
        filename = 'testfile.txt'
        filepath = os.path.join(app.root_path, 'static', filename)
        if os.path.exists(filepath):
            return send_file(filepath)
        else:
            return "File not found.", 404
    return 'Please submit the form.'



if __name__ == '__main__':
    app.run(debug=True)
