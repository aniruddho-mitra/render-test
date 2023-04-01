import pickle

import numpy as np
from flask import Flask, request, jsonify

model=pickle.load(open('model.pkl','rb'))
#in the above line the input from the user will be from a form
app=Flask(__name__)
@app.route('/')

def home():
    return "Hi Anirudh"

@app.route('/predict',methods=['POST']) #our api will reside here
def predict():
    pH=request.form.get('pH')
    temp=request.form.get('temp')
    fat=request.form.get('fat')

    #result={'ph':pH,'temp':temp,'fat':fat} #this is a dictionary

    input_query=np.array([[pH,temp,fat]],dtype=float) #this will be the input for our model

    result=model.predict(input_query)[0]


    return jsonify({'adulterated':str(result)}) #this line will return the output to a json format

if __name__=="__main__":
    app.run(debug=True)