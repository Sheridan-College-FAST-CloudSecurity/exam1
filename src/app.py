from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/hello")
def hello():
    name = request.args.get("name", "World")
    return jsonify({"message": f"Hello, {name}"})


if __name__ == "__main__":
    app.run(debug=False)


# Insecure example
user_input = input("Enter something: xyz")
print(user_input)
