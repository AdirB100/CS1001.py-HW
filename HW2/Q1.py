############
# QUESTION 1
############

def poker_hand(hand):
    poker_hands = ["High Card", "One Pair", "Two Pairs", "Three of a Kind",
                   "Straight", "Flush", "Full House", "Four of a Kind",
                   "Straight Flush", "Royal Flush"]
    rank_dict = {'23456789TJQKA'[i]: i + 2 for i in range(13)}
    lst_hand = hand.split()
    suits, ranks = [lst_hand[i][1] for i in range(5)], [lst_hand[i][0] for i in range(5)]
    sorted_ranks_int = sorted([rank_dict[i] for i in ranks])
    same_suit = suits.count(suits[0]) == 5
    rank_difference = [sorted_ranks_int[i + 1] - sorted_ranks_int[i] for i in range(4)]
    sequential_rank = rank_difference.count(rank_difference[0]) == 4
    rank_count = {}
    for rank in ranks:
        rank_count[rank] = rank_count.get(rank, 0) + 1
    if sequential_rank:
        if same_suit:
            return poker_hands[9] if sorted_ranks_int[0] == 10 else poker_hands[8]
        return poker_hands[4]
    if same_suit:
        return poker_hands[5]
    count_vals = list(rank_count.values())
    return poker_hands[7] if 4 in count_vals \
      else poker_hands[6] if 3 in count_vals and 2 in count_vals \
      else poker_hands[3] if 3 in count_vals \
      else poker_hands[2] if count_vals.count(2) == 2 \
      else poker_hands[1] if 2 in count_vals \
      else poker_hands[0]
