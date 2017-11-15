FROM mongo:3.4.10
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r dependencias.txt
EXPOSE 80
CMD ["python", "run.py"]