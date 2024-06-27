import socket


def get_pc_name():
    pc_name = socket.gethostname()
    return pc_name