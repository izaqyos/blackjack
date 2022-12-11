logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
 
win = """
 _______________
|@@@@|     |####|
|@@@@|     |####|
|@@@@|     |####|
\@@@@|     |####/
 \@@@|     |###/
  `@@|_____|##'
       (O)
    .-'''''-.
  .'  * * *  `.
 :  *       *  :
: ~ B L A C K ~ :
: ~ ~ J A C K ~ :
 :  *       *  :
  `.  * * *  .'
    `-.....-'
"""
win2 = """
                                    .__                                                                               ._.._.._. 
 ___.__.  ____   __ __     __  _  __|__|  ____                 _____  __  _  __  ____    ______ ____    _____    ____ | || || | 
<   |  | /  _ \ |  |  \    \ \/ \/ /|  | /    \      ______    \__  \ \ \/ \/ /_/ __ \  /  ___//  _ \  /     \ _/ __ \| || || | 
 \___  |(  <_> )|  |  /     \     / |  ||   |  \    /_____/     / __ \_\     / \  ___/  \___ \(  <_> )|  Y Y  |\  ___/ \| \| \| 
 / ____| \____/ |____/       \/\_/  |__||___|  /               (____  / \/\_/   \___  >/____  >\____/ |__|_|  / \___  >__ __ __ 
 \/                                          \/                     \/              \/      \/              \/      \/ \/ \/ \/ 
                                                                                                                                
"""
lose = """
 ___                                    .__                                   ___ 
 \  \  /\     ___.__.  ____   __ __     |  |    ____   ______  ____      /\  /  / 
  \  \ \/    <   |  | /  _ \ |  |  \    |  |   /  _ \ /  ___/_/ __ \     \/ /  /  
   )  )/\     \___  |(  <_> )|  |  /    |  |__(  <_> )\___ \ \  ___/     /\(  (   
  /  / \/     / ____| \____/ |____/     |____/ \____//____  > \___  >    \/ \  \  
 /__/         \/                                          \/      \/         \__\ 
                                                                                  
"""
clubs=[
    '''
     _________ 
    |A        |
    |+   *    |
    |    !    |
    |  *-+-*  |
    |    |    |
    |   ~~~  +|
    |        V|
     ~~~~~~~~~ 
    
    ''',
    '''
     _________ 
    |2        |
    |+        |
    |    +    |
    |         |
    |    +    |
    |        +|
    |        Z|
     ~~~~~~~~~ 

    ''',
    '''
 _________ 
|3        |
|+   +    |
|         |
|    +    |
|         |
|    +   +|
|        E|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|4        |
|+        |
|  +   +  |
|         |
|  +   +  |
|        +|
|        b|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|5        |
|+        |
|  +   +  |
|    +    |
|  +   +  |
|        +|
|        S|
 ~~~~~~~~~ 
    ''',
    '''
  _________
|6        |
|+ +   +  |
|         |
|  +   +  |
|         |
|  +   + +|
|        9|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|7        |
|+ +   +  |
|    +    |
|  +   +  |
|         |
|  +   + +|
|        L|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|8 +   +  |
|+        |
|  +   +  |
|         |
|  +   +  |
|        +|
|  +   + 8|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|9 +   +  |
|+        |
|  +   +  |
|    +    |
|  +   +  |
|        +|
|  +   + 6|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|10+   +  |
|+   +    |
|  +   +  |
|         |
|  +   +  |
|    +   +|
|  +   +0l|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|J /~~|_  |
|+ | o`,  |
|  | -|   |
| =~)+(_= |
|   |- |  |
|  `.o | +|
|  ~|__/ P|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|Q |~~~|  |
|+ /o,o\  |
|  \_-_/  |
| _-~+_-~ |
|  /~-~\  |
|  \o`o/ +|
|  |___| Q|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|K |/|\|  |
|+ /o,o\  |
|  \_-_/  |
| ~-_-~-_ |
|  /~-~\  |
|  \o`o/ +|
|  |\|/| X|
 ~~~~~~~~~ 
    ''',
    

 ]

diamonds = [
    '''
     _________ 
    |A        |
    |O  /~\   |
    |  / ^ \  |
    | (  ) |   
    |  \ v /  |
    |   \_/  O|
    |        V|
     ~~~~~~~~~ 
    ''',
    '''
 _________ 
|2        |
|O        |
|    O    |
|         |
|    O    |
|        O|
|        Z|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|3        |
|O   O    |
|         |
|    O    |
|         |
|    O   O|
|        E|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|4        |
|O        |
|  O   O  |
|         |
|  O   O  |
|        O|
|        b|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|5        |
|O        |
|  O   O  |
|    O    |
|  O   O  |
|        O|
|        S|
 ~~~~~~~~~ 
    ''',
    '''
  _________
|6        |
|O O   O  |
|         |
|  O   O  |
|         |
|  O   O O|
|        9|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|7        |
|O O   O  |
|    O    |
|  O   O  |
|         |
|  O   O O|
|        L|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|8 O   O  |
|O        |
|  O   O  |
|         |
|  O   O  |
|        O|
|  O   O 8|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|9 O   O  |
|O        |
|  O   O  |
|    O    |
|  O   O  |
|        O|
|  O   O 6|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|10O   O  |
|O   O    |
|  O   O  |
|         |
|  O   O  |
|    O   O|
|  O   O0l|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|J /~~|_  |
|O ( o\   |
|  ! \l   |
| ^^^Xvvv |
|   l\ I  |
|   \o ) O|
|  ~|__/ P|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|Q |~~~|  |
|O |o.o|  |
|   \v/   |
|  XXOXX  |
|   /^\   |
|  |o'o| O|
|  |___| Q|
 ~~~~~~~~~ 
    ''',
    '''
 _________ 
|K |/|\|  |
|O |o.o|  |
|   \v/   |
|  XXXXX  |
|   /^\   |
|  |o'o| O|
|  |\|/| X|
 ~~~~~~~~~ 
    ''',

]

