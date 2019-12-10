FROM python:3.8.0

RUN mkdir /usr/src/Tweetproj
WORKDIR /usr/src/Tweetproj

COPY requirements.txt /usr/src/Tweetproj/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/Tweetproj/
WORKDIR /usr/src/Tweetproj/backend
RUN chmod +x ./run.sh

CMD [ "./run.sh" ]