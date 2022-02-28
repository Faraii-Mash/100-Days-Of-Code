# By FB Mashiri for #100Days of Code
# A small treasure island choice  game
# This program uses user input to navigate through if functions in order to simulate a choice making story

print('''
b                            ,,,,                    ,d
 8b,                       ,(()(()),               ,ad8P
d888b,_                   ,(((""""))),           ,d8888b,
88   `"Ya,_              ,(()<@  @>(()        _a8P"  `888b
Y8ba,a   `"Ya,_          (()(  ..  ))(      _aP"   ad88888b
`8888P       `"Ya,_      ())(\ -- /(()    ,aP'       `Y8888
 Y88P'           `""Ya,_ )(())`--'())  ,adP'   ,@,     Y88P
 `Y8'       ,@,       ""Y((()'|  |`()aP"'      @@@     ,8P'
  `Ybaad    @@@        /'            `\        `@'   ad8'
    8P"     `@'       /    /        \  \              Y8,
   dP'               /    /(  o |    o  \     b,    b  `8
  d'  d     ,P      /   /|  `--' `--/'\  \    `8,  YP  dP
  8,  YP  ,d"      |  /' |         /   | |     `Ya,__,dP'
  `Yb,__,a8P       | |   |       ,'    | |      `88888P'
    "Y88888ba      | |   )     . (     | |      d888P"
      `"Y888'      | |  /         \    | |      `8P"
         `"Yb,     | | (           `.  / \      ,8'
            `Ya    / \ (      `Y'    \|/\ \    b8'
              `b  / /\|`.       `\    \  ||    `8,
               8  ||    8\        `\   \        8b,
               8        8 `\        \   \       888,
              dP        8   `\       \   ),    dP'`8b,
            ,d88       ,P     `\      \  )Y, ,d"   888,
          ,d8' 8,     ,P'       `\     )/ `Yd"     8'`b,
        ,dP'8  `Y,,,aP"          ,)    )   `Y,    8'  `b
       d"   "    `8'            //    /     `Y,        8,
      d'  ,@,     8           /'/    /       `b   ,@,  `b
     d'   @@@    ,P        _,' (    /         8   @@@   8,
     8, a `@'   ,P'       |   (    /          8   `@'   `b
     `b 8      aP'        |  /|   /           Y,         8
      8 `b   ,d"          | / )  /            `Ya,  a,   8
      8 ,8a,aP'           \/ ,' (               "Ya,`P  ,8
      8a888P'                (   \                "Y8b,,d8
      888P'                   `\  \                 "Y888P
      8P'                       `\ |                  Y8P'
      P                           `'                   P'
''')
print('Welcome to Treasure Island.')
print('A mythical magic story game')
print('Your mission is to not get trapped by the mystical creature and find the treasure.')

#Initial story
choice1 = input(' You\'ve just crash landed in your boat. To your left is a sandy beach and to your right is the mountain range. Where do you want to go? Type "left" or "right" \n').lower()

if choice1 == 'left':
  choice2 = input('You\'ve walked down the beach and find a many boats coming and leaving the beach usable. You can take a boat to the come the other side of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == 'wait':
    choice3 = input('You arrive at the other side of the lake unharmed. There is a small cabin with 3 doors. One red, one yellow and one blue. Which colour door do you choose? \n').lower()
    if choice3 == 'red':
      print('It is a room that has no light. As you enter, the door closes and you\'re never heard from again. Game Over.')
    elif choice3 == 'yellow':
      print('You found the treasure! Congradulations You Win!')
    elif choice3 == 'blue':
      print('You entered a room of beasts. They offer you to the mermaid queen as a peace offering. Game Over.')
    else:
      print('You chose a door that does not exist. Game Over.')
  else:
    print('The mermaids come and collect you. You are now in their hands. Game Over.')
else:
  print('You fell of a cliff. Game Over.')
