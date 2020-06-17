# text = input('prompt\n')
# print(f'Fook off! {text}')
# This is a comment?

from dice import Die
from dice import DiceShaker

first_attack_dice=DiceShaker(Die(6, 4) * 4)
first_defense_dice=DiceShaker(Die(6, 5) * 3)
second_attack_dice=DiceShaker(Die(6, 4) * 3)
second_defense_dice=DiceShaker(Die(6, 5) * 4)