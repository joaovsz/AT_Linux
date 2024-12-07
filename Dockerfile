

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3

COPY hello-world.py /hello-world.py
CMD ["python3", "/hello-world.py"]
