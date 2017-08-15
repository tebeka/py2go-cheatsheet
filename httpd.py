# START
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Python'


if __name__ == '__main__':
    app.run(port=8080)
# END
