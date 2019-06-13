# Algodoo Scoreboard

This is the setup that WuigiBaka uses for their marble events.

# Basic Setup

e.this.\_name: Used as an identifier. Marbles sharing the same name will share the same score.

Scene.my.Point (+ \_name): Where all of the scores are stored. For example, if a marble had the name “Red”, their score would be at “Scene.my.PointRed”.

e.this.\_pointGain: Determines how many points to give. Negatives do not work.

e.this.\_pointSet: How many points to set a marble to.

### Marbles

Marbles will need e.this.\_name to function.

### Point Givers

Point Givers need e.this.\_pointGain to function. They do not need e.this.\_name

### Scoreboard

The scoreboard needs e.this.\_name to function.

# Functions

## Add Score (Via OnCollide)
~~~
eval("Scene.my.Point" + e.other._name + " = Scene.my.Point" + e.other._name + " + " + e.this._pointGain)
~~~
Used to add score to the marble that hits the point-giver. 

Adjustments: Replace other with geom if using lasers, or replace with this if marbles are adding to their own score. Replace the second-to-last + with - if subtracting score instead.

## Set Score(Via OnCollide)
~~~
eval("Scene.my.Point" + e.other._name + " = “ + e.this._pointSet)
~~~
Used to set a marble's score to a certain number when hitting the object that has it.

Adjustments: Replace other with geom if using lasers, or replace with this if marbles are adding to their own score.

## Display Text
These should be used to display each marble's individual score.

### Integer Text
~~~
e.this.text = Math.toString(Math.toInt(eval("Scene.my.Point" + e.this._name)))
~~~
Truncates past the integer. EX: -0.9 -> 0; 0.9 -> 0; 1.9 -> 1; -1.9 -> -1.

### Full Text
~~~
e.this.text = Math.toString(eval("Scene.my.Point" + e.this._name))
~~~
Not recommended due to the length of the text changing often.

### 2 Decimals
~~~
e.this.text = Math.toString(Math.toInt(eval("Scene.my.Point" + e.this._name) * 100) / 100.0)
~~~
Truncates past the second decimal.


## Share Name
~~~
e.this._name = e.other._name
~~~
Notes: If you want to change color, also do e.this.color = e.other.color

## Automatic Naming
~~~
e.this._name = math.toString(math.toInt(e.this.colorHSVA(0)) * 10000 + math.toInt(e.this.colorHSVA(1) * 99) * 100 + math.toInt(e.this.colorHSVA(2) * 99))
~~~
Notes: S = 0 or 1, as well as V = 0 or 1 with the same H will cause name collisions. A (Transparency) is not factored in to the automatic naming, so changing only A will cause name collisions.
