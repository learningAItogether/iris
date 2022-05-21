from tensorflow.keras.models import load_model
import numpy as np

# 加载模型
model = load_model('model/model_iris.h5')

#模型预测
def prediction(input):
    pred = model.predict(input)
    pred_=np.argmax(pred[0])
    return pred_