# Algicosathlon Scoreboard

How to use the AlgiosathlonScoreboard.

## What is This?

This is a scoreboard that aims to be similar to carykh's original Algicosathlon scoreboard.
The only thing that hasn't been added directly is the ELIMINATED bar.

#### So, should I use it?

It's a pretty solid scoreboard. If you don't have anything better, go ahead.

## General Notes

Do not remove eliminated marbles from the scoring.

## Initial Points

![InitialPoints](https://raw.githubusercontent.com/Wenyunity/algodoo-eval-scoreboard/master/AlgicoEx/Initial.PNG)

This is the setup for initial points. Type in the marble's points prior to the event in question. If the scoreboard is not in sorted order, you will have to sort it first. (You can do this either manually, or let the sorter handle it.)

## Sorter

![Sorter](https://raw.githubusercontent.com/Wenyunity/algodoo-eval-scoreboard/master/AlgicoEx/compare.PNG)

This is the sorter. When all marbles go through the sorter, it will find what place the athletes are in. Make sure that all marbles go through the sorter after the scores are updated.

## Event Score

![Event](https://raw.githubusercontent.com/Wenyunity/algodoo-eval-scoreboard/master/AlgicoEx/EventPoints.PNG)

This is the setup for each event. Below each marble, place the amount of points they gained in the event. If a marble is eliminated, place the ELIM block below the marble.

## Scoreboard

![Score](https://github.com/Wenyunity/algodoo-eval-scoreboard/blob/master/AlgicoEx/scoreboard.PNG)

This is the scoreboard. You can edit the names of the athletes. Do not edit the scores of the athletes here; it will not work. If you need more space, you can expand the textbox for the names.

## Settings

![Settings](https://raw.githubusercontent.com/Wenyunity/algodoo-eval-scoreboard/master/AlgicoEx/Settings.PNG)

The top-left setting shows how many seconds it takes for the bars to go from their old scores to their new ones. The higher this number, the slower the bars will increase.

The top-right setting shows how many seconds it takes for the bars to switch to their new places. The higher this number, the slower the bars move to their new places.

The bottom setting shows how long the bar of the leading player will be. The more to the right it is, the longer the bars will be. Note that the names are not counted here; so it is advised to leave space for the name.

# How to Add Contestants

Copying and pasting does work, and is highly recommended. Changing the color (along with a start-undo-start reset) will automatically sync the items to the new color.

In order to add another contestant, they will need the following. Change **all items to the desired color.**

- A Scoreboard Bar. **Make Sure ALL three boxes have the desired color.**
- A sorter Bar. If you add a lot of contestants, you'll need to move the Event score upwards (and possibly expand the sorter horizontally).
- An Initial Score.
- A marble.
