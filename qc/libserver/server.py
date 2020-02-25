import socket

import miniupnpc

u = miniupnpc.UPnP()
u.discoverdelay = 200
# u.minissdpdsocket = '../minissdpd/minissdpd.sock'
# discovery process, it usually takes several seconds (2 seconds or more)
print("Discovering... delay=%ums" % u.discoverdelay)
print(u.discover(), "device(s) detected")
# select an igd
u.selectigd()
print(u.statusinfo(), u.connectiontype())
# print u.addportmapping(64000, 'TCP',
#                       '192.168.1.166', 63000, 'port mapping test', '')
# print u.deleteportmapping(64000, 'TCP')
port = 0
proto = "UDP"
# list the redirections :
i = 0
while True:
    p = u.getgenericportmapping(i)
    if p == None:
        break
    print(i, p)
    (port, proto, (ihost, iport), desc, c, d, e) = p
    # print port, desc
    i = i + 1
u.addportmapping(8333, "TCP", "192.168.0.2", 8333, "coin-port", "")

#########
# Connect
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind(("0.0.0.0", 8333))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = bytes()
    conn.send(b"[Server] begin transfer")
    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client += data
    conn.send(b"[Server] received data: %a" % len(from_client))
    print("received data: %a" % len(from_client))
    conn.close()
    print("client disconnected")
