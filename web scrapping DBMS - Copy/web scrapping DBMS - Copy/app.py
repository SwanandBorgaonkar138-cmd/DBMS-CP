from flask import Flask
from flask import render_template
from flask import request
from services.url_detector import detect_platform
from services.profile_parser import extract_profile_info

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Search Route
@app.route("/search", methods=["POST"])
def search():

    profile_url = request.form["profile_url"]

    info = extract_profile_info(profile_url)



    return f"""
    <h1>Profile Information</h1>

    <pre>{info}</pre>


    <br>

    

    <a href="/">Go Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)