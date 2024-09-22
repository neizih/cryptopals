def main(): 
    encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    key = 0
    result = ""

    hex_byte = bytes.fromhex(encoded)

    while(key <= 255):
        for x in hex_byte: 
            seq = x ^ key
            result += chr(seq)

        print(key, result, end="\n")
        key += 1
        result = ""

if __name__ == "__main__": 
    main()
