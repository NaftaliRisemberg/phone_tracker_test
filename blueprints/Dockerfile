FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY phone_bp.py .
CMD ["python", "phone_bp.py"]