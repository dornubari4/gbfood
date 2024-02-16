FROM python:3.9
WORKDIR /order
COPY . /order
#COPY requirements.txt /menu
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5002
CMD [ "python3 ", "order.service.py" ]