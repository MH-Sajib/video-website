import os

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Configure uploads directory (adjust path as needed)
UPLOAD_FOLDER = '/path/to/uploads'
ALLOWED_EXTENSIONS = {'mp4', 'mov'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_video():
    from werkzeug.utils import secure_filename
    if request.method == 'POST':
        # Get video file
        video = request.files['video']
        if video and allowed_file(video.filename):
            filename = secure_filename(video.filename) 
            video.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('upload_success'))
        else:
            return redirect(url_for('upload_error'))
    return render_template('upload.html')  # Render upload form on GET request

@app.route('/upload_success')
def upload_success():
    return render_template('success.html')  # Show success message

@app.route('/upload_error')
def upload_error():
    return render_template('error.html')  # Show error message if upload fails

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production