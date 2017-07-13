# Convert IP address, e.g. 192.168.1.1 to hex string, two hex numbers per octet (e.g. c0a80101)


def convert_ip(ip):
    """
    >>> convert_ip("255.255.255.255")
    'ffffffff'
    >>> convert_ip("192.168.1.1")
    'c0a80101'
    """
    return ''.join('{:02x}'.format(int(oct)) for oct in ip.split('.'))
