from flask import Flask, request, Response
from docx import Document

app = Flask(__name__)

@app.route("/", methods=['POST'])
def file_upload():
  if request.method == 'POST' and request.content_length <= 1_000_000:
    files = request.files
    print(request.form)
    document = Document(files['file'])
    res = Response()

    for paragraph in document.paragraphs:
      paragraph.text = ''
    
    document.save(res.stream)
    
  
    res.access_control_allow_origin = '*'
    res.content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    return res