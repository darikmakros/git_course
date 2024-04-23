def getHatCats(num_cats, num_rounds):
    hats = [False] * num_cats
 
    for i in range(1, num_rounds + 1):        
        for j in range(i - 1, num_cats, i):
            hats[j] = not hats[j]
    
    hatted_cats = [index + 1 for index, has_hat in enumerate(hats) if has_hat]
    return hatted_cats

hatted_cats = getHatCats(100, 100)
print("Cats with hats:", hatted_cats)