hearts = [
    '''
     _________ 
    |A        |
    |# _   _  |
    | / ~V~ \ |
     Bej / |   
    |  \ # /  |
    |   `.'  #|
    |        V|
     ~~~~~~~~~ 
     ''',
     '''
 _________ 
|2        |
|#        |
|    #    |
|         |
|    #    |
|        #|
|        Z|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|3        |
|#   #    |
|         |
|    #    |
|         |
|    #   #|
|        E|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|4        |
|#        |
|  #   #  |
|         |
|  #   #  |
|        #|
|        b|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|5        |
|#        |
|  #   #  |
|    #    |
|  #   #  |
|        #|
|        S|
 ~~~~~~~~~ 
     ''',
     '''
  _________
|6        |
|# #   #  |
|         |
|  #   #  |
|         |
|  #   # #|
|        9|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|7        |
|# #   #  |
|    #    |
|  #   #  |
|         |
|  #   # #|
|        L|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|8 #   #  |
|#        |
|  #   #  |
|         |
|  #   #  |
|        #|
|  #   # 8|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|9 #   #  |
|#        |
|  #   #  |
|    #    |
|  #   #  |
|        #|
|  #   # 6|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|10#   #  |
|#   #    |
|  #   #  |
|         |
|  #   #  |
|    #   #|
|  #   #0l|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|J /~~|_  |
|# % *`.  |
|  % <~   |
| %% / %% |
|   _> %  |
|  `,* % #|
|  ~|__/ P|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|Q |~~~|  |
|# %*,*%  |
|  \_o_/  |
| -=<*>=- |
|  /~o~\  |
|  %*'*% #|
|  |___| Q|
 ~~~~~~~~~ 
     ''',
     '''
 _________ 
|K |/|\|  |
|# %*,*%  |
|  \_o_/  |
| #>-=-<# |
|  /~o~\  |
|  %*'*% #|
|  |\|/| X|
 ~~~~~~~~~ 
     ''',
         ]

spades = [
         '''
     _________
    |A        |
    |@   *    |
    |   / \   |
    /_@_\  |
    |    !    |
    |   ~ ~  @|
    |        V|
     ~~~~~~~~~
         ''',
         '''
 _________
|2        |
|@        |
|    @    |
|         |
|    @    |
|        @|
|        Z|
 ~~~~~~~~~
         ''',
         '''
 _________
|3        |
|@   @    |
|         |
|    @    |
|         |
|    @   @|
|        E|
 ~~~~~~~~~
         ''',
         '''
 _________
|4        |
|@        |
|  @   @  |
|         |
|  @   @  |
|        @|
|        b|
 ~~~~~~~~~ 
         ''',
         '''
 _________
|5        |
|@        |
|  @   @  |
|    @    |
|  @   @  |
|        @|
|        S|
 ~~~~~~~~~ 
         ''',
         '''
  _________
|6        |
|@ @   @  |
|         |
|  @   @  |
|         |
|  @   @ @|
|        9|
 ~~~~~~~~~ 
         ''',
         '''
 _________
|7        |
|@ @   @  |
|    @    |
|  @   @  |
|         |
|  @   @ @|
|        L|
 ~~~~~~~~~ 
         ''',
         '''
 _________
|8 @   @  |
|@        |
|  @   @  |
|         |
|  @   @  |
|        @|
|  @   @ 8|
 ~~~~~~~~~
         ''',
         '''
 _________
|9 @   @  |
|@        |
|  @   @  |
|    @    |
|  @   @  |
|        @|
|  @   @ 6|
 ~~~~~~~~~
         ''',
         '''
 _________
|10@   @  |
|@   @    |
|  @   @  |
|         |
|  @   @  |
|    @   @|
|  @   @0l|
 ~~~~~~~~~
         ''',
         '''
 _________
|J /~~|_  |
|@ ! -\   |
|  \ -!   |
|  ',\',  |
|   I- \  |
|   \- I @|
|  ~|__/ P|
 ~~~~~~~~~
         ''',
         '''
 _________
|Q |~~~|  |
|@ \- -/  |
| o |-|   |
|  I % I  |
|   |-| o |
|  /- -\ @|
|  |___| Q|
 ~~~~~~~~~
         ''',
         '''
 _________
|K |/|\|  |
|@ \- -/  |
| ! |-|   |
|  % I %  |
|   |-| ! |
|  /- -\ @|
|  |\|/| X|
 ~~~~~~~~~
         ''',
]