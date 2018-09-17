import shutil, os

tt = os.listdir()
print(tt)
#curFolder = "/home/cadmin/ad"
curFolder = "test"

print("First Round")
for folderName, subFolders, filenames in os.walk(curFolder):
    #print('CurFolder :- ' + folderName)
    for filename in filenames:
        
        if filename.endswith('.txt'):
            print(folderName)
            print('Cur File :- ' + folderName + '  ' + filename)

print("Second Round")
for folderName, subFolders, filenames in os.walk(curFolder):
    #print('CurFolder :- ' + folderName)
    for filename in filenames:
        
        if filename.endswith('.txt'):
            tfile = folderName+"/"+filename
            print(tfile)
            os.unlink(tfile)
            print('Cur File :- ' + folderName + '  ' + filename)

print("Third Round")
for folderName, subFolders, filenames in os.walk(curFolder):
    #print('CurFolder :- ' + folderName)
    for filename in filenames:
        
        if filename.endswith('.txt'):
            print('Cur File :- ' + folderName + '  ' + filename)

### CORRECT SOLUTION

### SCORE = 10 MARKS

### TOTAL = 39 MARKS
