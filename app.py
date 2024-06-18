from flask import Flask, render_template, request, send_file
from download_track import download_track
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        url = request.form['url']
        # Use download_track to process the URL and get the MP3 file path
        mp3_file_path = download_track(url)
        if os.path.exists(mp3_file_path):
            return send_file(mp3_file_path, as_attachment=True)
        else:
            return "Failed to download the track.", 404
    return 'Please submit the form.'

if __name__ == '__main__':
    app.run(debug=True)
