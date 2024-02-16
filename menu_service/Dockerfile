FROM python:3.9
WORKDIR /menu
COPY . /menu
#COPY requirements.txt /menu
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001 
CMD [ "python3 ", "menu.service.py" ]