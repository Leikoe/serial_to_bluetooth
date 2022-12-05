# serial to bluetooth module for ssl robots

## How to use
```shell
# setup virtual serial with baudrate 39600
socat -d -d pty,raw,echo=0,b38400 pty,raw,echo=0,b38400


```

then you will need to send packets on one of the fds and read on the other (modify it in the main.py)