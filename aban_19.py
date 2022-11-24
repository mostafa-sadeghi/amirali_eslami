
# zfil alternative
# z = 'abc'
# x = z.rjust(6, ' ')
# print(x)

# x: int = 0


def custom_rjust(string: str, length: int) -> str:
    '''
    Parameters:
    length : number of zeros that must be placed in start point (0)
    '''
    string_list = list(string)
    string_list.insert(0, length*'0')
    # alternative:
    # for _ in range(length):
    #     string_list.insert(0, '0')
    string_list = "".join(string_list)
    return string_list


if __name__ == '__main__':
    print(custom_rjust('123', 3))
