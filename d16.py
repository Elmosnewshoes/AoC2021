# hexstring = 'D2FE28'
# hexstring = 'EE00D40C823060'
hexstring = '38006F45291200'
def hex2binstring(nmbr):
    return ''.join([f'{str(bin(int(x, 16)))[2:].rjust(4,"0")}' for x in nmbr])

counter = 0

def parse_literal(literal):
    bits = ''
    litlist = list(literal)
    while True:
        start_bit = litlist.pop(0)
        for _ in range(4):
            bits += litlist.pop(0)
        if start_bit == '0':
            return int(bits, 2), ''.join(litlist)


def parse_header(binstring, no_of_packets, counter):
    """
        return version, typeId, remainder
    """
    print(f'Got: ', binstring)
    for i in range(no_of_packets):
        print('Cumsum = ', counter)
        version = int(binstring[:3],2)
        typeId = int(binstring[3:6], 2)
        ltypeid = int(binstring[6])
        new_counter = counter + version
        print(f'Version {version}, type {typeId}')
        if typeId == 4:
            binstring.ljust(4*(len(binstring)//4 + 1), '0')
            counter += version
            print(f'Parsing string literal {binstring[6:]}')
            remainder = binstring[6:]
            print(f'Got left: {remainder}')
            while True:
                number, remainder  = parse_header(remainder, 1, counter)
                print(f'Got number {number}, remaining {remainder}')
                if len(remainder) < 5:
                    break
            print('new counter ', new_counter)
        else:
            if ltypeid == 1:
                print(binstring[7:18])
                remaining_packages = int(binstring[7:18],2)
                binstring = binstring[18:]
                print(f'Got type ID 1, parsing {remaining_packages} packages')
                print(binstring)
                parse_header(binstring, remaining_packages, new_counter)
            else:
                remaining_bits = binstring[7:22]
                splice = (22, int(remaining_bits, 2) + 22)
                deeper_binstring = binstring[splice[0]: splice[1]]
                print(f'Got {remaining_bits} -> {int(remaining_bits, 2)} bits')
                parse_header(deeper_binstring, no_of_packets - i, new_counter)
                binstring = binstring[splice[1]:]

def parse_binstring(binstring):
    ver, tpe, string = parse_header(binstring)
    if tpe == 4:
        lit_value = ''
        while True:
            first_bit = string.pop(0)
            lit_value += string[:4]
            if first_bit == '0':
                break



binstring = hex2binstring(hexstring)
print(parse_header(binstring, 1, 0))
print(counter)
