def suggestedProducts(products, searchWord):
    products = sorted(products)
    answer = [[] for i in range(len(searchWord))]
    i = 0
    temp = ''
    for w in searchWord:
        temp += w
        for word in products:
            if len(answer[i]) == 3:
                continue
            if (len(word) > i) and (word[:i+1] == temp):
                answer[i].append(word)
        i += 1
    return answer

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchword = "mouse"
print(suggestedProducts(products, searchword))


