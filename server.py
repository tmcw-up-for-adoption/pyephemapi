import ephem, datetime
from flask import Flask, jsonify, request, jsonify
from datetime import timedelta
from functools import update_wrapper

app = Flask(__name__)

@app.route('/')
def main():
    name = str(request.args.get('name', ''))
    line1 = str(request.args.get('line1', ''))
    line2 = str(request.args.get('line2', ''))
    tle_rec = ephem.readtle(name, line1, line2)
    tle_rec.compute()
    return jsonify(coords=[float(tle_rec.sublong), float(tle_rec.sublat)])

if __name__ == "__main__":
    app.run()
