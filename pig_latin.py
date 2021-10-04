import sys

def pig_latin(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    cons = '-'
    count = 0
    for char in word:
        if char not in vowels:
            cons += char
            count += 1
            continue
        else:
            break

    result = word[count:] + cons + 'ay'
    print(result)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])