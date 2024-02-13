import random

def blackjack():
    arr = [1,2,3,4,5,6,7,8,9,10,10,10,10]  # Deck of cards

    computer = 0 
    player = 0
    
    temp_comp = 0
    temp_player = 0
    
    with_ace_player = 0
    with_ace_player2 = 0
    
    arr_comp = []
    arr_player = []
    
    play = input("Start Blackjack game? (y/n): ")
    
    if play == 'y':
        # Deal two cards for the computer
        arr_comp.extend(random.sample(arr,2))
        computer = sum(arr_comp)
        
        # Adjust for ace in computer's hand
        if (1 in arr_comp) and (computer + 10 <= 21):
            computer += 10
        
        # Computer hits if total is less than 17
        while computer < 17:
            computer += random.choice(arr)
        
        # Deal two cards for the player
        arr_player.extend(random.sample(arr,2))
        player = sum(arr_player)
        
        # Check for ace in player's hand
        if (1 in arr_player) and (player + 10 <= 21):
            with_ace_player = player + 10 
            print("Player's current total when Ace = 11: " + str(with_ace_player) + "\n")
            print("Player's current total when Ace = 1: " + str(player) + "\n")
        else:
            print("Player's current total:" + str(player) + "\n")
            
        hit_or_stand = input("Hit or Stand? (h/s): ")
        if hit_or_stand == 'h':
            player += random.choice(arr)
            
            if 1 in arr_player:
                with_ace_player2 = player + 10
            
            if (with_ace_player2 > player) and (with_ace_player2 <= 21):
                player = with_ace_player2
                
        else:
            if (with_ace_player > player) and (with_ace_player <= 21):
                player = with_ace_player
        
        print("Computer: " + str(computer) + " Player: " + str(player) + "\n")
        
        # Determine the winner
        if (computer > 21) and (player > 21):
            print("Both lose!\n")
        elif (computer <= 21) and (player <= 21):
            if computer > player:
                print("Computer wins!\n")
            elif computer == player:
                print("Tie!\n")
            else:
                print("Player wins!\n")
        elif (computer <= 21) and (player > 21):
            print("Computer wins!\n")
        elif (computer > 21) and (player <= 21):
            print("Player wins!\n")
        else:
            print("Error!\n")
        
        play_again = input("Play again? (y/n): ")
        
        if play_again == 'y':
            blackjack()
        else:
            return
    
    else:
        blackjack()

def main():
    blackjack()

if __name__ == "__main__":
    main()
