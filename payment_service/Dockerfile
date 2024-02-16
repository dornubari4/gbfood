FROM python:3.9
WORKDIR /payment
COPY . /payment
#COPY requirements.txt /menu
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5004
CMD [ "python3 ", "payment.service.py" ]