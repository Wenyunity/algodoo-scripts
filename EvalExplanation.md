# Eval

eval() is a function often seen in my functions. This document will explain what eval is and why it's useful.

# What is eval?

Eval takes a string and runs it as code. For example: ` eval("x = x + 1") ` will run the code `x = x + 1`.

# Why is that useful?

In the example above, eval just makes the code look longer. However; eval has some good uses. Here are a few:

- Functioning like a case-switch, avoiding long IF chains.
- Being able to copy code across multiple objects that perform the same function but with different variables.

## Case-Switch

Suppose there are three marbles: Red, Yellow, and Blue. 

Now, there's a block that gives one point to the marbles. 

The marble's points are in Scene.my.ScoreRed, Scene.my.ScoreYellow, and Scene.my.ScoreBlue respectively. Red, Yellow, and Blue also have \_name variables which stores their name (Red, Yellow, Blue).

Using if statements, the code would look like this:

```
e.other._name == "Red" ? 
  {Scene.my.ScoreRed = Scene.my.ScoreRed + 1} : {}
e.other._name == "Yellow" ? 
  {Scene.my.ScoreYellow = Scene.my.ScoreYellow + 1} : {}
e.other._name == "Blue" ? 
  {Scene.my.ScoreBlue = Scene.my.ScoreBlue + 1} : {}
```
(The alternate option is to use nested IF statements, but that's not much better)

With eval, that code can be simplified to this:

```
eval("Scene.my.Score" + e.other._name + " = Scene.my.Score" + e.other._name + " + 1")
```

The other point in eval's favor: Suppose Green joins the race.

- Another if statement would need to be added to accomodate Green.
- The eval code **does not need to be changed**.

#### A Side-Note on Local Variables

It would be possible to store marble's scores locally (In this example, \_score is used), which would produce this code for the block that gives points:

```
e.other._score = e.other._score + 1
```

However; suppose there are **five** Red marbles, each with their own \_score. There is no easy way to combine all of the Red marbles' scores. 

Thus, for more flexibility, global variables should be used if more than one object may need it. (Even if there's only one Red marble, the scoreboard will still need to access Red's score.)

## Copying Similar Code

Suppose that each marble has a block that displays their score.

Without eval, this is what would happen:

- Red: `e.this.text = Math.toString(Scene.my.ScoreRed)`
- Yellow: `e.this.text = Math.toString(Scene.my.ScoreYellow)`
- Blue: `e.this.text = Math.toString(Scene.my.ScoreBlue)`

With eval, the same code can be used for all three blocks, assuming they have the appropriate \_name parameter.

```
e.this.text = Math.toString(eval("Scene.my.Score" + e.this._name))
```

The eval text has some advantages.

For example, suppose the code that needs to be copied isn't short, but rather looks like this (If you want to know what it does, look at the [Scene.my.verticalAnimation section here)](https://github.com/Wenyunity/algodoo-eval-scoreboard/blob/master/AlgicosathlonScoreboardCodeExplained.md):

```
        eval("Scene.my.Display" + e.this._name) > 0 ? {
            eval("e.this.pos = [Scene.my.finishSize*(Scene.my.Display" + e.this._name + ")/ (Scene.my.finishScore * 1.0), Scene.my.Current" + e.this._name + "] - [e.this.size(0) / 2, 0]")
        } : {
            eval("e.this.pos = [0, Scene.my.Current" + e.this._name + "] - [e.this.size(0) / 2, 0]")
        };
        Scene.my.animationTime2 < 1 ? {
            eval("Scene.my.Current" + e.this._name + " = ((e.this._originalY) * (1.0 - Scene.my.animationTime2)) +  ((Scene.my.Beats" + e.this._name + ") * (Scene.my.animationTime2))")
        } : {
            eval("Scene.my.Current" + e.this._name + " = Scene.my.Beats" + e.this._name)
        };
        Scene.my.done ? {
            e.this._originalY = e.this.pos(1);
            eval("Scene.my.Current" + e.this._name + " = e.this.pos(1)");
            e.this.postStep = Scene.my.waitForAnimation
        } : {}
```

Without the use of eval, there are **9** places where the text would need to be changed for each block. With the use of eval, none of this needs to change between blocks.

And, since nothing needs to change, we can also put this whole long piece of code within a function **only if we use eval.**

```
    Scene.my.verticalAnimation = (e)=>{
    \\ Insert all of that code in here
    }
```

This allows the ability to select all of the blocks, and then type in `e.this.postStep = Scene.my.verticalAnimation` in the top-left box of the scripting menu. It'll automatically put all of that code in each block.

## Limitations

Since eval is a function, it evaluates first. That means this doesn't work to set a marble's score to 10.

```
eval("Scene.my.Score" + e.other._name) = 10
```

Suppose \_name = Red, and Scene.my.ScoreRed = 5.

The code would run in this order:

```
eval("Scene.my.Score" + e.other._name) = 10
eval("Scene.my.ScoreRed") = 10
5 = 10
```

`5 = 10` isn't even a valid function!

On the other hand, comparisons do work.

```
eval("Scene.my.Score" + e.other._name) == 10
eval("Scene.my.ScoreRed") == 10
5 == 10
false
```

Do note that putting the eval on the other side does work, even if this example is a little bit silly:

```
e.this.collideSet = eval("Scene.my.Score" + e.other._name)
e.this.collideSet = eval("Scene.my.ScoreRed")
e.this.collideSet = 5
```

In order to set a marble's score to 10, this is necessary:
```
eval("Scene.my.Score" + e.other._name + " = 10")
```

Another limitation: Eval requires organization to work. In the examples above, all relevant objects need the \_name parameter for eval to function correctly. If the objects don't have a \_name parameter, or the \_name parameter is set incorrectly, then there will be undesirable results.
