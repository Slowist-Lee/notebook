import hashlib
import os
lst=[]
def md5_hash_check(string):
    md5 = hashlib.md5()
    md5.update(string.encode('utf-8'))
    md5_value=md5.hexdigest()
    if md5_value.startswith('0e'):
        # print(f"'{string}'produces: {md5_value}")
        lst.append(string)
def search_strings_in_files(directory):
    cnt = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    for line in f:
                        line = line.strip()
                        md5_hash_check(line)
                        cnt += 1
            except (PermissionError, OSError) as e:
                print(f"Skipping file {file_path}: {e}")
    return cnt


directory_to_search = "D:/MyRepository/slowist-notebook/docs/Coding/CTF"
cnt=search_strings_in_files(directory_to_search)
num=len(lst)
s='\n'.join(lst)
with open('D:/MyRepository/slowist-notebook/docs/Coding/CTF/web-lab3/result.txt', 'w',errors='replace') as file:
    file.write(s)
print(f"{cnt}file_lines read, {num}lines written")