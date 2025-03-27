FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install numpy
RUN pip install pyspark
RUN pip install ucimlrepo

CMD ["python3", "--version"]
