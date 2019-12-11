# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request
from flask import jsonify
app = Flask(__name__)

# The Fibonacci function

#with app.app_context():
    # within this block, current_app points to app.
  #  print(current_app.name)

def fibonacci(n:int):
    """
    Calculating the fibonacci numbers
    """

    result = []
    f1 = 0
    f2 = 1
    if n < 1:
        return "Please enter a positive integer"
    elif n == 1:
        return 1
    else:
        for x in range(0, n): 
            result.append(f1)
            f3 = f1 + f2 
            f1 = f2 
            f2 = f3
            
    return jsonify(result)

# The actual route
@app.route("/")
def get_fibonacci():

    try:
        n = request.args.get("n")
        print(n)
        if n is None:
            return "Please provide an argument n with a positive integer"
        elif not n.isdigit():
            return "Please enter a positive integer"
        return fibonacci(int(n)) 
    except ValueError:
        return "Please enter a positive integer"
        
if __name__ == '__main__' : 
    app.run()