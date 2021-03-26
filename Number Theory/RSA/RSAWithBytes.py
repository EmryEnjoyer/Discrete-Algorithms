import PrimeGenerator

def fastExponentiation(base, exponent, mod):
    if(mod == 1):
        return 0;
    result = 1;
    base = base % mod;
    while exponent > 0:
        if(exponent % 2 == 1):
            result = result * base % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result;

def findInverse(a, b):
    t = 0;
    newt = 1
    r = b;
    newr = a;

    # GCD algorithm, r is the GCD. t is the bezout coefficient we need since we don't care about the bezout coefficeint of the modulus.
    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r-quotient * newr)

    if r > 1:
        #a is not reversible mod b
        return None
    if t < 0:
        t = t + b

    return t
#Where msg represents the message to send, key represents the ordered pair of the key and modulus.
def generateCrypto(msg="", key=[]):
    # Split the message into character strings
    print("Splitting the message...")
    messageArray = []
    n = findBlockSize(key[0])
    while(len(msg) % n != 0):
        msg += '-'
    for i in range(0,len(msg), n):
        messageArray.append(msg[i:i+n])
    print("Serializing the characters...")
    for i in range(0,len(messageArray)):
        for c in messageArray[i]:
            char = ord(c)
            if(char < 100):
                messageArray[i] = messageArray[i].replace(c, "0" + str (char))
            else:
                messageArray[i] = messageArray[i].replace(c, str(char))
    print("Encrypting the characters using the public encryption key...")
    for i in range(0, len(messageArray)):
        messageArray[i] = fastExponentiation(int(messageArray[i]), key[1], key[0])
    return messageArray;

def decrypt(msgBlock = [], p=0, q=0, d=0):
    decryptedIntegers = []
    blockLength = findBlockSize(p * q)
    for i in msgBlock:
        s = fastExponentiation(i, d, p*q)
        s = str (s)
        if len(s) < blockLength * 3:
            s = '0' + s
        decryptedIntegers.append(s)
    msg = ""
    for s in decryptedIntegers:
        msg += s
    decrypted = ""
    print("The decrypted integer text is", msg)
    for i in range(0,len(msg),3):
        decrypted += chr(int(msg[i:i+3]))
    return decrypted.replace('-', "")

def findBlockSize(n):
    print("Finding the block size for", n)
    num = "127"
    while(int(num+"127") <= n):
        num += "127"
    print("The block size is", int(len(num)/3), "\n")
    return int (len(num)/3)



p = PrimeGenerator.generatePrime();
q = PrimeGenerator.generatePrime();
pwr = PrimeGenerator.generateCoPrime((p-1) * (q-1));
r = findInverse(pwr, (p-1)*(q-1))

message = input("Input your secret message: ")

cryptoText = generateCrypto(message, [p*q, pwr])
print("The encrypted text is", cryptoText, "\n")
print("The decrypted text is", decrypt(cryptoText, p, q, r))