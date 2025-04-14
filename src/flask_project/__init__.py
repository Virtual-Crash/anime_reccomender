from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "New services to play around with: The addition service! Use /add/<num1>/<num2> to add two numbers. or personal greeting. Use /greet/<first>/<last> to get a personal greeting"

@app.route("/add/<int:num1>/<int:num2>")
def add_numbers(num1, num2):
    result = num1 + num2
    return f"The sum of {num1} and {num2} is {result}."

@app.route("/greet/<string:first>/<string:last>")
def add_greeting(first, last):
    first_normalized = first.lower()

    if first_normalized in ["lee", "lee-roy"]:
        return f"I LOVE YOU SO MUCH {first}!"
    else:
        return f"Hello {first} {last}"    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#test