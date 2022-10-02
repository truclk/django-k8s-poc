FROM python:3.9.8

# If this argument is present then we're installing developer dependencies.
ARG debug

WORKDIR /tmp/build

# Install live dependencies.
COPY requirements.txt requirements.txt
RUN \
    mkdir /workspace && \
    pip3 install -r requirements.txt

COPY requirements.dev.txt requirements.dev.txt
RUN pip3 install -r requirements.dev.txt

# Cleanup
RUN rm -rf /tmp/build

WORKDIR /workspace
COPY upload_project .

CMD ./manage.py runserver 0.0.0.0:80 
