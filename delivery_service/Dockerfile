FROM python:3.9
WORKDIR /delivery
COPY . /delivery
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5006
CMD [ "python3 ", "delivery.service.py" ]