from USUARIOWEB import app
from flask import render_template, request, jsonify

@app.route('/')
def acessar_index():
    return render_template('index.html') 