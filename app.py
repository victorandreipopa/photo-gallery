from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
import os
from PIL import Image

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route
@app.route('/')
def index():
    images = {}
    for category in os.listdir(UPLOAD_FOLDER):
        category_path = os.path.join(UPLOAD_FOLDER, category)
        if os.path.isdir(category_path):
            images[category] = [os.path.join(category, file) for file in os.listdir(category_path) if allowed_file(file)]
    return render_template('index.html', images=images)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # Simplified authentication
            session['logged_in'] = True
            return redirect(url_for('upload'))
        else:
            flash('Invalid credentials')
            return redirect(url_for('login'))
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

# Upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            category = request.form['category']
            category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
            os.makedirs(category_path, exist_ok=True)
            file.save(os.path.join(category_path, filename))

            # Create thumbnail
            img = Image.open(os.path.join(category_path, filename))
            img.thumbnail((200, 200))
            thumb_path = os.path.join(category_path, f"{filename}.thumb.jpg")
            img.save(thumb_path)

            flash('File successfully uploaded')
            return redirect(url_for('upload'))
    return render_template('upload.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
