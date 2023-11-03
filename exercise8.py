def vokon_zählen(x):
    wort = x
    count = 0
    vokalen = ["a", "e", "i", "o", "u"]
    for i in wort:
        if i.isalpha():
            if i in vokalen:
                count += 1
    return count

print(vokon_zählen("Hello Berlin"))