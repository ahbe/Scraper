FROM python:3.8-slim

LABEL maintainer="Ahmed Belarbi <its.ahmedbelarbi@gmail.com>"

COPY . /app

WORKDIR /app

RUN python -m pip install -U pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1053
# execute the command python scraper.py (in the WORKDIR) to start the app
CMD ["python3", "./scraper.py"]