from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = 'dfsdf'

# Mock data for resources
resources = [
    {"title": "Physics Notes", "description": "Detailed physics notes", "filename": "physics.pdf"},
    {"title": "Math Problems", "description": "Sample math problems", "filename": "math.pdf"}
]

recommendations = [
    {"title": "Quantum Physics", "description": "Introduction to quantum physics", "filename": "quantum.pdf"}
]


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')
"""
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        title = request.form['title']
        description = request.form['description']
        
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resources.append({"title": title, "description": description, "filename": filename})
            return redirect(url_for('home'))
    return render_template('upload.html')

@app.route('/profile')
def profile():
    # You can dynamically load user-specific uploads here
    return render_template('profile.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/perform_search', methods=['GET'])
def perform_search():
    query = request.args.get('query')
    result = [res for res in resources if query.lower() in res['title'].lower()]
    return jsonify(result)

@app.route('/recommendations')
def recommendations_page():
    return render_template('recommendations.html')

@app.route('/get_recommendations', methods=['GET'])
def get_recommendations():
    return jsonify(recommendations)
"""
if __name__ == '__main__':
    app.run(debug=True)
