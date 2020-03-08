from flask import Flask


class Blockchain:
    def __int__(self):
        self.transaction = []
        self.chain = []


blockchain = Blockchain()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=1001, type=int, help='porta qe do te degjojm ')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)