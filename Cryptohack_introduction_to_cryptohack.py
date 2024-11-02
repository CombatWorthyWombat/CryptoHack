"""challenge 1 - run the script"""
import sys

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("here is your flag for challenge 1:")
print("".join(chr(o ^ 0x32) for o in ords))

"""challenge 2 - print the following numbers in ASCII,"""
"""ord() prints input as ordinals"""
"""chr() prints input as ASCII string"""

print("here is your flag for challenge 2:")

ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
challenge2 = []
for i in ords:
    challenge2.append(chr(i))

"""prints the appended list with the criteria: seperate items in the list with what is between the quotes, which in this case is nothing"""
print(*challenge2, sep = "")

"""challenge 3 - the following hex is an encoded flag, print into bytes"""
"""bytes.fromhex() is used to convert input hex to output bytes"""
""".hex() is used to convert bytes to hex"""

challenge3hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print("here is your flag for challenge 3:")
print(bytes.fromhex(challenge3hex))

"""challenge 4 - decode the following hex into bytes, then into base64"""
"""import the base64 module using; import base64"""
"""the base64.b64encode() function is used to encode from hex to b64"""
"""base64.b64decode() is the reverse function"""

import base64
challenge4hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
challenge4bytes = (bytes.fromhex(challenge4hex))
print("here is your flag for challenge 4:")
print(base64.b64encode(challenge4bytes))

"""challenge 5 - RSA"""
"""often there are text messages we want to encode using matematical operations"""

"""for instance, the message: HELLO"""
"""ascii bytes: [72, 69, 76, 76, 79]"""
"""hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]"""
"""base-16: 0x48454c4c4f"""
"""base-10: 310400273487"""

"""yourbytes.to_int() converts a byte string to a long integer"""
"""yourint.to_bytes() converts a long integer to a byte string"""

C5int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

"""add 7 to make sure each byte is 'full', then divide by 8 and discard the remainder to find the number of bytes this int represents"""
C5bytelength = (C5int.bit_length() + 7)//8
print("here is your flag for challenge 5")
"""this prints the bytes as their ascii representation"""
print(C5int.to_bytes(C5bytelength, byteorder='big'))

"""XOR operations act on binary digits, denoted by the symbol: ⊕"""
"""when XORing anything other than binary, we need to convert to binary first"""

C61 = 13
C62 = 'label'


"""convert both to binary data"""

"""with integers, we can use the bin(int) function, it will append the binary with '0b'"""

binaryC61 = bin(C61)

"""when using strings, we first store each character as its ordinal in a variable"""

ordC62 = ' '.join(format(ord(char)) for char in C62)

"""next we split all the ordinals into individual ascii code pieces for the bin() function to work on"""

ascii_codes = ordC62.split()
binaryC62 = ' '.join(bin(int(code)) for code in ascii_codes)

"""now we XOR each character of our string, with the binary for 13"""
"""so our operation looks like:"""
"""'l' ⊕ '13' """
"""'a' ⊕ '13' """
"""'b' ⊕ '13' """
"""'e' ⊕ '13' """
"""'l' ⊕ '13' """

"""an example operation would be for 'l'"""
"""the '^' operator is used for XOR"""
"""the '^' operator only works on integers  """
"""int(1101100) ^ int(1101)"""

"""instead of converting from binary up to integer, we can just int() the origional inputs - which we named ordC62"""

"""here we initialize the variable we will call later"""
XORresults = []
"""we turn the list into a list of integers (as before it was technically a string with spaces between)"""
ordC62list = [int(num) for num in ordC62.split()]
"""iterate through each number in the list, and XOR it with 13. we append that to a variable called XORresults"""
for integer in ordC62list:
    result = integer ^ C61
    XORresults.append(result)

"""we now iterate through our results, and do the chr() operation on each one"""
character_results = ' '.join(chr(result) for result in XORresults)
print("here is your flag for challenge 6")
print("crypto{",(character_results),"}")

"""there are 4 main properties of the XOR operation that are key to understand"""
"""Commutative: A ⊕ B = B ⊕ A"""
"""Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C"""
"""Identity: A ⊕ 0 = A"""
"""Self-Inverse: A ⊕ A = 0 """

"""the order of the XOR operation is important, we can only undo it if we know the initial order and reverse it. Unlike say, multiplication and division"""

"""the following is a series of operations with XOR"""
"""three random keys have been XORed with the flag, try and get the flag"""

#KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
#KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
#KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
#FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

