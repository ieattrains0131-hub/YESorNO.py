#Yes/No game

#Update notes
#SEPT 24th: Added play again feature. Also made it so you can only say yes/no to play again.
#Also made remarks easier to read.


#Introduction
again = True
while again == True:

    print('Welcome to the yes/no game. All inputs must be yes or no.')
    print()
    #Outside
    print('You are currently in your house.')
    outside = input("Will you go outside?: ").lower()

    #Joingang
    if outside == 'yes':
        print('You see a gang. They want you to join them.')
        joingang = input('Will you join them?: ').lower()
    
        if joingang == 'yes':
            print('Your fellow gang members want you to beat up a homeless guy.')
            beatup = input('Will you beat up the homeless guy?: ').lower()
            #Beating up
            if beatup == 'yes':
                print()
                print('Uh oh! That was a homeless veteran! He apparently still had some fight in him!')
                print("ENDING 1: Disrespectful to veterans")

            elif beatup == 'no':
                    print()
                    print('Wow, what a way to make your gang turn on you! Now they will kick your ass!')
                    print("ENDING 2: Pussy gang member")
        #No joining gang ending
        elif joingang == 'no':
            print()
            print("Uh oh! The gang doesn't look happy to hear that! They're gonna kick your ass!")
            print('Oh wait they just took your money.')
            print('ENDING 3: Mugged lol')
    #Videogames
    elif outside == 'no':
        print("Oh that's okay. The world is a scary place anyway. You should entertain yourself.")
        videogames = input('Will you play video games?: ').lower()
        if videogames == 'yes':
            print('Wow! You sure are good at gaming! Why not join a Discord server full of gamers like you?')
            discord = input('Will you join a discord server?: ').lower()
            #Kittens
            if discord == 'yes':
                print('WOAH! There are a lot of minors here! One of the 14 year old girls wants to be your Discord kitten.')
                kitten = input('Will you make this 14 year old your Discord kitten? (you are 20 btw): ').lower()
                if kitten == 'yes':
                    print()
                    print('Wow, you are vile.')
                    print("You are now wanted by the FBI. Good luck Mr. Epstein.")
                    print("ENDING 4: P Diddy")
                elif kitten == 'no':
                    print()
                    print('This minor is OBSESSED with you. She found your address and she will not have mercy.')
                    print('ENDING 5: Yandere minor')

            #No Discord ending
            elif discord == 'no':
                print()
                print('Wow, so you chose to not have anyone to play with. So sad.')
                print('ENDING 6: Just you and your CRAPBOX console')

        #Sports
        elif videogames == 'no':
            print('Okay, maybe you should turn on your TV and watch sports.')
            sports = input('Will you watch sports?: ').lower()
            if sports == 'yes':
                #Gambling
                print('You noticed that this particular team has been on a winning streak.')
                betting = input('Will you bet your life savings on this team?: ').lower()
                if betting == 'yes':
                    print()
                    print("THEY WON AGAIN! OH MY GOD YOU'RE RICH!")
                    print('ENDING 7: We have a winner')
                if betting == 'no':
                    print()
                    print("So, the team ended up winning again and you're struggling to pay off your debt.")
                    print('You REALLY coulda used the money.')
                    print('ENDING 8: Regrets')
            elif sports == 'no':
                #Why does this bum ass player keep saying no?
                something = input('Are you even going to do anything?: ').lower()
                #FINALLY
                if something == 'yes':
                    print()
                    print('You decided to do something with your life.')
                    print('You now run an Etsy business')
                    print('ENDING 9: Business owner')
                #Nothing. This player gets NOTHING.
                elif something == 'no':
                    print('ending 10: nothing. Seriously, you gotta DO something to actually get an ending.')
    #If the player doesn't enter yes or no for outside
    else:
        print()
        print('So you decided to enter something that was NOT yes or no.')
        print('REAL CLEVER BUDDY. This is the game where you can only input yes or no!')
        print('ENDING 11: Smartass')
    #Play again
    print()
    print()
    play = input('Would you like to play again?: ').lower()

    #Error check
    while play not in ('yes' , 'no'):
            print()
            print('Okay, I get that the game is over, but you still need to input yes or no.')
            play = input('Would you like to play again? (YES or NO): ').lower()
    if play == 'no':
         again = False

#Ending
print()
print('This Python game was made by Peyton Robison on September 23rd, 2025')
print('Last updated on September 24th, 2025')
print('Thanks for playing!')
