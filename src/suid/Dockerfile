FROM ubuntu:24.04
RUN apt-get -yq update && \
    apt-get -yq dist-upgrade && \
    apt-get -yq install --no-install-recommends strace adduser && \
    rm -rf /var/lib/apt/lists/*

# copy finger and mark it suid
COPY finger.elf /usr/bin/finger
RUN chmod +s /usr/bin/finger

# add the mark accout with secret file
RUN adduser mark
COPY --chown=mark:mark --chmod=600:600 secret_file.txt /home/mark

# add the hacker account
RUN adduser hacker
CMD ["/bin/false"]
