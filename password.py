def random_password(num):
    chars = 'abkmcbxnzlkiop'
    num_str = str(num)
    first_num = int(num_str[0])
    print(f'el numero es tipo {type(first_num)}')
    c1 = (first_num -3) % len(chars)
    c2 = (first_num)  % len(chars)
    c3= (first_num + 4)  % len(chars)
    print(f'el numero es tipo {type(num)}')
    
    x = int(num)*2
    
    password = f'you random password is {chars[c3]}{chars[c2]}{chars[c1]}{x}'
    return password

new_password = input('give me a number crack ')

print(random_password(new_password))
