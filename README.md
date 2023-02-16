# MLOps Model Deployment
Model deployment with FastAPI + Streamlit + Docker

At first, I created a model to classify the iris dataset. 

Then I deploy this model using FastAPI for the backend service and streamlit for the frontend service. And docker-compose orchestrates the two services and allows communication between them.

To run the example in a machine running Docker and docker-compose, run:
- clone this github:
```
git clone https://github.com/thohoang87/MLOps_model_deployment.git
```

- find where your downloaded folder is in your computer, then copy its path, and run:
```
cd "(path)"
```
for exemple:
```
cd "/Users/Desktop/MLOps_model_deployment"
```

- finally, run:
```
docker-compose up
```

To visit the FastAPI documentation of the resulting service, use http://localhost:8000 with a web browser.

To visit the streamlit UI, use http://localhost:8501.
