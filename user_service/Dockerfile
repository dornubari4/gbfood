FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip
WORKDIR /user
COPY . /user
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
EXPOSE 5003
CMD [ "python3 ", "user.service.py" ]