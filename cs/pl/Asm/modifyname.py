with open('D://MyRepository//notebook-publish/notebook/docs/cs/pl/Asm/sum.md', 'r', encoding='utf-8') as file:
    lines = file.readlines()
with open('D://MyRepository//notebook-publish/notebook/docs/cs/pl/Asm/sum.md', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line.rstrip('\n') + '  \n')