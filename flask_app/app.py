from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg",
    "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg",
    "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg",
    "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg",
    "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg",
    "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg",
    "https://i.insider.com/602ee9d81a89f20019a377c6?width=1136&format=jpeg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")