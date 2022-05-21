from flask import Flask, render_template, request
import numpy as np
import model

#建立一个API
app = Flask(__name__)

#网页功能

@app.route('/')
def index():
    return render_template("index.html")#先引入index.html，同时根据后面传入的参数，对html进行修改渲染。

@app.route('/submit', methods=['POST'])
def submit():
    #features = [x for x in request.form.values()]#存储用户输入的参数
    #input = [[np.array(features)]]#将用户输入的值转化为一个数组
    
    x1  = float(request.form.get('sepalLengthCm'))
    x2 = float(request.form.get('sepalWidthCm'))
    x3 = float(request.form.get('petalLengthCm'))
    x4 = float(request.form.get('petalWidthCm'))
    input = np.array([[x1,x2,x3,x4]])
    
    result = model.prediction(input)
    if( result == 0):
        result = "setosa"
    elif( result == 1):
        result = "versicolor"
    else:
        result = "verginica"

    return render_template('index.html',result1=result)

#启动服务器
if __name__ == '__main__':
    app.run(debug=True)