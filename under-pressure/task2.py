


def analyse(param):
    if param.isdigit():
        if(int(param)) % 2 == 0:
            print("Integer ie even")
        else:
            print("Integer is odd")
    elif param.isalpha():
        if(len(param))==1:
            print(param)
        else:
            print(param+" Length is - "+str(len(param)))
        



#print("Enter your parameter :- ") read param
param=''
while param != 'stop':
    param = input("Input your parameter (type 'stop' to exit) :-")
    analyse(param)
