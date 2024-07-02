def to_binary(n):
    
    """

    description:
        converts decimal to binary
    
    parameters:
        n (decimal) : number which we want to represent/convert into binary
    
    return:
        padded_binary_str

    """

    if n == 0:
        return '0' * 32 
    
    binary_str = ''
    
    while n > 0:

        bit = '1' if n % 2 == 1 else '0'
        binary_str = bit + binary_str
        n //= 2
    
    padded_binary_str = binary_str.zfill(8)
    
    return padded_binary_str

binary_number = to_binary(135)
print(binary_number)

def swap_nibbles(binary_number):

    """

    description:
        swaps the nibbles of the converted binary string
    
    parameters:
        binary (binary number): the converted binary passed an argiument
    
    return:
        None

    """

    swap_nibbles = binary_number[4::] + binary_number[0:4:] 
    print(swap_nibbles)

function2=swap_nibbles(binary_number)
