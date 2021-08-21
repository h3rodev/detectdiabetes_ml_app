from flask import Flask, jsonify
from flask_cors import CORS
import getDR

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
# p, g, bp, st, i, bmi, dpf, a
@app.route('/api/<int:p>/<int:g>/<int:bp>/<int:st>/<int:i>/<float:bmi>/<float:dpf>/<int:a>', methods=['GET'])
def get_result(p, g, bp, st, i, bmi, dpf, a):
    passgen = {
        "data": getDR.getData(p, g, bp, st, i, bmi, dpf, a)
    }

    return jsonify(passgen)


if __name__ == '__main__':
    app.run()
