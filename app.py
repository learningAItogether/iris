
from flask import Flask, render_template, request,redirect, url_for
import numpy as np
import model

#建立一个API
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def submit():
    
    if request.method == "GET":
        return render_template("index.html")
    
    else:
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
            
        return render_template('prediction.html',result = result)



#启动服务器
if __name__ == '__main__':
    app.run(debug=True)