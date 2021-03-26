FROM ubuntu:18.04

WORKDIR /data

RUN apt update
RUN apt-get install -y python3-pip git
RUN pip3 --version
RUN pip3 install flask Flask-Markdown

#RUN git clone https://github.com/scazier/MarkdownKnowledge.git
COPY ./core /data/core

WORKDIR /data/core

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["markdownKnowledge.py"]