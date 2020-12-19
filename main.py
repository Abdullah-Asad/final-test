import cv2
from flask import Flask, request


def prepare(file):
    IMG_SIZE = 50
    new_array = cv2.resize(file, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)





app = Flask(__name__)


@app.route('/')
def home_endpoint():
    return 'Hello World!'


if __name__ == '__main__':

    app.run(debug=True)
