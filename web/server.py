"""Include flask app variable

Routs
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def view_root():
    """Root page"""
    return render_template('root.html')
