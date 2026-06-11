import sys

print(sys.path)



#function to create a random password

def random_password(num):
    chars = 'abcdefghijklmnopqrst'
    #conver the parameter to str
    num_str = str(num)
    if not num_str.isdigit():
     return 'error, solo numeros'
    first_num = int(num_str[0])
    c1 = (first_num -3) % len(chars)
    c2 = (first_num)  % len(chars)
    c3= (first_num + 4)  % len(chars)
    
    x = int(num)*2
    
    password = f'you random password is {chars[c3]}{chars[c2]}{chars[c1]}{x}'
    return password

if __name__ == '__main__':

 new_password = input('give me a number crack ')

 print(random_password(new_password))

num =[1,2,3,4,5,6]

for i in num :
    print(i)