import hashlib

while True:
    data = input("Digite algo para ser mascarado: ")
    hash_object = hashlib.sha1(data.encode())
    hex_dig = hash_object.hexdigest()

    print(hex_dig)
