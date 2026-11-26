FROM ubuntu:24.04
RUN apt-get -yq update && \
    apt-get -yq dist-upgrade && \
    apt-get -yq install --no-install-recommends strace adduser && \
    rm -rf /var/lib/apt/lists/*

# copy finger
COPY finger.elf /usr/bin/finger

# mark finger suid, and add the mark account and the hacker account
RUN chmod +s /usr/bin/finger \
    && adduser mark \
    && adduser hacker

# the secret file of the mark account
COPY --chown=mark:mark --chmod=600:600 secret_file.txt /home/mark
CMD ["/bin/false"]
