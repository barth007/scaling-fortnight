from flask import Flask, jsonify, make_response, abort, request
from datetime import datetime as dt, timedelta

app = Flask(__name__)


def current_date_time():
    """excutes the utc date and time"""


    now = dt.utcnow()
    WAT_now = (now + timedelta(hours = 1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    #string = dt.isoformat(WAT_now)
    return WAT_now


def current_day():
    """excutes the current day in full"""


    now = dt.utcnow()
    WAT_now = now + timedelta(hours = 1)
    day = WAT_now.strftime("%A")
    return day


details = {
            "slack_name": "Codeslinger",
            "current_day": current_day(),
            "utc_time": current_date_time(),
            "track": "backend",
            "github_file_url": "https://github.com/barth007/scaling-fortnight/hng_task1/app.py",
            "github_repo_url": "https://github.com/barth007/scaling-fortnight",
            "status_code": 200
        }


@app.route('/hng/api', methods=['GET'])
def get_all():
    """ route for fetching a particular detail"""


    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    if slack_name != details['slack_name'] or track != details['track']:
        abort(not_found(404))
    if slack_name is None or track is None:
        abort(bad_request(400))
    return jsonify(details)


@app.errorhandler(400)
def bad_request(error):
    """error for NULL input"""


    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    """error for wrong input or None existing values"""


    return make_response(jsonify({'error': 'Not Found'}))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
