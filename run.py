import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Flask Chat</h1>"


app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)  # don't use debug=True in your live app!
