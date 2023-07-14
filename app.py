#서버 뛰우기
from flask import Flask , render_template , request
#flask 안에 Flask 객체를 가져온다.
app = Flask(__name__)

@app.route('/')
def index():
    os_info = dict(request.headers) #['Sec-Ch-Ua']
    print(os_info)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)