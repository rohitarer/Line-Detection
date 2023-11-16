FROM python:3.11-bullseye

WORKDIR /app

COPY . /app
RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx
RUN pip install opencv-python numpy paho-mqtt
EXPOSE 3000
CMD python ./Line_Detection.py
