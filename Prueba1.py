# Caesar cipher
# Notes: ord is for retrieving ascii value of character and with char we add then the number of pos we want to add
while True:
    inputText = input("Enter your text to cipher: ")
    cipheredText = ""
    if inputText != "exit":
        for x in inputText:
            if ord(x)>96 and ord(x)<119:
                x = chr(ord(x)+4) #we add for positions in the char (ascii value)
                cipheredText = cipheredText + x
            elif ord(x)>118 and ord(x)<123:
                x = chr(ord(x)-22)
                cipheredText = cipheredText + x
    else:break
    print("Text ciphered: " + cipheredText)
