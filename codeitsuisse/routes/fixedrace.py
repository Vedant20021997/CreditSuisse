import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluate():
    data = request.get_data(as_text=True)
    print(data)
    print(type(data))
    list_data = list(data.split(','))
    random.shuffle(list_data)
    return ','.join(list_data)
    
    # logging.info("My result :{}".format(result))
    # return json.dumps(result)

