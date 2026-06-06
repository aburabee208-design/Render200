from flask import Flask, request, make_response
import json
import os

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    response_data = {
        "valid": True,
        "reason": "ok",
        "expires": "2099-12-31T23:59:59Z",
        "sig": "42e051828c47281e49f21a0d674bbcb014f645118c8961e8bb965053bcea1132"
    }
    json_response = json.dumps(response_data, separators=(',', ':'))
    response = make_response(json_response, 200)
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
