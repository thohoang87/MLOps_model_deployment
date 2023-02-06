from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import json
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Iris Dataset Prediction"}


# loading the saved model
model = joblib.load("model.sav")

# define the data type for all the inputs
class model_input(BaseModel):
    
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

# Creating a POST request to the API
@app.post('/iris_prediction')
def iris_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    sepal_length = input_dictionary['sepal_length']
    sepal_width = input_dictionary['sepal_width']
    petal_length = input_dictionary['petal_length']
    petal_width = input_dictionary['petal_width']
    
    
    input_list = [sepal_length, sepal_width, petal_length, petal_width]
    
    prediction = model.predict([input_list])
 
    if (prediction[0] == 0):
        pred = 'setosa'
    elif (prediction[0] == 1):
        pred = 'versicolor'
    else:
        pred = 'virginica'
        
    return {'Prediction':  pred}
