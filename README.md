# algodoo-eval-scoreboard

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

## Add Score (Via OnCollide): 
~~~
eval("Scene.my.Point" + e.other._name + " = Scene.my.Point" + e.other._name + " + " + e.this._pointGain)
~~~
Notes: Replace other with geom if using lasers, or replace with this if marbles are adding to their own score. Replace the underlined + with a - if wanting to subtract points instead.

## Set Score(Via OnCollide):
~~~
eval("Scene.my.Point" + e.other._name + " = “ + e.this._pointSet)
~~~
Notes: Replace other with geom if using lasers, or replace with this if marbles are adding to their own score.

### Display Text (Integer):
~~~
e.this.text = Math.toString(Math.toInt(eval("Scene.my.Point" + e.this._name)))
~~~

### Display Text (Full):
~~~
e.this.text = Math.toString(eval("Scene.my.Point" + e.this._name))
~~~

### Display Text (2 Decimals):
~~~
e.this.text = Math.toString(Math.toInt(eval("Scene.my.Point" + e.this._name) * 100) / 100.0)
~~~

## Share Name:
~~~
e.this._name = e.other._name
~~~
Notes: If you want to change color, also do e.this.color = e.other.color

## Automatic Naming
~~~
e.this._name = math.toString(math.toInt(e.this.colorHSVA(0)) * 10000 + math.toInt(e.this.colorHSVA(1) * 99) * 100 + math.toInt(e.this.colorHSVA(2) * 99))
~~~
Notes: Collisions are if S = 0 or 1 and V = 0 or 1. A (Transparency) is not factored in to the automatic naming.
