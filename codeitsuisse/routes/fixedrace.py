import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluate():
    data = request.get_data(as_text=True)
    list_data = list(data.split(','))
    string = ','
    formation = random.shuffle(list_data)
    return string.join(formation)
    
    # logging.info("My result :{}".format(result))
    # return json.dumps(result)

