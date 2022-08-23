
# A five-byte sequence as bytes and as bytearray
cafe = bytes('café', encoding='utf_8')
cafe  # b'caf\xc3\xa9'
cafe[0]  # 99
cafe[:1]  # b'c'

cafe_arr = bytearray(cafe)
cafe_arr  # bytearray(b'caf\xc3\xa9')
cafe_arr[-1:]  # bytearray(b'\xa9')


# building sequence using hex
seq = bytes.fromhex('31 4B CE A9')
seq.decode('utf_8')

# Initializing bytes from the raw data of an array
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])

octets = bytes(numbers)

print(octets.decode('utf-16'))