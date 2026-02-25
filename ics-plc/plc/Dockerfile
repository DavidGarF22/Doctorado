FROM python:3.11-slim
RUN pip install pymodbus==3.6.4
COPY server.py /app/server.py
CMD ["python", "/app/server.py"]
