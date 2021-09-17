# Source: Learn Python Programming Masterclass Created by Tim Buchalka,
# Jean-Paul Roberts, Tim Buchalka's Learn Programming Academy on Udemy
# URL: https://www.udemy.com/course/python-the-complete-python-developer-course/

# Albums List (Data)
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# Iterating Over And Unpacking Albums
while True:
    print("*** Please choose your album (invalid choice exists): \n")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}, {}, {}, {}"
              .format(index + 1, title, artist, year, songs))
    break
