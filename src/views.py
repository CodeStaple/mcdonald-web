from app import app
from flask import make_response, jsonify, render_template
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] (%(threadName)-9s) %(message)s',)

@app.route("/mcdonald/burger", methods=["GET"])
def index():
    logging.debug("Hello world from Mc Donalds!")
    return render_template("index.html")

# ERROR HANDLING
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)