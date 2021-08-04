FROM python:3.8

WORKDIR /home
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN export PYTHONPATH="/home/src:${PYTHONPATH}"
RUN pip install -i https://test.pypi.org/simple/ tweet-preprocesser
# RUN pip --no-cache-dir install --upgrade --index-url https://test.pypi.org/simple/ tweet_preprocesser