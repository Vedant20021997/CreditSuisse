import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def decode():
    data = request.get_json()
    print(data)
    possible_values = data["possible_values"]
    print(possible_values)
    num_slots = data["num_slots"]
    print(num_slots)
    possible_values = ["x","q","v","k", "c"]
    choice = random.choices(possible_values, k=num_slots)
    print(choice)
    return jsonify({"answer": choice})
    
    # logging.info("My result :{}".format(result))
    # return json.dumps(result)
