# Other Scoreboard Functions

These are functions that are not necessary but will work with the scoreboard presented in README.

They will not work without the setup described in README.

Parenthesis after the name shows which Algodoo function to paste it (inside of the curly brackets).

# Score Sorting (OnKey, put in all Marbles)

This will put all of the marbles horizontally at the Y = 0 line, with their integer score (truncated) being their X-Value, when pressing capital A.

~~~
keys.isdown("A") ? {
    pos = [math.toint(eval("Scene.my.point" + e.this._name)), 0];
    vel = [0, 0];
    sim.running = false
} : {}
~~~

Alternate version if you want the true score and not rounded to the nearest integer:

~~~
keys.isdown("A") ? {
    pos = [eval("Scene.my.point" + e.this._name), 0];
    vel = [0, 0];
    sim.running = false
} : {}
~~~
It will also stop the simulation, and set all velocities to zero. Be careful, because marbles may overlap partially or fully.

# Interpret Sorted Score (OnCollide)
If you paste sorted marbles from a different scene, then this can interpret how many points each marble got.
~~~
e.this._pointGain = math.toInt(e.other.pos(0));
eval("Scene.my.Point" + e.other._name + " = Scene.my.Point" + e.other._name + " + " + e.this._pointGain)
~~~

Alternative for non-integer:
~~~
e.this._pointGain = e.other.pos(0);
eval("Scene.my.Point" + e.other._name + " = Scene.my.Point" + e.other._name + " + " + e.this._pointGain)
~~~
Put a teleport after the function so that the marbles do not hit multiple times.

# Score Sorting (OnCollide)
When colliding with the block, it will teleport the marble to the number of points in the X-Axis, and 0 in the Y-Axis.
~~~
eval("e.other.pos = ["Scene.my.Point" + e.other._name + ", 0]")
~~~

In Algodoo Marble Trials, I use a different version of this for the results screen.
~~~
eval("e.other.pos = [99.5 - Scene.my.Point" + e.other._name + ", 4.5]")
~~~
This one puts the marbles at 99.5 - The Marble's score in the X-Position, which means marbles with a greater score will be on the left. All marbles were put on 4.5 in the Y-Position. (Note: This might not make sense if you've watched Trials, but the next one will clear this up.)

# Modified Display (Scoreboard PostStep)
In this display, I use 99 - Score.
~~~
eval("e.this.text = Math.toString(99 - Scene.my.Point" + e.this._name + ")")
~~~
This was to show the number of lives remaining in Algodoo Marble Trials, since I actually counted the number of deaths in Scene.my.Point in that series.

# Score Checker (OnCollide)
This is an if statement that checks the score of a marble. Scene.my.FinishScore is the minimum score needed for a Marble to pass.
~~~
eval("Scene.my.Point" + e.other._name + " >=  Scene.my.FinishScore ? 
    {#Stuff done if they met the score} : 
    {#Stuff done if they don't meet the score}");
~~~

In Tour Season 2, this is the code I used:
~~~
(e)=>{
    eval("Scene.my.Point" + e.other._name + " + 1 >  Scene.my.FinishScore ? {e.this._win = true} : {e.this._win = false}");
    e.this._win ? {
        e.other.pos = Scene.my.winPort;
        e.other.vel = [0, 0]
    } : {
        e.other.collideSet = 1017
    }
}
~~~
The section in the eval just sets e.this._win to true if the marble meets the score, or false if they do not. I did this to make the if statement as short as possible.

If the marble does meet the score, they're teleported to the exit; if it doesn't, they switch to a collideSet that does not include Collision Layer B. The Score Checker is only on Collision Layer B.

# Marble Painting (OnCollide)
For paint wars, use this for the objects to be painted.
~~~
eval("Scene.my.Point" + e.this._name + " = Scene.my.Point" + e.this._name + " -1");
e.this._name = e.other._name;
e.this.color = e.other.color;
eval("Scene.my.Point" + e.other._name + " = Scene.my.Point" + e.other._name + " +1")
~~~
