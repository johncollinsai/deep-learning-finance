FROM python:slim

WORKDIR /home/posts/deep-learning-finance

COPY requirements.txt requirements.txt 
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

# I use boot.sh rather than ENTRYPOINT in the Dockerfile because the exec command
# in my boot.sh does not work here in Dockerfile in ENTRYPOINT. Don't know why
COPY dl-finance.ipynb boot.sh ./ 
RUN chmod a+x boot.sh
ENV PORT 8080

ENTRYPOINT ["./boot.sh"]



