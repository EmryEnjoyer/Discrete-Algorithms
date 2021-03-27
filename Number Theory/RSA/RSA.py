import betterPrimeGeneration

letterSerialization = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
    " ":26,
    '-':27
}

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
    msg = msg.lower()
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

            if(letterSerialization.get(c) < 10):
                messageArray[i] = messageArray[i].replace(c, "0" + str (letterSerialization.get(c)))
            else:
                messageArray[i] = messageArray[i].replace(c, str(letterSerialization.get(c)))
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
        if len(s) < blockLength * 2:
            s = '0' + s
        decryptedIntegers.append(s)
    msg = ""
    for s in decryptedIntegers:
        msg += s
    decrypted = ""
    letters = list(letterSerialization.keys())
    for i in range(0,len(msg),2):
        decrypted += letters[int (msg[i:i+2])]
    return decrypted.replace('-', "")

def findBlockSize(n):
    print("Finding the block size for", n)
    num = "27"
    while(int(num+"27") <= n):
        num += "27"
    print("The block size is", int(len(num)/2), "\n")
    return int (len(num)/2)



p = betterPrimeGeneration.generatePrime(1024);
q = betterPrimeGeneration.generatePrime(1024);
pwr = betterPrimeGeneration.generateCoPrime((p-1) * (q-1));
r = findInverse(pwr, (p-1)*(q-1))

message = input("Input your secret message: ")

cryptoText = generateCrypto(message, [p*q, pwr])
print("The encrypted text is", cryptoText, "\n")
print(decrypt(cryptoText, p, q, r))