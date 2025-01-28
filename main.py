def wordcount(file_contents):

    return len(file_contents.split())

def characterCount(file_contents):
    
    characterDict = {}
    contentsLower = file_contents.lower()
        
    for character in contentsLower:
             
        if character in characterDict:
                    
            characterDict[character] += 1
        else:
            characterDict[character] = 1
    

    return characterDict

def sorton(dict):
    for n in dict: 
        return dict[n]

def letterList(characterDict):
    
    list=[]
    
    for n in characterDict:

        if n.isalpha():
            
            dict = {}
            dict[n]=characterDict[n]
            list.append(dict)       
   

    list.sort(reverse=True, key=sorton)
    

    for item in list:
        for n in item:
            print(f"The '{n}' character was found  {item[n]} times")

    
def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print(f"\n--- Begin report of books/frankenstein.txt ---")   

    print(f"\n{wordcount(file_contents)} words found in the document\n")

    characterDict = characterCount(file_contents) 
    
    letterList(characterDict)

    print("\n --- End report ---\n")

main()


  