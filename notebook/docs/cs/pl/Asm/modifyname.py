with open('D://MyRepository//notebook-publish/notebook/docs/cs/pl/Asm/exercise.md', 'r', encoding='utf-8') as file:
    lines = file.readlines()
with open('D://MyRepository//notebook-publish/notebook/docs/cs/pl/Asm/exercise.md', 'w', encoding='utf-8') as file:
    for line in lines:
        if line!=("\n") and (not line.startswith('|')):
            file.write(line.rstrip('\n') + '  \n')