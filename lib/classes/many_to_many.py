class Game:
    def __init__(self, title):
        # Initialize a new Game instance with a given title. The results of the game are stored as a list 
        # of Result instances.
        self.title = title
        self.results = []

    def results(self):
        # Return a list of all the results for this game.
        return self.results

    def players(self):
        # Return a list of all the players who have played this game.
        players = set()
        for result in self.results:
            players.add(result.player)
        return list(players)

    def average_score(self, player):
        # Return the average score for the specified player in this game. If the player has not 
        # played the game, return None.
        scores = [result.score for result in self.results if result.player == player]
        return sum(scores) / len(scores) if scores else None

class Player:
    def __init__(self, username):
        # Initialize a new Player instance with a given username. The results of the player's games
        # are stored as a list of Result instances.
        self.username = username
        self.results = []

    def results(self):
        # Return a list of all the results for this player.
        return self.results

    def games_played(self):
        # Return a list of all the games this player has played.
        games = set()
        for result in self.results:
            games.add(result.game)
        return list(games)

    def played_game(self, game):
        # Return True if the player has played the specified game, otherwise return False.
        for result in self.results:
            if result.game == game:
                return True
        return False

    def num_times_played(self, game):
        # Return the number of times the player has played the specified game.
        return len([result for result in self.results if result.game == game])

class Result:
    def __init__(self, player, game, score):
        # Initialize a new Result instance with a given player, game, and score. The result is added to
        # the lists of results of the player and game.
        self.player = player
        self.game = game
        self.score = score

        if not isinstance(player, Player):
            # Verify the player is an instance of the Player class
            raise ValueError("player must be an instance of Player class")
        if not isinstance(game, Game):
            # Verify the game is an instance of the Game class
            raise ValueError("game must be an instance of Game class")
        if not isinstance(score, int) or score < 1 or score > 5000:
            # Verify the score is an integer between 1 and 5000
            raise ValueError("score must be an integer between 1 and 5000")

        if self.played_game(player, game):
            # Verify the player has not played the game before
            raise ValueError("player has already played this game")

        game.results.append(self)
        player.results.append(self)

    @staticmethod
    def played_game(player, game):
        # Return True if a Result exists with the given player and game, otherwise return False.
        for result in Game.results(game):
            if result.player == player:
                return True
        return False