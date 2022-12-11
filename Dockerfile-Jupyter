FROM jupyter/minimal-notebook

RUN pip install voila

ENV PORT=8080

WORKDIR /home/posts/deep-learning-finance

COPY dl-finance.ipynb /home/posts/deep-learning-finance/dl-finance.ipynb 

ENTRYPOINT ["/boot.sh"]

