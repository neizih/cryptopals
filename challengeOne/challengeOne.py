def main(): 
    hex1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

    answ = base64.b64encode(bytes.fromhex(hex1))

    print(answ)

if __name__ == "__main__": 
    main()
