n = 0x00111111

if n & 0xff:
    print('little endian')
    print(0xff)

else:
    print('big endian')