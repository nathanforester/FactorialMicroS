from flask import Flask, Response, jsonify
import json
from flask import json
import sys
from flask import jsonify


def factorial(n):
    try:
        n = int(float(input("Enter a non-negative integer: ")))
        if n < 0:
            print("Please enter a non-negative integer.")
        # else:
        #     print(f"The factorial of {n} is {factorial(n)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

