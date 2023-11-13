from flask import Flask,send_file

app = Flask(__name__)

@app.route('/')
def send_pdf():
    pdf_path = 'aa.pdf'  # 替换为实际的PDF文件路径
    return send_file(pdf_path, mimetype='application/pdf')

