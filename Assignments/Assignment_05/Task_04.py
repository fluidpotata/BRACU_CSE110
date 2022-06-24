book_info = ( ("Best Mystery & Thriller","The Silent Patient",68821), 
             ("Best Horror","The Institute",75717), 
             ("Best History & Biography","The five",31783 ), 
             ("Best Fiction","The Testaments",98291) )
for items in book_info:
    genre,name,votes = items
    print(f"{name} won '{genre}'' by {votes}")
