import sys
print( sys.path)
import sklearn
from flask import Flask
import pandas as pd


from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import module2
print(module2.a)

module2.printjoke("This is me")