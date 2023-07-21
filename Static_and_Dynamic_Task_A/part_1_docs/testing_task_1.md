### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
                           

  def check_for_ace(self, card):
    if card.value = 1:       #!!!!ERROR #1 !!!! It needs a double equal sign ==, not a single equal sign =
      return True
    else                     #!!!!ERROR #2 !!!!! It is missing a colon :
      return False
   

  dif highest_card(self, card1 card2):    #!!!!ERROR #3 !!!! It should say def instead of dif. !!!!ERROR #4 !!!! There is a comma missing after card1
  if card1.value > card2.value:      #!!!!ERROR #5 !!!! The code block inside of the function must be indented
    return card             #!!!!ERROR #6 !!!! It should return card1 rather than card
  else:
    return card2
  


def cards_total(self, cards):         #!!!! ERROR #7 !!!! this function definition block needs to be indented
  total                    #!!!ERROR #8 !!!! total should be assigned a value of 0 with total = 0
  for card in cards
    total += card.value
    return "You have a total of" + total   #!!!!ERROR #9 !!!! The return statement should not be indented. The return statement should be outside of the for loop.
  
```
