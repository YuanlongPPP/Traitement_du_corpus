FROM alpine:latest
RUN apk update && apk add --no-cache \
    openssh \
    sqlite \
    python3 \
    py3-pip \
    bash

RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN adduser -h /home/user -s /bin/sh -D user
RUN echo -n "user:defaultpassword" | chpasswd

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 22

COPY entrypoint.sh /
COPY insert_data.py /home/user/
RUN chmod +x /home/user/insert_data.py
ENTRYPOINT ["/entrypoint.sh"]

