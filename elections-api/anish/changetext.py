def change_text(Text):
    T = ""
    for K in range(len(Text)):
        if Text[K].isupper():
            T = T + Text[K].lower()
        elif K%2 == 0:
            T = T + Text[K].upper()
        else:
            T = T + T[K-1]
    
    print(T)

Text = "Good Go Head"
change_text(Text)