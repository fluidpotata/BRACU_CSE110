max = 'TBD'
genre = ""
dict1 = {'sci fi': -1, 'mystery': -15, 'horror':- 8, 'mythology': -10, 'young_adult': -4, 'adventure':-14}

for key,val in dict1.items():
    if max=='TBD':
        max = val
    if val>max:
        max = val
        genre = key
        
print(f"The highest selling book genre is '{genre}' and the number of books sold are {max}.")
