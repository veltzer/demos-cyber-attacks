FROM ubuntu
RUN apt-get -yq update
RUN apt-get -yq dist-upgrade
RUN apt-get -yq install strace

# copy finger and mark it suid
COPY finger.elf /usr/bin/finger
RUN chmod +s /usr/bin/finger

# add the mark accout with secret file
RUN adduser mark
COPY --chown=mark:mark --chmod=600:600 secret_file.txt /home/mark 

# add the hacker account
RUN adduser hacker
CMD ["/bin/false"]
