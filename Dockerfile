FROM continuumio/anaconda3

RUN apt-get install -y python-qt4
RUN apt-get install -y tk-dev

RUN mkdir /root/zero-deep-learning
WORKDIR /root/zero-deep-learning
