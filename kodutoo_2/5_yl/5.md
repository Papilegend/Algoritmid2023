# Ülesanne 5

## Stabiilse algoritmi definitsioon

“Stabiilne” sortimisalgoritm tähendab seda, et kui loendis on võrdsete või sarnaste väärtustega elemendid, siis nende järjekord jääb samaks/säilib sorteeritud väljundis. 

### Näide Bubblesortiga

1) [3a, 3b, 2, 1]  
2) [3b, 2, 1, 3a]  (3a <= 3b, 3a > 2; 1)
4) [2, 1, 3a, 3b]  (3b > 2;1 , 3a <= 3b)
6) [1, 2, 3a, 3b]  (2 > 1, 2 < 3a)


## Adaptiivse algoritmi definitsioon

Adaptiivne sorteerimine tähendab seda, et sorteerimisliik suudab loendis olevate elementide järgi kohaneda ning väldib seeläbi üleliigseid vahetusi. Insertion sort on kolmest eelmainitud sorteerimisalgoritmist adaptiivne.


