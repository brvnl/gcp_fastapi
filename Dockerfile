FROM python:3.12-slim
EXPOSE 8081
WORKDIR /app
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT ["fastapi", "dev ", "app.py", "--server.port=8081", "--server.address=0.0.0.0"]
