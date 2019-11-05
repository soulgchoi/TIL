s = 'Reverse this strings'

# ss = s[::-1]
#
# print(ss)


def reverse(x):
    str_list = []
    for char in x:
        str_list.append(char)

    for n in range(len(x)//2):
        str_list[0+n], str_list[-1-n] = str_list[-1-n], str_list[0+n]

    return ''.join(str_list)


print(reverse(s))
