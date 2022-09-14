FROM alpine:3.14
RUN apk update
RUN apk add python3 git bash bash-doc bash-completion openssh-client
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd
COPY bashrc_aliases /tmp/bashrc_aliases
RUN touch /root/.bashrc && cat /tmp/bashrc_aliases >> /root/.bashrc
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN /usr/bin/python3 -m pip install -U flake8
RUN apk add openjdk17 --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community
