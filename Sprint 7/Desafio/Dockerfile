FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    python3-pip

WORKDIR /app

COPY load_data_to_s3.py .

RUN pip install boto3

CMD ["python", "./load_data_to_s3.py"]
