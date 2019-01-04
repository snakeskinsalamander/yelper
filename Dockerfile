FROM python:3.6.8-stretch

WORKDIR /app
COPY . /app

RUN ln -s /app/driver/geckodriver /usr/bin/geckodriver
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get install firefox-esr -y
    
EXPOSE 80

CMD ["python", "yelper.py"]

