from typing import List


def omit(list: List, words: str, n: int) -> List:
    for i in range(n):
        list.remove(words)
    return list

def omit2(list: List, words: str, n: int) -> List:
    index = 0
    count = 0
    while (count < n) and (index < len(list)):
        if list[index] == words:
            list.pop(index)
            count += 1
        index += 1
    return list

if __name__ == '__main__':
    print(omit2(['can','you', 'can', 'a', 'can', '?', 'can'], 'can', 3))

