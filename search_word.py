import pprint
import os
os.system('cls')
inputSequence = "Воображаю день счастливый, Когда средь вас возник лицей, И слышу наших игр я снова шум игривый И вижу вновь семью друзей."
searchWorld = "слова"
matchedDict = {}
searchWorldCount = 1000
def not_find():
    print('Буков не хватило, слово не составить.')
    print("==================================================================")
    quit()
print("==================================================================")
print("Составляем слово:", end=' ')
print("{ " + searchWorld + " }\n") 
print("Из букв фразы:", end=' ')
print("{ " + inputSequence + " }\n")
lenth = len(inputSequence)
######################## Массив нужных букв ########################
for character in searchWorld:
    if not character in matchedDict.keys():
        start = 0
        newposition = 0    
        try:
            for symbol in inputSequence:                
                newposition  = inputSequence.index(character, start, len(inputSequence))
                if not newposition in matchedDict.values():
                    #print(newposition)                               
                    matchedDict.setdefault(character,[]).append(inputSequence.index(character, start, len(inputSequence)))
                start = newposition + 1                
                #pprint.pprint(matchedDict, width=20)
        except:                          
            foo = "bar"
#pprint.pprint(matchedDict, width=20)      
######################## Поиск кол-ва слов ########################
for character in matchedDict:
    x = matchedDict.get(character)
    #print(searchWorldCount)
    #print(x)
    if searchWorldCount >= len(x):
        searchWorldCount = len(x)
        #print(searchWorldCount)
######################## Поиск слова ########################
for character in searchWorld:
    if character in matchedDict:        
        #print('Буква нашлась:' + character)        
        x = matchedDict.get(character)
        ## убавим букву если есть запас
        if x and len(x) > 0 :
            x.pop()
        else:     
            not_find()                   
    else:
         not_find()         
print("\n(: Слово нашлось :) [ " + searchWorld + " ]")
print(" и потворилось  [ " + str(searchWorldCount) + " ] раз.")
print("==================================================================")
#print("Не потраченные буквы:")
#pprint.pprint(matchedDict, width=20)
#input('Press Enter to Continue')
