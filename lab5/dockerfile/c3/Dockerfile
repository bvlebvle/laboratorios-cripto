FROM ubuntu:18.10

RUN sed -i 's/http:\/\/ports.ubuntu.com\/ubuntu-ports/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list && \
	sed -i '/^deb.*security.ubuntu.com/s/^/#/' /etc/apt/sources.list && \ 
	apt-get update && \
	apt-get install -y sudo net-tools openssh-client