key1b = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key1XORkey2b = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
key2XORkey3b = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flagXORkey1XORkey3XORkey2b = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

"""key1 ^ key2 = x where x and key1 is known"""
"""∴ by commutative identity key2 = key1 ^ x"""

"""the zip() function is used to combine lists. it combines the first items in the list, and the second and so on"""
"""x_coords = [1, 2, 3, 4, 5]"""
"""y_coords = [5, 4, 3, 2, 1]"""
"""print(sip(x_coords, y_coords)) -> [(1, 5), (2, 4), (3, 3), (2, 4), (1, 5)]"""
"""we use it here because each 'byte' in the list is considered its own item in a list, on which we XOR"""

key2b = bytes([b1 ^ b2 for b1, b2 in zip(key1b, key1XORkey2b)])

key3b = bytes([b1 ^ b2 for b1, b2 in zip(key2b, key2XORkey3b)])

"""we now have all 3 keys"""
"""the flag has been XORed with key1, then key3, then key2"""
"""to undo this, we take the result we have, and XOR it with key2, then key3, then key1"""

C7flag = bytes([
    b ^ k2 ^k3 ^ k1
    for b, k2, k3, k1 in zip(flagXORkey1XORkey3XORkey2b, key2b, key3b, key1b)
])
print("""here is your flag for challenge 7""")
print(C7flag)

#For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles
#I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first

#73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

C8encodedflag = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

"""we need to write something that will iterate through a bunch of different bytes"""
"""and perform the XOR operation on every byte in the encoded flag"""
"""we know the format is: crypto{FLAG}, so we stop the iteration once we acheive a byte list that reads 'crypto' in ascii"""

"""somehow we code the following:"""

#initialize the byte guess as 00000000

#while result doesn't start with 'crypto':
    #XOR each byte with byte guess
    #if result in ascii starts with crypto, exit loop and print
    #else
        #add 1 to the byte guess

byte_guess = 0

"""bytes can range from 0 to 255"""

while byte_guess <= 255:
    C7result = bytes([b ^ byte_guess for b in C8encodedflag])

    try:
        C7result_string = C7result.decode('ascii')
    except UnicodeDecodeError:
        bute_guess += 1
        continue

    if C7result_string.startswith('crypto'):
        print("here is your flag for challenge 8")
        print("found flag", C7result_string, "with byte guess", byte_guess)
        break
    else:
        byte_guess += 1

if byte_guess > 255:
    print("no flag found in byte range")

#I've encrypted the flag with my secret key, you'll never be able to guess it
#0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

"""find the key and decrypt the message using XOR"""
"""the decrypted text will be in the format: crypto{flag}"""

C9encryptedflag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
"""crypto{ is 7 chars long, so will have 7 bytes that XORed to those ascii chars"""
C9trimmed_flag = C9encryptedflag[:7]

"""we know that:"""
"""trimmed_flag ^ key = 'crypto{', so trimmed_flag ^ 'crypto{' = key"""

C9target = "crypto{"
cryptobytes = C9target.encode('utf-8')
C9keytrimmed = bytes(b1 ^ b2 for b1, b2 in zip(C9trimmed_flag, cryptobytes))

"""printing the key reveals: 'myXORke' in ascii"""
"""we can guess that the full key is 'myXORkey' and try it on the untrimmed flag"""

C9key_str = "myXORkey"
C9key_bytes = C9key_str.encode('utf-8')
C9flagtrimmed = bytes(b1 ^ b2 for b1, b2 in zip(C9encryptedflag, C9key_bytes))

"""print(C9flag) gives us only 2 more letters of the flag, we need a byte to byte conversion"""
"""try using myXORkeymyXORkeymyXORkey... etc to match the number of bytes in the encrypted flag"""

"""using:"""
#print(len(C9encryptedflag))
"""we find that the length of the encrypted flag is 42 bytes"""
"""now we need a repeated 'myXORkey' that is 42 bytes long"""

C9fullkey = ""
while len(C9fullkey) < 42:
    C9fullkey += "myXORkey"
C9fullkey = C9fullkey[:42]  # Trim to ensure exactly 42 characters

"""now we convert from str to bytes"""

C9fullkey_bytes = C9fullkey.encode('utf-8')

C9flag = bytes(b1 ^ b2 for b1, b2 in zip(C9encryptedflag, C9fullkey_bytes))

print("here is your flag for challenge 9")
print("the flag is", C9flag, "encoded with the key", C9fullkey_bytes)
