#function for all anagrams
def b_anagram():
    openfile = open("eng_dict.txt", 'r')
    #Open and read the file
    words = openfile.read().splitlines()
    anagram_proto = {}
    anagrams = {}
    for word in words:
        #sets length of words = 8
        if len(word) >= 8:
            letters = word.lower()
            word = word.lower()
            #sorts letters in word by alphabetical order
            letters = ''.join(sorted(letters))
            #add new dictionary if one doesn't exist
            if not (letters in anagram_proto):
                anagram_proto[letters] = [word]
            else:
                new = True
                #if the word is already there don't add it to anagram_proto dictionary
                for i in anagram_proto[letters]:
                    if i == word:
                        new = False
                #if the word is new, add it to anagram_proto dictionary
                if new:
                    anagram_proto[letters].append(word)
    for letters in anagram_proto:
        #if there are more than 1 word as an anagram, append to anagrams dictionary
        if len(anagram_proto[letters]) > 1:
            anagrams[letters] = anagram_proto[letters].copy()

    return anagrams

def sorted_anagram():
    openfile = open("eng_dict.txt", 'r')
    #Open and read the file
    words = openfile.read().splitlines()
    anagram_proto = {}
    anagrams = {}
    for word in words:
        #sets length of words = 8
        if len(word) >= 8:
            letters = word.lower()
            word = word.lower()
            #sorts letters in word by alphabetical order
            letters = ''.join(sorted(letters))
            #add new dictionary if one doesn't exist
            if not (letters in anagram_proto):
                anagram_proto[letters] = [word]
            else:
                new = True
                #if the word is already there don't add it to anagram_proto dictionary
                for i in anagram_proto[letters]:
                    if i == word:
                        new = False
                #if the word is new, add it to anagram_proto dictionary
                if new:
                    anagram_proto[letters].append(word)
    for letters in anagram_proto:
        #if there are more than 1 word as an anagram, append to anagrams dictionary
        if len(anagram_proto[letters]) > 1:
            anagrams[letters] = anagram_proto[letters].copy()

    sorted_dict = sorted(anagrams.items(), key = lambda x : len(x[1]))
    for i in range(len(sorted_dict)):
        sequence = sorted_dict[i]
        a_list = list(sequence)
        print("BAG OF LETTERS:", a_list[0], "\n WORDS:", a_list[1], "\n")
    
    print("NUMBER OF ANAGRAMS:", len(anagrams))
#function for interesting anagrams
def five_anagrams():
    openfile = open("eng_dict.txt", 'r')
    #Open and read the file
    words = openfile.read().splitlines()
    anagram_proto = {}
    anagrams = {}
    for word in words:
        #sets length of words = 8
        if len(word) >= 8:
            letters = word.lower()
            word = word.lower()
            #sorts letters in word by alphabetical order
            letters = ''.join(sorted(letters))
            #add new dictionary if one doesn't exist
            if not (letters in anagram_proto):
                anagram_proto[letters] = [word]
            else:
                new = True
                #if the word is already there don't add it to anagram_proto dictionary
                for i in anagram_proto[letters]:
                    if i == word:
                        new = False
                #if the word is new, add it to anagram_proto dictionary
                if new:
                    anagram_proto[letters].append(word)
    for letters in anagram_proto:
        #if there are more than 1 word as an anagram, append to anagrams dictionary
        if len(anagram_proto[letters]) >= 5:
            anagrams[letters] = anagram_proto[letters].copy()
    sorted_dict = sorted(anagrams.items(), key = lambda x : len(x[1]))
    for i in range(len(sorted_dict)):
        sequence = sorted_dict[i]
        a_list = list(sequence)

        print("BAG OF LETTERS:", a_list[0], "\n WORDS:", a_list[1], "\n")
    print("NUMBER OF ANAGRAMS:", len(anagrams))

