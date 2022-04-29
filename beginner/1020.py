# years = age /365
# months = age / 30
# days = age % 30

age = int(input())
new_age = age

if new_age >= 365:
    while new_age >= 365:
        new_age = int(age/365)
    print(new_age, "ano(s)")
else:
    print(0, "ano(s)")

age_months = age % 365
if age_months >= 30:
    print(int(age_months/30), "mes(es)")
    print(age_months%30, "dia(s)")

else:
    print(0, "mes(es)")
    print(age_months, "dia(s)")
