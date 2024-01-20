print("------------Caesar Cipher-----------------")


key = int(input("Enter the key to shift the message: "))
message = input("Enter the message you want to send: ").lower()
def encrypt():
    messages = list(message)
    print(messages)
    cipher = []
    for i in range(0, len(messages)-1):
        text = ord(messages[i])
        cipher[i] = chr(key +text)
    print(text)
    print(cipher)

encrypt()

