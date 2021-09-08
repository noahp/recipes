FROM peaceiris/mdbook:v0.4.12

# add python3
RUN apk add --no-cache python3

# change entrypoint to normal shell not mdbook
ENTRYPOINT [ "/bin/sh" ]
