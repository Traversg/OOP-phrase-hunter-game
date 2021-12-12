# Create your Game class logic in here.

from phrase import Phrase
import random

class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('Spare A Square'), 
                        Phrase('No Soup For You'),
                        Phrase('Master Of My Domain'),
                        Phrase('Serenity Now'),
                        Phrase('These Pretzels Are Making Me Thirsty')]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ']
        
    def get_random_phrase(self):
        random_number = random.randint(0, (len(self.phrases) - 1))
        return self.phrases[random_number]
    
    def welcome(self):
        welcome = ' Welcome to the Phrase Guessing Game! '
        bars = '=' * len(welcome)
        print(bars)
        print(welcome)
        print(bars)
        
    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f'\nNumbers missed: {self.missed}\n')
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        
    def get_guess(self):
        guessed_letter = input('\n\nPlease guess a letter: ')
        return guessed_letter.lower()
