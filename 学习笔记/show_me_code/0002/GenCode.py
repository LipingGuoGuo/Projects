import random
import string


forSelect = string.ascii_letters + "0123456789"


def gen_code(count, length=8):
   for c in range(count):
       Re = ""
       for y in range(length):
           Re += random.choice(forSelect)
        print(Re)


if __name__ == "__main__":
    generate(200,20)
