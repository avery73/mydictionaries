def main():
    infile = open("sometext.txt","r")

    dictionary = {}

    for text in infile:
        text = text.lower()   # converts to all lowercase
        text = text.rstrip("\n")
        text = text.replace("-"," ")
        text = text.replace(",","")
        text = text.replace(".","")
        text = text.split(" ") # splits by word

        for key in text:
            if key in dictionary:
                dictionary[key] = dictionary[key] + 1 # adds keys up
            else:
                dictionary[key] = 1 # if no more repeating keys, stay at count 1
        
    print(dictionary)

    infile.close()

main()