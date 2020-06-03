films = {
    "Finding Dory" : [3,5],
    "Bourne" : [18,5],
    "Tarzan" : [15,0],
    "Ghost Busters" : [12,5]
}

while True:
    choice = input("What movie do you want to watch? ").strip().title()     #all inputs will start with capital letters
    if choice in films:
        age =  int(input("How old are you? ").strip())
        if age >= films[choice][0]:
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the movie")
                num_seats -= 1
            else:
                print("Sorry, no tickets")
        else:
            print("You are too young for the movie")
    else:
        print("we don't have that film")
