alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Making different functions for encrypt and decrypt the text 
# def encrypt(plain_text,shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position= position+shift_amount
#         new_letter=alphabet[new_position]
#         cipher_text+= new_letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text,shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         new_position= position-shift_amount
#         plain_text+=alphabet[new_position]
#     print(f"The decoded text is {plain_text}")


# if direction=="encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction=="decode":
#     decrypt(cipher_text=text,shift_amount=shift)




# there is one function for encrypt and decrypt the text 
def ceaser(cipher_direction,start_text,shift_amount):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in start_text:

        if char in alphabet:

            position=alphabet.index(char)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {cipher_direction}d text is {end_text}")
    


logo = """           
 ,dSSSBba, ,dSSSSba,  ,dSSSBba, ,dSSSBba, ,dSSSSba, 8e,dSSSSba,  
e8"     "" e"     "8 e8S_____88 I8[    "" e"     "8 88e'       ,8 
8e         ,SSSSSSS88 8SS"""""""  `"Y8ee, ,SSSSSSS88 88         88 
"8a,   ,aa 88,    ,88 "8a,   ,aa aa    ]8I 88,    ,88 88         
 `"YSSSSSP" `"SSSSS"Y8  `"SSSSSY" `"YeeP"' `"SSSSS"Y8 88     
            88             88                                 
           ""             88                                 
                          88                                 
 ,dSSSSSS, 88 8e,dSSSSSS,  88,dSSSSSS,   ,dSSSSSS, 8e,dSSSSSS,  
e8"     "8 88 88e'    `88 88e'    `88 e8S_____88 88e'       ,8  
8e         88 88       88 88       88 8SS""""""" 88         
"8a,   ,aa 88 88b,   ,a8" 88       88 "8a,   ,aa 88         
 `"YSSSSSP" 88 88`SSSSSY"  88       88  `"SSSSSP" 88         
              88                                             
              88
 
"""
print(logo)

should_end=True
while should_end:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt : \n ") 
    text =input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    shift=shift%26

    ceaser(start_text=text,cipher_direction=direction,shift_amount=shift)


    restart=input("Type 'yes' if you want to go again. otherwise type 'no' \n")
    if restart=="no":
        should_end=False
        print("Goofbye")
            
    