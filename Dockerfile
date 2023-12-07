FROM --platform=$BUILDPLATFORM python:3.9 AS build
ADD main.py .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python", "main.py" ]