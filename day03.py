


def caeser():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    original_text=input("type your message\n")
    encode_or_decode=input("type 'encode' to encrypt and 'decode' to decrypt\n")
    shift_amount=int(input("type the number of shifts\n"))

                   
        
    
    decode_text=""
    if encode_or_decode=="decode":
            shift_amount*=-1
    for letter in original_text:
        if letter not in alphabets:
            decode_text+=letter

        
        
            
        shifted_position=alphabets.index(letter)+shift_amount
        shifted_position%=len(alphabets)
        decode_text+=alphabets[shifted_position]
    print(f"here is your {encode_or_decode}d message :{decode_text}")
caeser()
restart=True
while restart:
    ask=input("type 'yes' to continue or type 'no' to exit\n")  
    if ask=="yes":
        caeser()
    else:
        restart=False
        print("goodbye")

    
