# parent image
FROM python:3.9 

# copy everything from . to /app
COPY . /app

# all commands will be run from /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# what to do when run
CMD [ "python", "test.py"]
