FROM ubuntu:16.04

#MAINTANER Your Name "andre-ramos1994@hotmail.com"\

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./backend/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

COPY ./backend /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
