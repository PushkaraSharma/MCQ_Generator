FROM ubuntu:18.04

RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /app
RUN apt update && apt upgrade -y && apt install -y python python3 python-pip python3-pip  
RUN apt-get install -y git
RUN pip3 install --upgrade pip
RUN pip3 --no-cache-dir install --default-timeout=100 -r /app/requirements.txt
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader averaged_perceptron_tagger
RUN python3 -m nltk.downloader stopwords
RUN python3 -m spacy download en

WORKDIR /app
EXPOSE 5000
CMD python3 /app/Flask_api.py

