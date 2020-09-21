FROM ubuntu:18.04
COPY . /app
RUN apt update && apt upgrade -y && apt install -y python python3 python-pip python3-pip  
RUN pip3 install --upgrade pip
RUN pip3 --no-cache-dir install --default-timeout=100 -r /app/requirements.txt
WORKDIR /app
EXPOSE 5000
CMD python3 /app/Flask_api.py
