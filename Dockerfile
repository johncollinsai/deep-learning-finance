FROM jupyter/minimal-notebook:latest

RUN pip install voila
RUN pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

WORKDIR /home/posts/deep-learning-finance

EXPOSE 8080

CMD voila --no-browser --port=8080 --base_url=/dlf --enable_nbextensions=True --template=dark


