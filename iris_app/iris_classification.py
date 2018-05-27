import sys
import time
import json
import numpy as np
from sklearn.externals import joblib


# iris target class
class_dict = {0: 'setosa',
              1: 'versicolor',
              2: 'virginica'}

now = time.time()


# func.toLog(param) みたいに作り変える。
#   - func の実行結果を返し、かつログに param を吐き出す。
#   - デコレータよりも細かい粒度でロギングできる点で優れる。
def export_log(text, prefix=''):
    file_name = './log/log_{}.txt'.format(now)
    with open(file_name, 'a') as f:
        f.write(prefix + str(text) + '\n')
        f.flush()


def read_stdin():
    json_params = sys.stdin.readline()
    # export_log(json_params, 'stdin: ')

    return json.loads(json_params)


def run_prediction():
    json_params = read_stdin()
    # export_log(json_params, 'json: ')

    # dict 型データに対するバリデートなども必要
    new_iris_data = np.array([list(json_params.values())])

    model = joblib.load('model.pkl')  # 97.4%
    prediction = model.predict(new_iris_data)[0]

    # export_log(prediction, 'prediction: ')
    print(class_dict[prediction])


if __name__ == '__main__':
    run_prediction()
