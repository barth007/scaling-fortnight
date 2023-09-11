from flask import Flask, jsonify, make_response, abort, request
from datetime import datetime as dt, timedelta

app = Flask(__name__)



@app.route('/hng/api', methods=['GET'])
def get_all():
    """ route for fetching a particular detail"""


    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = dt.utcnow().strftime('%A')
    current_date_time = dt.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/barth007/scaling-fortnight/hng_task1/app.py"
    github_repo_url =  "https://github.com/barth007/scaling-fortnight"
    if slack_name is None or track is None:
        abort(bad_request(400))

    details = {
                "slack_name": slack_name,
                "current_day": current_day,
                "utc_time": current_date_time,
                "track": track,
                "github_file_url": github_file_url,
                "github_repo_url": github_repo_url,
                "status_code": 200
            }
    return jsonify(details)


@app.errorhandler(400)
def bad_request(error):
    """error for NULL input"""


    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
