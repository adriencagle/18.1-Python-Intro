def wordsUpper(list, req):
    for word in list:
        for letter in req:
            if word.startswith(letter):
                return (word.upper())