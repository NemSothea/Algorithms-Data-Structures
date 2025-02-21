def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """
    Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    # case 1 : if the total player is more 21
    if player_total > 21:
        return False
    # case 2 : if the total player is less than 17
    # we will count it as 11 + 1 + 1 + 7
    if player_total >= 17:
        return player_total < 17
    # case 3 : if the total player is more than 17
    return player_total < 12

print(should_hit(2, 20, 2, 1)) # False