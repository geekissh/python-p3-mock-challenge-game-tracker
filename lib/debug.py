#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Instantiate classes
    game = Game('Game 1')
    player1 = Player('player1')
    player2 = Player('player2')
    result1 = Result(player1, game, 500)
    result2 = Result(player2, game, 700)
    result3 = Result(player1, game, 600)

    # Test methods and properties
    print("Game results: ", game.results())
    print("Player 1 games played: ", player1.games_played())
    print("Game players: ", game.players())
    print("Player 1 played Game 1: ", player1.played_game(game))
    print("Player 1 played Game 1 count: ", player1.num_times_played(game))
    print("Game 1 average score for Player 1: ", game.average_score(player1))

    # Enter debugger
    ipdb.set_trace()