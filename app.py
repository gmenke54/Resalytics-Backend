from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods=['POST'])
def file_upload():
  if request.method == 'POST' and request.content_length <= 1_000_000:
    files = request.files
    print(files['file'])
    res = Response(response="<p>Received file!</p>")
    res.access_control_allow_origin = '*'
    return res