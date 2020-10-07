from fastapi import FastAPI
import math

app = FastAPI()

def x_to_the_e():
    value = input("What exponent would you like to choose?")
    intValue = int(value)
    return { "x to the e" : math.exp(intValue)}
