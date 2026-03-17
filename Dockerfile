FROM python:3.9-slim
WORKDIR /app
COPY requirments.txt .  
RUN pip install --no-cache-dir -r requirments.txt
COPY app.py . 
EXPOSE 80
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]