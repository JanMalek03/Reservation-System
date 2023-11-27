CODE_FORMAT = "utf-8"
HEADER = 64


def send_to(target, msg):
    encoded_msg = msg.encode(CODE_FORMAT)
    message_len = len(encoded_msg)

    encoded_len = str(message_len).encode(CODE_FORMAT)
    encoded_len += b" " * (HEADER - len(encoded_len))

    target.send(encoded_len)
    target.send(encoded_msg)


def recv_from(target):
    message_len = target.recv(HEADER).decode(CODE_FORMAT)
    if not message_len:
        return None
    message_len = int(message_len)

    message = target.recv(message_len).decode(CODE_FORMAT)
    return message
