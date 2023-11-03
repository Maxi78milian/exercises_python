x = "Hallo, Berlin"

x_list = list(x)
count_letters = []
for buchstabe in x_list:
    count_letters.append(buchstabe.isalpha())


print(sum(count_letters))