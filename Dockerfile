FROM continuumio/miniconda3

# Install packages
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN conda create --name deep-learning-finance python=3.7

# Activate environment
RUN echo "source activate deep-learning-finance" > ~/.bashrc
ENV PATH /opt/conda/envs/deep-learning-finance/bin:$PATH

# Install the necessary packages 
RUN pip install --upgrade pip \
    jupyter \
    voila \
    numpy \
    pandas \
    scikit-learn \
    matplotlib 

# Set working directory
WORKDIR /home/posts/deep-learning-finance

CMD voila dl-finance.ipynb --Voila.ip=0.0.0.0 --port=8080 --no-browser --strip_sources=False --theme=dark 
