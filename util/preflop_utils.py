from components.cards import offsuit_range, pairs_in_range, suited_range, suited_cards, offsuit_broadway_range, \
    suited_broadway_range

absolute_positions = {"utg", "mp", "co", "btn", "sb"}
relative_positions = {"in", "out_of"}
actions = {"open", "flat", "3bet", "4bet", "5bet"}


class PreflopRange(dict):

    def __init__(self):
        super().__init__()
        for position in absolute_positions:
            self[position] = {}
        self["utg"]["open"] = pairs_in_range("A", 3) + offsuit_range("A", "J") + offsuit_range("K", "Q") + \
                              suited_range("A", 10) + suited_range("K", 10) + suited_range("Q", 10) + suited_range("J",
                                                                                                                   9) + \
                              suited_broadway_range(10, 6, 1)

        self["mp"]["open"] = pairs_in_range() + offsuit_range("A", 10) + offsuit_range("K", "Q") + suited_range("A",
                                                                                                                7) + \
                             suited_cards("A", 5) + suited_range("K", 10) + suited_range("Q", 10) + suited_range("J",
                                                                                                                 9) + \
                             suited_broadway_range(10, 7, 2) + suited_broadway_range(6, 5, 1)

        self["co"]["open"] = pairs_in_range() + offsuit_range("A", 10) + offsuit_range("K", "J") + offsuit_range("Q",
                                                                                                                 "J") + \
                             suited_range("A") + suited_range("K", 6) + suited_range("Q", 7) + suited_range("J", 8) + \
                             suited_broadway_range(10, 6, 2) + suited_broadway_range(5, 5, 1)

        self["btn"]["open"] = pairs_in_range() + offsuit_range("A") + offsuit_range("K", 7) + offsuit_range("Q", 9) + \
                              offsuit_broadway_range("J", 10, 2) + offsuit_broadway_range(9, 8, 1) + suited_range("A") + \
                              suited_range("K") + suited_range("Q") + suited_range("J", 5) + suited_range(10, 6) + \
                              suited_broadway_range(9, 7, 3) + suited_broadway_range(6, 5, 2) + suited_broadway_range(4,
                                                                                                                      4,
                                                                                                                      1)

        self["sb"]["open"] = pairs_in_range() + offsuit_range("A", 7) + offsuit_range("K", 9) + offsuit_range("Q", 9) + \
                             offsuit_range("J", 9) + offsuit_broadway_range(10, 9, 1) + suited_range(
            "A") + suited_range("K") + \
                             suited_range("Q", 4) + suited_range("J", 7) + suited_range(10, 7) + suited_broadway_range(
            9, 6, 2) + \
                             suited_broadway_range(5, 5, 1)
