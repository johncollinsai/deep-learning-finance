#!/bin/bash

# I use boot.sh rather than ENTRYPOINT in the Dockerfile because the exec command 
# in my boot.sh does not work here in Dockerfile in ENTRYPOINT. Don't know why
source venv/bin/activate

# NB - explicitly pass Voila.ip to account for changes in voila-0.3.0
exec voila dl-finance.ipynb --Voila.ip=0.0.0.0 --port=8080 --no-browser --strip_sources=False --theme=dark

