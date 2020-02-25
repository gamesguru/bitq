import socket

import miniupnpc

upnp = miniupnpc.UPnP()
upnp.addportmapping(8333, "TCP", "192.168.0.2", 8333, "coin-port", "")
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
