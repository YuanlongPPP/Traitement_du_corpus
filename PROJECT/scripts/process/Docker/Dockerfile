# 使用最新版本的Alpine Linux
FROM alpine:latest

# 安装openssh、sqlite、python3和bash
RUN apk update && apk add --no-cache \
    openssh \
    sqlite \
    python3 \
    py3-pip \
    bash

# 允许密码认证
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
# 创建用户
RUN adduser -h /home/user -s /bin/sh -D user
# 设置用户密码
RUN echo -n "user:defaultpassword" | chpasswd

# 设置entrypoint脚本
ENTRYPOINT ["/entrypoint.sh"]

# 暴露端口22
EXPOSE 22

# 复制entrypoint脚本到容器中
COPY entrypoint.sh /
COPY insert_data.py /home/user/  # 复制 insert_data.py 到容器中
RUN chmod +x /home/user/insert_data.py

ENTRYPOINT ["/entrypoint.sh"]

