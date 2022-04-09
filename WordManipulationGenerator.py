#Note - Either use the NLTK library below (okay-ish), or download the Enable Word list library from https://www.wordgamedictionary.com/enable/ to work with it

#from nltk.corpus import brown
#english_vocab = set(w.lower() for w in brown.words())

english_vocab=[]
f = open("/home/serkis/code/Python-Programs/words code/enablewordlist.txt", "r")
for x in f:
	english_vocab.append(x.strip())

print(len(english_vocab))

english_vocab2 = set()
for x in english_vocab:
	english_vocab2.add("".join(filter(str.isalpha, x)))

print(len(english_vocab2))

def caesar(word,b):
	 z = "".join(list(map(lambda x: chr(ord(x)+b) if ord(x) + b <=122 else chr(ord(x)+b-26), [char for char in word])))
	 return z

caesarable = []
for x in english_vocab2:
	for i in range(1,26):
		x2 = caesar(x,i)
		if(x2 in english_vocab2 and x<x2):
			caesarable.append((x,x2))

print(len(caesarable))

def atbash(word):
     z = "".join(list(map(lambda x: chr(96+27-(ord(x)-96)), [char for char in word])))
     return z

atbashable = []
for x in english_vocab2:
    x2 = atbash(x)
    if(x2 in english_vocab2 and x<x2):
        atbashable.append((x,x2))

print(len(atbashable))

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def vinegar(text, key):
      cip = []
      start = ord('a')
      key2 = repeat_to_length(key,max(len(key),len(text)))
      for l, k in zip(text, key2):
         shift = ord(k) - start
         pos = start + (ord(l) - start + shift) % 26
         cip.append(chr(pos))
      return ''.join([l for l in cip])

vinegarable = []
for x in english_vocab2:
	x2 = vinegar(x,"keys")
	if(x2 in english_vocab2 and x<x2):
		vinegarable.append((x,x2))

print(len(vinegarable))

for x in vinegarable:
    print(f"{x[0]}\t{x[1]}")


playfairable = []
for x in english_vocab2:
	if(len(x)%2==0):
		x2 = "".join(play_encryption(x.upper(),"KEYS"))
		if(x2.lower() in english_vocab2 and x.upper()<x2):
			playfairable.append((x.upper(),x2))

print(len(playfairable))




piggable = []
for x in english_vocab2:
	if(len(x)>2 and x[-2:]=="ay"):
		piggable.append(x)

print(len(piggable))


list2 = sorted(caesarable, key = lambda x: len(x[1]), reverse = True)

list3 = list(filter(lambda x: x if len(x[0])>=4 else None,list2))

for x in list3:
	print(x[0]+"\t"+x[1])


garb = []
for x in english_vocab2:
	if (len("".join(filter(str.isalpha, x)))<len(x)):
		garb.append(x)

print(len(garb))


def convertPlainTextToDiagraphs (plainText):
    # append X if Two letters are being repeated
    for s in range(0,len(plainText)+1,2):
        if s<len(plainText)-1:
            if plainText[s]==plainText[s+1]:
                plainText=plainText[:s+1]+'X'+plainText[s+1:]
    # append X if the total letters are odd, to make plaintext even
    if len(plainText)%2 != 0:
        plainText = plainText[:]+'X'
    return plainText

def generateKeyMatrix (key): 
    # Intially Create 5X5 matrix with all values as 0
    # [
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0], 
    #   [0, 0, 0, 0, 0]
    # ]
    matrix_5x5 = [[0 for i in range (5)] for j in range(5)]
    simpleKeyArr = []
    """
     Generate SimpleKeyArray with key from user Input 
     with following below condition:
     1. Character Should not be repeated again
     2. Replacing J as I (as per rule of playfair cipher)
    """
    for c in key:
        if c not in simpleKeyArr:
            if c == 'J':
                simpleKeyArr.append('I')
            else:
                simpleKeyArr.append(c)
    """
    Fill the remaining SimpleKeyArray with rest of unused letters from english alphabets 
    """
    is_I_exist = "I" in simpleKeyArr
    # A-Z's ASCII Value lies between 65 to 90 but as range's second parameter excludes that value we will use 65 to 91
    for i in range(65,91):
        if chr(i) not in simpleKeyArr:
            # I = 73
            # J = 74
            # We want I in simpleKeyArr not J
            if i==73 and not is_I_exist:
                simpleKeyArr.append("I")
                is_I_exist = True
            elif i==73 or i==74 and is_I_exist:
                pass
            else:
                simpleKeyArr.append(chr(i))
    """
    Now map simpleKeyArr to matrix_5x5 
    """
    index = 0
    for i in range(0,5):
        for j in range(0,5):
            matrix_5x5[i][j] = simpleKeyArr[index]
            index+=1
    return matrix_5x5

kmm


