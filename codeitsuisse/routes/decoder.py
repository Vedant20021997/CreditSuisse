import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def decode():
    data = request.get_json()
    possible_values = data["possible_values"]
    num_slots = data["num_slots"]
    return {"answer": random.choices(possible_values, k=num_slots)}
    
    # logging.info("My result :{}".format(result))
    # return json.dumps(result)
