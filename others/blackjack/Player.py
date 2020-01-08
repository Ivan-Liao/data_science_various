class Player():
    dict_blackjack_values = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    """
    Player class.
    Attributes:
        name - name of player
        balance - player's balance
        stats - dictionary of statistics including wins, losses, draws, earnings.
        
    Methods:
        stand_or_hit - asks player to stand or hit and then executes the decision
        pick_bet - asks player about the bet amount
    """
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.stats = {'games_played':0,'wins':0,'losses':0,'draws':0,'earnings':0}
        self.list_hand = []
        self.turn_bool = False
        
    def __str__(self):
        return (f"{self.name} has ${self.balance}. " 
                f"${self.stats['earnings']} earnings, {self.stats['games_played']} games played: " 
                f"{self.stats['wins']} wins {self.stats['losses']} losses {self.stats['draws']} draws.")
        
    def stand_or_hit(self):
        while True:
            decision = input("Enter 's' for stand 'h' for hit. ")
            decision.lower() 
            if (decision == 's') or (decision == 'h'):
                return decision
            else:
                print("Please enter valid decision.")
    
    def pick_bet(self):
        """
        returns bet amount
        """
        while True:
            try:
                bet_amount = int(input("Enter bet amount. Must be $1 increments. "))
                if bet_amount <= self.balance:
                    return bet_amount
            except:
                print("Please enter a positive integer.")
    
    def card_count(self, rank):
        count = 0
        for card in self.list_hand:
            if card.rank == rank:
                count += 1
        return count
        
    
    def hand_value(self):
        value = 0
        for card in self.list_hand:
            value += self.dict_blackjack_values[card.rank]
        # counts aces in hand
        best_value = 0
        ace_count = self.card_count('A')
        # subtract 10 from hand value for every ace
        # returns greatest value for all possible subtractions
        if ace_count >= 1:
            for i in range(1, ace_count + 1):
                if value + 10 <= 21:
                    value += 10
        return value
    
    def check_bust(self):
        return self.hand_value() > 21
    
    