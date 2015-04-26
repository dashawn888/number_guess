import locale
locale.setlocale(locale.LC_ALL, 'en_US')

min_num = 0
max_num = 1000 + 1

while True:
    guess = (min_num + max_num) / 2
    print locale.format("%d", guess, grouping=True)
    responce = raw_input("hlc: ")

    if responce == "c":
        print "cool number"
        break

    if responce == "l":
        max_num = guess

    if responce == "h":
        min_num = guess