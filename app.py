from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def file_upload():
  if request.method == 'POST' and request.content_length <= 1_000_000:
    uploaded_file = request.get_data(cache=False, as_text=True)
    print(uploaded_file)
    return "<p>Received file!</p>"