hexstring = 'D2FE28'
# hexstring = 'EE00D40C823060'
hexstring = '38006F45291200'
def hex2binstring(nmbr):
    return ''.join([f'{str(bin(int(x, 16)))[2:].rjust(4,"0")}' for x in nmbr])

counter = 0

def parse_literal(literal):
    bits = ''
    literal = literal.ljust(4 * (len(literal) // 4 + 1), '0')
    print(f'Parsing {literal} to number')
    litlist = list(literal)
    while True:
        start_bit = litlist.pop(0)
        for _ in range(4):
            bits += litlist.pop(0)
        if start_bit == '0':
            return int(bits, 2), ''.join(litlist)


def parse_bitstring(bitstring, n = 1, version_sum = 0):
    if n == 0:
        return version_sum
    elif n > 0:
        n-= 1

    typeId = int(binstring[3:6], 2)
    version = int(binstring[:3], 2)
    print(f'TypeId = {typeId}, version {version}, from {bitstring}')
    bitstring = bitstring[6:]
    if typeId == 4:
        nmbr, remainder = parse_literal(bitstring)
        if int(remainder, 2) == 0 and n <= 0:
            n = 0
        print(f'Got {nmbr}, remaining = {remainder}')
        return parse_bitstring(remainder, n, version_sum + version)

    ltypeId, bitstring = (int(bitstring[0]), bitstring[1:])
    if ltypeId == 0:
        bitslength = int(bitstring[:15], 2)
        bitstring = bitstring[15:]
        print(f'Parsing next {bitslength} packets')
        print(f'Parsing string {bitstring[:bitslength]}')
        return parse_bitstring(bitstring[:bitslength], 1, version_sum
                               + version)
    else:
        packets = int(bitstring[:11], 2)
        bitstring = bitstring[11:]
        return parse_bitstring(bitstring, packets, version_sum + version)




def parse_header(binstring, no_of_packets, counter):
    """
        return version, typeId, remainder
    """
    print(f'Got: ', binstring)
    for i in range(no_of_packets):
        print('Cumsum = ', counter)
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




binstring = hex2binstring(hexstring)
# binstring = '1101000101001010010001001000000000'
# binstring = '11010001010'
print(parse_bitstring(binstring, -1, 0))

# print(parse_header(binstring, 1, 0))
# print(counter)
