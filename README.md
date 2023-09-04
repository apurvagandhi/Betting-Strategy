# Betting-Strategy
This project will perform probabilistic experiments involving an American Roulette wheel. The project will help provide you with some initial feel for risk, probability, and “betting.” 

The goal of this project is to look into the well-known Martingale betting strategy
using Monte Carlo simulation in the context of a Roulette game. A Martingale
strategy is a type of betting strategy that developed in 18th-century France and
gained popularity during that time period. The most basic version of this method
was created for a game in which a gambler would win if a coin landed heads
up and lose if the coin landed tails up. The method entails doubling the bet
after each loss, with the ultimate goal of earning a win that not only recovers all
previous losses but also provides a profit equal to the initial stake. For example,
if we start with $1, the first bet will be $1. If a player wins the bet, he or she
collects the money and the game ends. If a player loses a stake, the next bet is
doubled to equal the prior bet. The Martingale gambling simulator was used to
carry out the following tests.
1. Using Monte Carlo simulation, investigate the strategy. There is no bankroll
limit, but we set a goal of winning $80 before we stop playing.
2. Investigating the strategy With a $256 bankroll. That is, if the player runs out
of money, players can not bet more money.
The odds of winning a bet on black is 18/38. Therefore, the experiments use the
probability of 18/38. The odds are calculated as following:
Odds of winning on black = (Number of black pockets) / (Total number of pockets)
Odds of winning on black = 18 / 38
