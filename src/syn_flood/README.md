# SYN flood attack

Show this demo once with

```bash
--sysctl "net.ipv4.tcp_syncookies=0"\
```

and once with them turned on.

## How to demo

Go into the client and run `./measure.py`.

Go into the hacker and run `./synflood.py`

Go into the server and run `netstat -nt4 | grep "SYN_RECV"`

## Links
* [Hypro999/synflood.c](https://github.com/Hypro999/synflood.c/tree/master/src)
* [EmreOvunc/Python-SYN-Flood-Attack-Tool](https://github.com/EmreOvunc/Python-SYN-Flood-Attack-Tool/tree/master)
* [knight42/synflood (Docker Hub)](https://hub.docker.com/r/knight42/synflood)
* [knight42/synflood-play](https://github.com/knight42/synflood-play)
* [knight42/synflood-demo](https://github.com/knight42/synflood-demo/tree/master)
