from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/github', methods=['POST'])
def github_event():
    # GitHub event handling logic will go here
    return jsonify({'status': 'received'})

if __name__ == '__main__':
    app.run(port=5000)
