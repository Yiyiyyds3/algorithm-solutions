birthday=input()
if len(birthday)==4:
    if birthday[0:2]<"22":
        year="20"+birthday[0:2]
        month=birthday[2:4]
        print(f"{year}-{month}")
    else:
        year="19"+birthday[0:2]
        month=birthday[2:4]
        print(f"{year}-{month}")
elif len(birthday)==6:
    year=birthday[0:4]
    month=birthday[4:6]
    print(f"{year}-{month}")