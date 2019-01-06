from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    method = request.method
    ip = request.remote_addr
    return f'<h2>This is flask. You are using: </h2> {user_agent}<br> {method} from {ip}'


@app.route('/reddit/<subreddit>')
def reddit(subreddit):
    return redirect(f'https://reddit.com/r/{subreddit}')


if __name__ == '__main__':
    app.run()
