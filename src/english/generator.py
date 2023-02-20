import random
import string

vowels = 'aeiou'
consonants = ''.join(c for c in string.ascii_lowercase if c not in vowels)
nouns = ['cat', 'dog', 'man', 'woman', 'tree', 'house', 'car', 'book']
verbs = ['runs', 'jumps', 'eats', 'sleeps', 'reads', 'drives', 'likes', 'hates']
adjectives = ['happy', 'sad', 'angry', 'funny', 'smart', 'stupid', 'tall', 'short']
adverbs = ['quickly', 'slowly', 'quietly', 'loudly', 'happily', 'sadly', 'angrily', 'eagerly']

def generate_word(length):
    word = ''
    for i in range(length):
        if i % 2 == 0:
            # Add a consonant
            word += random.choice(consonants)
        else:
            # Add a vowel
            word += random.choice(vowels)
    return word

def generate_sentence():
    subject = random.choice(nouns).capitalize()
    verb = random.choice(verbs)
    object = random.choice(nouns)
    phrase = ''
    if random.randint(0, 1) == 0:
        # Add an adjective
        phrase += ' ' + random.choice(adjectives)
    if random.randint(0, 1) == 0:
        # Add an adverb
        phrase += ' ' + random.choice(adverbs)
    return subject + ' ' + verb + ' ' + phrase + ' ' + object + '.'

if __name__ == '__main__':
    # Generate 10 random words with lengths between 5 and 10 characters
    for i in range(10):
        length = random.randint(5, 10)
        word = generate_word(length)
        print(word)
        
    # Generate 10 random sentences
    for i in range(10):
        sentence = generate_sentence()
        print(sentence)
