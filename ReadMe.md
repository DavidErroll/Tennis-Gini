# Tennis Gini(e)

This project grew out of an idea (admittedly half-baked) for a new method to determine which tennis player is/was the "greatest of all time," commonly abbreviated as the "GOAT."

Currently, most statistics would suggest that [Roger Federer](https://en.wikipedia.org/wiki/Roger_Federer) holds this position.  In addition to holding the Number 1 ranking for more weeks and having won more Grand Slam titles than any other player, the list of other tennis records that Federer holds [is long](https://en.wikipedia.org/wiki/List_of_career_achievements_by_Roger_Federer).

However, this has not stopped commentators from offering alternative analyses that support a conclusion in favor of another player, usually [Rafael Nadal](https://en.wikipedia.org/wiki/Rafael_Nadal). [One such analysis](https://www.economist.com/blogs/gametheory/2017/09/draws-tennis) was published by *The Economist*, which adapted a [ranking system originally designed for chess](https://en.wikipedia.org/wiki/Elo_rating_system) to tennis in order to control for the "adjusted difficulty of the draw."  The Elo analysis by *The Economist* concludes that Nadal's victories, while fewer, were sufficiently more difficult to conclude that he is the best player ever.

## Gini Coefficient

One of the elements that Elo sought to address is that in a single-elimination bracket-style tournament – which both chess and tennis use – there *will be* a winner, no matter what the state of the competition is.

Elo seemed to be focused primarily on the fact that two players could be awarded the same number of points for winning different tournaments despite the field of players in one being materially stronger than in the other. My Gini-based analysis seems to address the issue beginning from the opposite end of the spectrum: in any tournament, there will be a "winner" regardless of whether the players exhibit material differences in skill.  That is, even a tournament of theoretically equally-skilled players will produce a "champion" due to random chance during the play – something much more likely in tennis than in chess.

add

## 
