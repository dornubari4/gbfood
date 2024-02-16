FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip
WORKDIR /review
COPY . /review
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
EXPOSE 5007
CMD [ "python3 ", "review.service.py" ]