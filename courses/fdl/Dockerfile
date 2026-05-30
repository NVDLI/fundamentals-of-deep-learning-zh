FROM 224292665285.dkr.ecr.us-east-1.amazonaws.com/base-c-fx-01-v3-task1:v0.0.1

ENV SHELL /bin/bash
WORKDIR /dli
COPY tutorials .
COPY environment .

EXPOSE 8888
ENTRYPOINT ["/dli/environment/entrypoint.sh"]
