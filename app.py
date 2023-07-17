#서버 뛰우기
from flask import Flask , render_template , request  
from data import Articles
# print(Articles())
#flask 안에 Flask 객체를 가져온다.
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    # if request.method == 'GET':
    #     os_info = dict(request.headers)
    #     print(os_info)
    #     name = request.args.get("name")
    #     print(name)
    #     hello = request.args.get("hello")
    #     print(hello)
    #     return render_template("index.html",header=f'{name}님 {hello}!!!ㅋㅋㅋ')
    # elif request.method == 'POST' :
    #     # data = request.get_data()
    #     data = request.form.get("name")
    #     data_2 = request.form['hello']
    #     print(data)
    #     print(data_2)
    #     return render_template("index.html",header="안녕하세요")
    return render_template("index.html")
    # os_info = dict(request.headers) #['Sec-Ch-Ua']
    # req_data = request.get_json()
    # print(os_info)
    # print(os_info)
    # return render_template("index.html",header=os_info)
    #jinja2 문법. 렌더 템플릿에 첫번째 인자값 이후 2번쨰부터 원하는 값을 적으면 표현하는것
@app.route('/hello', methods =["GET","POST"])
def hello():
    if request.method == "GET":
        return render_template("hello.html")
    elif request.method == "POST":
        name=request.form["name"]
        hello=request.form["hello"]
        return render_template('index.html',name=name , hello = hello)
    
@app.route('/list',methods = ["GET","POST"])
def list():    
    data = Articles()      
    return render_template("list.html",data = data)
   

if __name__ == '__main__':
    app.run(debug=True)