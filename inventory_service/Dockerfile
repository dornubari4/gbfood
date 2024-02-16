FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip
WORKDIR /inventory
COPY . /inventory
RUN pip install --upgrade 
RUN pip install -r requirements.txt 
EXPOSE 5008
CMD [ "python3 ", "inventory.service.py" ]