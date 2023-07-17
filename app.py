#서버 뛰우기
from flask import Flask , render_template , request
#flask 안에 Flask 객체를 가져온다.
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        os_info = dict(request.headers)
        print(os_info)
        return render_template("index.html",header=os_info)
    elif request.method == 'POST' :
        return render_template("index.html",header="안녕하세요")
    # os_info = dict(request.headers) #['Sec-Ch-Ua']
    # req_data = request.get_json()
    # print(os_info)
    # print(os_info)
    # return render_template("index.html",header=os_info)
    #jinja2 문법. 렌더 템플릿에 첫번째 인자값 이후 2번쨰부터 원하는 값을 적으면 표현하는것
if __name__ == '__main__':
    app.run(debug=True)