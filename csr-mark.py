#!/usr/bin/python

# Copyright 2013, Verisign, Inc

import os
import sys
import json
import socket
import logging
import argparse
import xmlrpclib

from cobblerutil import Cobbler

SERVER_FIELDS = ['name', 'hostname', 'netboot_enabled', 'profile']
INTERFACE_FIELDS = ['mac_address', 'ip_address', 'netmask']
# This needs to be fixed for datacenter sites too

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

def main(hosts=None, cobbler=None, netboot=False, verbose=False):
    """
    Connect to Cobbler and return the contents of one or more hostnames!
    """
    cobbler = Cobbler(cobblers=cobbler)

    hosts = list(hosts)
    for hostname in hosts:
        try:
            host = cobbler.get_host(hostname)
        except ValueError:
            print "[ERROR] {h} not found.".format(h=hostname)
            continue

        if verbose:
            print json.dumps(host, indent=4)
            continue

        print ""
        title = " {h} (from: {c}) ".format(h=hostname, c=cobbler.cobbler_name)
        print "{t:*^50}".format(t=title)

        for key in SERVER_FIELDS:
            show_field(host, field=key, value=host.get(key, ''))

        for interface_name in host.get('interfaces', list()):
            interface = host['interfaces'][interface_name]

            for field in INTERFACE_FIELDS:
                field_name = "{i}-{f}".format(i=interface_name, f=field)
                show_field(host, field_name, interface.get(field, ''))

    # Print an extra line at the end of the output to make it a little easier to read
    print ""

def show_field(host, field, value):
    """
    Ensure that all output has the same format by putting it in a single place.
    """
    print "{k:25} : {v}".format(
        k=field,
        v=value,
    )
    return


def list_servers(netboot_only=False, verbose=False):
    """
    List hosts known by the Cobbler server
    """
    hosts = list()
    host_count = 0
    cobbler = Cobbler()

    if netboot_only:
        host_list = cobbler.find_systems({"netboot_enabled": "true"})
    else:
        host_list = cobbler.list_systems()

    if host_list is None:
        print "No server defined on {c}".format(c=cobbler)
        sys.exit()

    for host in host_list:
        # We get a dictionary for all systems list and a list for find requests
        if type(host) is dict:
            hosts.append(host.get('name', ''))
        elif type(host) is str:
            hosts.append(host)
        else:
            print "[ERROR] Unable to process {h}".format(h=host)

    for s in sorted(hosts):
        print s

    print ""
    print "Total systems:", len(hosts)
    sys.exit(0)


def full_json(host=None):
    """
    Perform a complete dump of all information known by the Cobbler server.

    Be warned, this generates an awful lot of output!
    """
    cobbler = Cobbler()
    host_details = cobbler.get_host(host)
    print json.dumps(host_details, indent=4)
    return


###############################################################################
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Query information from a cobbler server'
    )
    parser.add_argument(
        '-l', '--list',
        dest='list', action='store_true', default=False,
        help='List all servers known by the cobbler server',
    )
    parser.add_argument(
        '-n', '--netboot',
        action='store_true', default=False, required=False,
        help='When listing servers, only show the netboot enabled hosts',
    )
    parser.add_argument(
        '-j', '--json',
        action='store_true', default=False, required=False,
        help='Get and return ALL configuration data known by Cobbler',
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        default=False, required=False,
        help='Show all the fields, instead of just the short version',
    )
    parser.add_argument(
        '-c', '--cobbler', nargs='?',
        dest='cobbler', default=None,
        help='Use specific cobbler box instead of defaults',
    )
    parser.add_argument(
        'hostname',  help='hostname',
        nargs=argparse.REMAINDER
    )

    args = parser.parse_args()

    if args.json:
        full_json(host=args.hostname[0])
        sys.exit(0)

    if args.list:
        list_servers(netboot_only=args.netboot, verbose=args.verbose)
        sys.exit(0)

    main(
        hosts=args.hostname,
        netboot=args.netboot,
        cobbler=args.cobbler,
        verbose=args.verbose,
    )
