FROM ubuntu:bionic
COPY image_files/ /
RUN apt-get update -y \
    && apt-get install -y \
       rsyslog \ 
       python \
       python-pip \
    && pip install jinja2
ENV ALLOWEDSENDERS="" 
CMD /start.sh
