FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app 
RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]