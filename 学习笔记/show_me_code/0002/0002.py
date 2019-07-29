import random


def gen_code(length=8):
    code_list = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65,91):
        code_list.append(chr(i))
    for i in range(97,123):
        code_list.append(chr(i))

    myslice = random.sample(code_list,length)
    active_code = ''.join(myslice)
    return active_code

if __name__ == "__main__":
