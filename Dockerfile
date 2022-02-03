FROM python:3.9.7

WORKDIR /usr/app

RUN mkdir result

RUN mkdir src

EXPOSE 8888

RUN pip install --no-cache-dir --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN pip install jupyter

RUN jupyter notebook --generate-config --allow-root

ENTRYPOINT jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser
