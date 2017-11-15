FROM python:3.6.3-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r dependencias.txt
EXPOSE 80
CMD ["python", "run.py"]