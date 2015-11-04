def toString(values):
    temp = ''
    for value in values:
        if value is not "00":
            temp += value.decode('hex')
    return temp


def toInt(values):
    i = len(values)
    temp = 0
    for value in values:
        i -= 1
        weight = 256 ** i
        temp += int(value, 16) * weight
    return temp


def toIp(values):
    ip = ''
    for temp in values:
        ip += str(int(temp, 16))
        ip += '.'
    return ip[: -1]


def toTime(value):
    temp = base_time + datetime.timedelta(seconds=toInt(value))
    return temp.strftime('%Y-%m-%d %H:%M:%S')


def toFloat(values):
    temp = ''
    if len(values) < 4:
        values = ['00' for i in range(4 - len(values))] + values
    for value in values:
        temp += value
    return str(struct.unpack('f', temp.decode('hex'))[0])


def checkCRC(message):
    u8MSBInfo = 0x00
    u16CrcData = 0xffff
    for data in message:
        u16CrcData = u16CrcData ^ int(data, 16)
        for i in range(8):
            u8MSBInfo = u16CrcData & 0x0001
            u16CrcData = u16CrcData >> 1
            if u8MSBInfo != 0:
                u16CrcData = u16CrcData ^ 0xA001
    return int_to_hex(u16CrcData, 2)


def crc16(x):
    b = 0xA001
    a = 0xFFFF
    for byte in x:
        a = a ^ int(byte, 16)
        for i in range(8):
            last = a % 2
            a = a >> 1
            if last == 1:
                a = a ^ b
    aa = '0' * (6 - len(hex(a))) + hex(a)[2:]
    return aa
# CONFIG_FRAME


def int_to_hex(para, length):
    result = []
    temp = []
    data = str(format(para, 'x'))
    if (len(data)) < 2 * length:
        for i in range(2 * length - len(data)):
            data = '0' + data
    for i in range(len(data) / 2):
        result.append(data[2 * i: 2 * i + 2])
    distance = length - len(result)
    if distance != 0:
        temp = ['00' for n in range(distance)]
    return temp + result


def str_to_hex(para, length):
    result = []
    temp = []
    data = para.encode('hex')
    result = [data[2 * i: 2 * i + 2] for i in range(len(data) / 2)]
    distance = length - len(result)
    if distance != 0:
        temp = ['00' for i in range(distance)]
    return result + temp
