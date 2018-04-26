import socket
import sys
import json

GET_SCRIPTS=0
SAVE_PLAY=1

RECV_BUFF=1024

def send_msg(addr, mId):
    msg = json.dumps({'messageID': mId})
    raw = ""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)

    try:
        sock.sendall(msg)

        while True:
            data = sock.recv(RECV_BUFF)
            if len(data) == 0:
                break
            raw += data

    finally:
        sock.close()

    print("Got:\n"+raw)




# Editor modelines - http://www.wireshark.org/tools/modelines.html
#
# Local variables:
# c-basic-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# coding: utf-8
# End:
#
# vi:set shiftwidth=4 tabstop=4 expandtab fileencoding=utf-8:
# :indentSize=4:tabSize=4:noTabs=true:coding=utf-8:
