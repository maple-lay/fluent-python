import struct

if __name__ == '__main__':
    fmt = '<3s3sHH'
    with open("test.gif", "rb") as fp:
        img = memoryview(fp.read())

    header = img[:10]
    print(bytes(header))
    anc = struct.unpack(fmt, header)
    print(anc)
    del header
    del img