def i_anagram1(anagrams):
    listvalues1 = []
    interesting = []
    for key in anagrams:
        if len(anagrams[key]) == 2:
            listvalues1.append(anagrams[key])

    for i in range(len(listvalues1)):
        wordz=listvalues1[i]
        if len(wordz[0])%2==0:
            firsthalf = wordz[0][0:len(wordz[0])//2]
            lasthalf = wordz[1][len(wordz[1])//2:]
            if firsthalf == lasthalf:
                print("ANAGRAMS:", wordz)
                interesting.append(wordz)
    print("NUMBER OF ANAGRAMS:",len(interesting))


def i_anagram2(anagrams):
    listvalues2 = []
    interesting2 = []
    for key in anagrams:
        if len(anagrams[key]) == 2:
            listvalues2.append(anagrams[key])

    for i in range(len(listvalues2)):
        wordzz=listvalues2[i]
        if len(wordzz[0])%2==0:
            first4 = wordzz[0][0:len(wordzz[0])//2]
            last4 = wordzz[1][len(wordzz[1])//2:]
            last42 = wordzz[0][len(wordzz[1])//2:]
            first42 = wordzz[1][0:len(wordzz[0])//2]
            if first4 == last4 and first42 == last42:
                print("ANAGRAMS:", wordzz)
                interesting2.append(wordzz)
    print("NUMBER OF ANAGRAMS:",len(interesting2))


def anadromes(anagrams):  #CALLED Anadromes
    listvalues3 = []
    the_semor = []
    for key in anagrams:
        if len(anagrams[key]) > 2:
            listvalues3.append(anagrams[key])
    
    for i in range(len(listvalues3)):
        palabras = listvalues3[i]
        primera_nonreverse = palabras[0]
        primera_reverse = palabras[0][::-1]
        segunda_nonreverse = palabras[1]
        if primera_reverse == segunda_nonreverse:
            the_semor.append(primera_nonreverse)
            the_semor.append(segunda_nonreverse)
    print("ANADROMES:", the_semor)
    print("NUMBER OF ANADROMES:", len(the_semor)-1)

#all vowels prints the anagrams that contains words that have each vowel atleast once
def max_vowels(anagrams):
    listvalues = []
    the_vowels = []
    for key in anagrams:
        if len(anagrams[key]) > 1:
            listvalues.append(anagrams[key])
    for i in range(len(listvalues)):
        glosario = listvalues[i]
        firstword  = glosario[0]
        vowel_a = firstword.count("a") // 1
        vowel_e = firstword.count("e") // 1
        vowel_i = firstword.count("i") // 1
        vowel_o = firstword.count("o") // 1
        vowel_u = firstword.count("u") // 1
        add_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
        if add_vowels > 9:
            print("ANAGRAMS WITH 9 VOWELS:", glosario)
       
            the_vowels.append(glosario)
    print("NUMBER OF ANAGRAMS:", len(the_vowels))

def once_vowels(anagrams):
    listvalues = []
    the_vowels = []
    for key in anagrams:
        if len(anagrams[key]) > 1:
            listvalues.append(anagrams[key])
    for i in range(len(listvalues)):
        glosario = listvalues[i]
        firstword  = glosario[0]
        vowel_a = firstword.count("a") // 1
        vowel_e = firstword.count("e") // 1
        vowel_i = firstword.count("i") // 1
        vowel_o = firstword.count("o") // 1
        vowel_u = firstword.count("u") // 1
        multiply_vowels = vowel_a * vowel_e * vowel_i * vowel_o * vowel_u
        if multiply_vowels > 1:
            print("ANAGRAMS WITH EACH VOWEL:", glosario)
            the_vowels.append(glosario)
    print("NUMBER OF ANAGRAMS:", len(the_vowels))


#runs the functions
if __name__ == '__main__':
    choice = eval(input("Hello! This program gives different interesting functions of anagrams! Select -1 to quit!\n"
        +"Please select which type of anagrams you want to see!\n1 - All anagrams\n2 - Words with 5 anagrams\n3 - Symmetrical Anagrams"
        +"\n4 - Mirroring Anagrams\n5 - The anagram with the most vowels  !\n6 - Anadromes\n7 - Anagrams with all the vowels!\n>"))
    anagrams = b_anagram()
    while choice != -1:
        if choice == 1:
            sorted_anagram()
        elif choice == 2:
            five_anagrams()
        elif choice == 3:
            i_anagram1(anagrams)
        elif choice == 4:
            i_anagram2(anagrams)
        elif choice == 5:
            max_vowels(anagrams)
        elif choice == 6:
            anadromes(anagrams)
        elif choice == 7:
            once_vowels(anagrams)
        choice = eval(input("Hello! This program gives different interesting functions of anagrams! Select -1 to quit!\n"
        +"Please select which type of anagrams you want to see!\n1 - All anagrams\n2 - Words with 5 anagrams\n3 - Symmetrical Anagrams"
        +"\n4 - Mirroring Anagrams\n5 - The anagram with the most vowels  !\n6 - Anadromes\n7 - Anagrams with all the vowels!\n>"))
