fileName = 196500

path = f"HebrewSentence/hebrew_small_file_{fileName}"


file = open(path,"r+",encoding="utf-8")

lines = file.readlines()

# [print(line[::-1]) for line in lines]

inverted_line =[]
for line in lines:
    print(line)
    print(line[::-1])
    inverted_line.append(line[::-1])
    