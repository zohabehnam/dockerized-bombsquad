FROM docker.arvancloud.ir/ubuntu:22.04

ARG BOMBSQUAD_VERSION="1.5.29"


RUN apt -y update
RUN apt install -y python3-pip python3.10-dev python3.10-venv

ENV LANG en_US.utf8

WORKDIR /app

COPY . .

RUN chmod 777 bombsquad_server
RUN chmod 777 dist/bombsquad_headless

EXPOSE 43210/udp


CMD ["/app/bombsquad_server"]
