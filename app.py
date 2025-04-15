from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, World! Welcome to the CI/CD pipeline!")

@app.route('/health')
def health_check():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

