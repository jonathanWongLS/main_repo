if __name__ == '__main__':
    ar = []
    for i in range(100, 200):
        ar.append(i)

    print(ar)
    res = 0
    for j in ar:
        res += j/100
    print(res)