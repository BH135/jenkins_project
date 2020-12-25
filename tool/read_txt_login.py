def read_txt():
    with open("../data/login.txt", "r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
    arrs = []
    for data in read_txt():
        arrs.append(tuple(data.strip().split(",")))

    print(arrs[1::])