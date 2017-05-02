FROM continuumio/anaconda3

ENV LC_ALL C
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install curl git vim wget
RUN apt-get install -y python-qt4
RUN apt-get install -y tk-dev

RUN wget https://raw.github.com/gnachman/iTerm2/master/tests/imgcat -O /usr/local/bin/imgcat
RUN chmod +x /usr/local/bin/imgcat

WORKDIR /root/study-deep-learning-from-scratch