def indexLocator (char,cipherKeyMatrix):
    indexOfChar = []
    # convert the character value from J to I
    if char=="J":
        char = "I"
    for i,j in enumerate(cipherKeyMatrix):
        # enumerate will return object like this:         
        # [
        #   (0, ['K', 'A', 'R', 'E', 'N']),
        #   (1, ['D', 'B', 'C', 'F', 'G']), 
        #   (2, ['H', 'I', 'L', 'M', 'O']), 
        #   (3, ['P', 'Q', 'S', 'T', 'U']), 
        #   (4, ['V', 'W', 'X', 'Y', 'Z'])
        # ]
        # i,j will map to tupels of above array
        # j refers to inside matrix =>  ['K', 'A', 'R', 'E', 'N'],
        for k,l in enumerate(j):
            # again enumerate will return object that look like this in first iteration: 
            # [(0,'K'),(1,'A'),(2,'R'),(3,'E'),(4,'N')]
            # k,l will map to tupels of above array
            if char == l:
                indexOfChar.append(i) #add 1st dimension of 5X5 matrix => i.e., indexOfChar = [i]
                indexOfChar.append(k) #add 2nd dimension of 5X5 matrix => i.e., indexOfChar = [i,k]
                return indexOfChar              
            # Now with the help of indexOfChar = [i,k] we can pretty much locate every element,
            # inside our 5X5 matrix like this =>  cipherKeyMatrix[i][k]

def play_encryption (plainText,key):
    cipherText = []
    # 1. Generate Key Matrix
    keyMatrix = generateKeyMatrix(key)
    # 2. Encrypt According to Rules of playfair cipher
    i = 0
    while i < len(plainText):
        # 2.1 calculate two grouped characters indexes from keyMatrix
        n1 = indexLocator(plainText[i],keyMatrix)
        n2 = indexLocator(plainText[i+1],keyMatrix)
        # 2.2  if same column then look in below row so
        # format is [row,col]
        # now to see below row => increase the row in both item
        # (n1[0]+1,n1[1]) => (3+1,1) => (4,1)
        # (n2[0]+1,n2[1]) => (4+1,1) => (5,1)
        # but in our matrix we have 0 to 4 indexes only
        # so to make value bound under 0 to 4 we will do %5
        # i.e.,
        #   (n1[0]+1 % 5,n1[1])
        #   (n2[0]+1 % 5,n2[1])
        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 5
            j1 = n1[1]
            i2 = (n2[0] + 1) % 5
            j2 = n2[1]
            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
        # same row
        elif n1[0]==n2[0]:
            i1= n1[0]
            j1= (n1[1] + 1) % 5
            i2= n2[0]
            j2= (n2[1] + 1) % 5
            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
        # if making rectangle then
        # [4,3] [1,2] => [4,2] [3,1]
        # exchange columns of both value
        else:
            i1 = n1[0]
            j1 = n1[1]
            i2 = n2[0]
            j2 = n2[1]
            cipherText.append(keyMatrix[i1][j2])
            cipherText.append(keyMatrix[i2][j1])
        i += 2  
    return cipherText

import itertools

nearby_letters = {
    "q": "was",
    "w": "qeas",
    "e": "wrsd",
    "r": "etdf",
    "t": "ryfg",
    "y": "tugh",
    "u": "yihj",
    "i": "uojk",
    "o": "ipkl",
    "p": "ol",
    "a": "qwszx",
    "s": "weadzx",
    "d": "esfxc",
    "f": "rdgcv",
    "g": "tyfhvb",
    "h": "ygjbn",
    "j": "uihknm",
    "k": "iojlm",
    "l": "opk",
    "z": "asx",
    "x": "zsdc",
    "c": "xdfv",
    "v": "cfgb",
    "b": "vghn",
    "n": "bhjm",
    "m": "njk",
}

word = "word"



swiftable = []
i=0
for wordx in english_vocab2:
    if(i%10000==0):
        print(i)
    #print(wordx)
    #print(type(wordx))
    #print(len(wordx))
    if(len(wordx) > 5 and len(wordx) < 8 ):
        listw = [[x for x in nearby_letters[char]] for char in wordx]
        for x in itertools.product(*listw):
            x2 = "".join(x)
            if(x2 in english_vocab2 and wordx<x2):
                swiftable.append((wordx,x2))
    i=i+1

print(len(swiftable))



list2 = sorted(swiftable, key = lambda x: len(x[1]), reverse = True)



base36able = []
for word in english_vocab2:
	wordbase36 = "one"+word
	num = int(wordbase36,36)
	flg = True
	for i in str(num):
	    if(i>'6' or i<='0'):
	        flg = False
	if(flg):
		base36able.append((wordbase36,num))

print(len(base36able))

reversible= []
palinable = []
for x in english_vocab2:
	x2 = x[::-1]
	if(x2 in english_vocab2):
		if(x==x2):
			palinable.append(x)
		elif(x<x2):
			reversible.append((x,x2))

print(len(palinable))
print(len(reversible))

for i in base36able:
     print(i[0]+"\t"+str(i[1]))
