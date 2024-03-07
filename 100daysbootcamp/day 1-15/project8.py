# This can be solved by two method
# one by traditional calculation
# suppose [a-z] equals each of their correspondence [0-25]
# and calculating their values
# eg: for message ='ab' having key = 3
# it's cipher text will 'de' by calculation i.e. a = 0, b=1
# encryption = 0+3, 1+3 which is 3,4 ie their correspondence letters are de


# another method is by using ascii code where all text is converted into lower or upper and their correspondance 
# ascii value is calculated with key value
#suppose for message ='AB' having key = 3
#it's cipher text will be 'DE' by calculation ie. a= 65, b= 66
#encryption text = 65+3, 66+3 which is 68, 69 and their correspondance ascii code is 'DE'

print("------------Caesar Cipher-----------------")


key = int(input("Enter the key to shift the message: "))
message = str(input("Enter the message you want to send: "))
message.lower()
messages = list(message)
length = len(message)
def encrypt():
    

    cipher = []
    for i in range(length):
        
        text = ord(messages[i]) #converting  string into ascii unicode eg: A = 65
        sum = (key +text)
        cipher +=chr(sum)
    print(cipher)

def decrypt():
    # if encrypt()==True:
    plainText = []
    for i in range(length):
        text = ord(messages[i])
        sub = text - key
        plainText += chr(sub)
    print(plainText)

choice = input("""Do you Want to encode(E) or decode(D) message?
               Enter E for Encoding or D for Decoding the message: """).lower()
        
if choice=="e":
    encrypt()
elif choice =='d':
    decrypt()
else:
    print("Wrong Input!! Please try again.....")





# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
#           'X','Y','Z','A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
#           'X','Y','Z' ]
# letters.lower()
# key = int(input("Enter the key to shift the message: "))
# message = str(input("Enter the message you want to send: "))

# def caesar(key, message, direction):
#     end_text = ''
#     if direction=='d':
#         key *= -1
# for letter in message:
#     position = letters.index(letter)
#     new_position = position + key
#     end_text += letters[new_position]
#     print(f"The {direction}d message is: {end_text}")


# caesar(key, message, choice)
