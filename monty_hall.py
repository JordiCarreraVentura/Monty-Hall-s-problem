import random
import tqdm

from collections import Counter

from tqdm import tqdm

DOORS = 3
choices1 = Counter()
choices2 = Counter()
experiments = list(range(100000))
for i in tqdm(experiments):
    prize = random.randrange(0, 3)
    choice1 = random.randrange(0, 3)
    revealable = [
        door for door in range(DOORS)
        if door != choice1 and door != prize
    ]
    revealed = random.sample(revealable, 1)[0]
    second_guess = [
        door for door in range(DOORS)
        if door != revealed
    ]
    choice2 = random.sample(second_guess, 1)[0]
    
    if choice1 == prize:
        choices1[1] += 1
    else:
        choices1[0] += 1
    
    if choice2 == prize:
        choices2[1] += 1
    else:
        choices2[0] += 1
    
#     print 'prize', prize
#     print 'choice1', choice1
#     print 'revealable', revealable
#     print 'second_guess', second_guess
#     print 'choice2', choice2
#     print 'choices1', choices1.most_common()
#     print 'choices2', choices2.most_common()
#     print

for outcome, freq in choices1.most_common():
    print '1st choice - %s %.2f (%d)' % (
        'Win' if outcome else 'Loss', round(freq / float(len(experiments)), 2), freq
    )

for outcome, freq in choices2.most_common():
    print '2nd choice - %s %.2f (%d)' % (
        'Win' if outcome else 'Loss', round(freq / float(len(experiments)), 2), freq
    )
