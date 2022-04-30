def qs(ls):
    if not ls:
        return []
    return (qs([word for word in ls[1:] if word < ls[0]])
            + [ls[0]] +
            qs([word for word in ls[1:] if word >= ls[0]]))


stringVal = "sort this string into alphabetical order"
ls = [word for word in stringVal.split(" ")]
print(qs(ls))
