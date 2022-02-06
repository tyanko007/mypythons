FROM python:3

RUN mkdir /workspace
WORKDIR /workspace
ADD requirements.txt /workspace/
RUN pip3 install -r requirements.txt
ADD . /workspace/
