# Minimal alpine image, since I'm not using anything besides python3.8+

FROM python:3.9.1-alpine3.12

# get user id from build arg, so we can have read/write access to directories
# mounted inside the container. only the UID is necessary, UNAME just for
# cosmetics
ARG UID=1010
ARG UNAME=builder

# create a user matching the UID passed, so we can read/write the mounted
# directory. help for the cheesy busybox version of adduer below.

# / # adduser --help
# BusyBox v1.31.1 () multi-call binary.

# Usage: adduser [OPTIONS] USER [GROUP]

# Create new user, or add USER to GROUP

#         -h DIR          Home directory
#         -g GECOS        GECOS field
#         -s SHELL        Login shell
#         -G GRP          Group
#         -S              Create a system user
#         -D              Don't assign a password
#         -H              Don't create home directory
#         -u UID          User id
#         -k SKEL         Skeleton directory (/etc/skel)
RUN addgroup -S ${UNAME} && adduser -D -S ${UNAME} -G ${UNAME} -u ${UID}

USER ${UNAME}

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ENV PATH /home/${UNAME}/.local/bin:$PATH

# Install these in the base conda env
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --user -r /tmp/requirements.txt

WORKDIR /mnt/workspace
