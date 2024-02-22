import sys, os, re
#os.system('clear')
log_File_Path = sys.argv[1] # Первый аргумент: полный путь к файлу логов.
search_String = sys.argv[2] # Второй аргумент: искомое слово.
qualification = sys.argv[3] # Третий аргумент: уточняющее слово.
regexp = sys.argv[4]        # 4-ый аогумент: регулярка для поиска

regex = search_String
match_list = []

logFile = open(log_File_Path, "rt")

try:
    regexp
except :
    for line in logFile:
            for match in re.finditer(search_String, line, re.S):
                #match_text = match.group()
                #print(line)

                for match in re.finditer(qualification, line, re.S):
                    match_list.append(match.group())
                    # print(match_text)
###                    print(line)
else:
    for line in logFile:
         for match in re.finditer(regexp, line, re.S):
              match_text = match.group()
              match_list.append(match_text)
              print(match_text)
              #print(line)
