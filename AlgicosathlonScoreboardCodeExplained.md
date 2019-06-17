# Algicosathlon Scoreboard Code

This is an explanation of the code behind the Algicosathlon scoreboard.

**If you're looking for an explanation on how to use it, read the README instead.**

## General

### Naming Conventions
```
    e.this._name = math.toString(math.toInt(e.this.colorHSVA(0)) * 10000
    + math.toInt(e.this.colorHSVA(1) * 99) * 100
    + math.toInt(e.this.colorHSVA(2) * 99))
```
This is the naming convention I use for all blocks and it works to sync up the various scores.
Combined with eval(), this allows me to reuse code for each marble while not using the same variables.

## The Timing Loop

#### Variables

- `Scene.my.playAnimation` is true if the bars are currently in the process of changing size horizontally.
- `Scene.my.playSwap` is true if the bars are currently swapping places vertically.
- `Scene.my.done` is true if the animation has just finished.
- `Scene.my.numSeconds` is the amount of time (in seconds) that the bars change size horizontally.
- `Scene.my.swapSeconds` is the amount of time (in seconds) that the bars swap places vertically.
- `Scene.my.finishSize` is the size of the first place bar.
- `Scene.my.finishScore` is the score of the first place athlete.
- `Scene.my.animationTime` goes from 0 to 1 and determines where the bars are in the horizontal animation.
- `Scene.my.animationTime2` goes from 0 to 1 and determines where the bars are in the vertical swap animation.
- `e.this._timer, e.this._timer2, e.this._timer3,` are timers for all three animations.
- `e.this._start1, e.this._start2` determine whether the animation has just started or is progressing.

### Code

#### Horizontal Movement
```
    Scene.my.playAnimation ? {
        e.this._timer = e.this._timer + (1.0 / (Scene.my.numSeconds * Sim.frequency * 1.0));
        e.this._start1 ? {
            Scene.my.startTime = sim.time;
            e.this._start1 = false
        } : {
            Scene.my.animationTime = (sim.time - Scene.my.startTime) / (Scene.my.numSeconds * 1.0)
        };
        Scene.my.animationTime > 1.0 ? {
            Scene.my.animationTime = 1.0
        } : {}
    } : {};
```
This piece of code updates where the bars are in their animation using Scene.my.animationTime. It goes from 0 (when sim.time = Scene.my.startTime) up to 1. Scene.my.numSeconds is used to determine how long going from 0 to 1 takes.
```
    e.this._timer >= 1.01 ? {
        Scene.my.playAnimation = false;
        Scene.my.playSwap = true;
        e.this._timer = 0;
        e.this._start1 = true;
        Scene.my.animationTime = 0.0
    } : {};
```
This piece of code resets everything for playAnimation and starts playSwap.

#### Vertical Swapping
```
    Scene.my.playSwap ? {
        e.this._timer2 = e.this._timer2 + (1.0 / (Scene.my.swapSeconds * Sim.frequency * 1.0));
        e.this._start2 ? {
            Scene.my.startTime2 = sim.time;
            e.this._start2 = false
        } : {
            Scene.my.animationTime2 = (sim.time - Scene.my.startTime2) / (Scene.my.swapSeconds * 1.0)
        };
        Scene.my.animationTime2 > 1.0 ? {
            Scene.my.animationTime2 = 1.0
        } : {}
    } : {};
```
This is mostly the same as the piece of code in the horizontal version.

This piece of code updates where the bars are in their animation using Scene.my.animationTime2. It goes from 0 (when sim.time = Scene.my.startTime2) up to 1. Scene.my.swapSeconds is used to determine how long going from 0 to 1 takes.
```
    e.this._timer2 >= 1.01 ? {
        e.this._timer2 = 0;
        Scene.my.playSwap = false;
        Scene.my.done = true;
        e.this._start2 = true;
        Scene.my.animationTime2 = 0.0
    } : {};
```
Similarly, this piece of code just cleans up stuff for the next time around and starts Scene.my.done

#### Cleanup Code
```
    Scene.my.done ? {
        e.this._timer3 = e.this._timer3 + 1
    } : {};
    e.this._timer3 > 4 ? {
        Scene.my.done = false;
        e.this._timer3 = 0
    } : {}
```
Scene.my.done is just a cleanup stage, so it does not need to last for very long. It lasts long enough to get the cleanup message out to the other interested parties, and then it turns itself off.

## Scoreboard Movement

#### Variables

- `Scene.my.Display (+ _name)` holds the current display score.
- `Scene.my.Initial (+ _name)` holds the name of the previous score, before the event.
- `Scene.my.Point (+ _name)` holds the name of the score after the event.
- `Scene.my.Current (+ _name)` holds the current Y-Position of the bar.
- `Scene.my.Beats (+ _name)` holds the place of the athlete after the event.
- `e.this._originalY` holds the place of the athlete before the event.

### Code

#### Text
```
    eval("Scene.my.Point" + e.this._name) < 10 ? {
        e.this.size = [1.1, 1]
    } : {
        eval("Scene.my.Point" + e.this._name) < 100 ? {
            e.this.size = [1.7, 1]
        } : {
            eval("Scene.my.Point" + e.this._name) < 1000 ? {
                e.this.size = [2.3, 1]
            } : {
                e.this.size = [2.9, 1]
            }
        }
    };
```
In order to simulate right-align text the best I could, I change the size of the text bar when more digits are necessary. It's not perfect, as it sets the text based on Scene.my.Point, but Scene.my.Display doesn't work.

#### Position
```
    eval("e.this.pos = [Scene.my.finishSize*(Scene.my.Display" + e.this._name + ")/ (Scene.my.finishScore * 1.0), Scene.my.Current" + e.this._name + "] - [e.this.size(0) / 2, 0]");
```
The order of the code matters here. If this was placed after the following code, the number would be 1 frame "ahead" of the rest of it.

#### Horizontal Movement
```
    Scene.my.playAnimation ? {
        e.this.text = "<markup><b>" + Math.toString(Math.toInt(eval("Scene.my.Display" + e.this._name))) + "</b></markup>";
        Scene.my.animationTime < 1 ? {
            eval("Scene.my.Display" + e.this._name + " = (Scene.my.Initial" + e.this._name + " * (1.0 - Scene.my.animationTime)) +  (Scene.my.Point" + e.this._name + " * (Scene.my.animationTime))")
        } : {
            eval("Scene.my.Display" + e.this._name + " = Scene.my.Point" + e.this._name)
        }
    } : {};
```
The first line in this if statement updates the text. Since this is the only time the text needs updating, it can safely be placed here without worry.

Scene.my.Display is calculated as follows: Initial * (1 - animationTime) + Point * (animationTime). This means, when the animation has begun (animationTime = 0), it'll be at the Initial position, while when the animation is over (animationTime = 1), it'll be at the Point position. In between, it takes the proper ratio between the two positions.

#### Vertical Movement
```
    Scene.my.playSwap ? {
        Scene.my.animationTime < 1 ? {
            eval("Scene.my.Current" + e.this._name + " = ((e.this._originalY) * (1.0 - Scene.my.animationTime2)) +  ((Scene.my.Beats" + e.this._name + ") * (Scene.my.animationTime2))")
        } : {
            eval("Scene.my.Current" + e.this._name + " = Scene.my.Beats" + e.this._name)
        }
    } : {};
```
The vertical movement is calculated in the exact same way as the horizontal movement and makes for linear movement between the starting position and the desired finishing position.

#### Cleanup
```
    Scene.my.done ? {
        e.this._originalY = e.this.pos(1);
        eval("Scene.my.Current" + e.this._name + " = e.this.pos(1)")
    } : {}
```
Setting variables up that will be used for future runs.

### Namebar Code
```
    eval("e.this.pos = [Scene.my.finishSize*(Scene.my.Display" + e.this._name + ")/ (Scene.my.finishScore * 1.0), Scene.my.Current" + e.this._name + "] + [e.this.size(0) / 2, 0]")
```
This is the exact same as the number's positioning code except we place it to the right by adding half of the X-size instead of subtracting half of it.

### Bar Code
```
   eval("e.this.size = [1 + Scene.my.finishSize*(Scene.my.Display" + e.this._name + ")/ (Scene.my.finishScore * 1.0), e.this.size(1)]");
    eval("e.this.pos = [- 0.5 + (Scene.my.finishSize * Scene.my.Display" + e.this._name + " * 1.0) / (Scene.my.finishScore * 2.0), Scene.my.Current" + e.this._name + "]")
```
The size code and the positioning code combine such that the bar looks like it's only increasing from the right side. The multiplication by 1.0 and 2.0 are to prevent integer division from happening.

# Old Code

Probably to be deleted.

## Text Display
~~~
eval("Scene.my.Display" + e.this._name + " = Math.toint(e.this.text)")
~~~

## Counting How Many Marbles are Ahead
~~~
eval("Scene.my.Point" + e.this._name + " < Scene.my.Point" + e.other._name + " ? {Scene.my.Beats" + e.this._name + " = Scene.my.Beats" + e.this._name + " - 1} : {}");
~~~

## Tiebreaker for Marbles Ahead
~~~
eval("Scene.my.Point" + e.this._name + " == Scene.my.Point" + e.other._name + " ? {" + e.this._name + " > " + e.other._name + " ? {} : {Scene.my.Beats" + e.this._name + " = Scene.my.Beats" + e.this._name + " - 1}} : {}")
~~~

## Marbles Ahead Text
~~~
e.this.text = Math.toString(eval("Scene.my.Beats" + e.this._name))
~~~

## Increase Displayed Score (For Animations) (Not Final)
~~~
eval("Scene.my.Display" + e.this._name + " > Scene.my.Point" + e.this._name + " ? {Scene.my.Display" + e.this._name + " = Scene.my.Display" + e.this._name + " + Scene.my.Increase" + e.this._name + " / (Scene.my.numSeconds * 1.0)} : {}")
~~~

## Move Bars Up And Down
~~~
eval("e.this.pos(1) - (Scene.my.Beats" + e.this._name + ") < 0.0001 && e.this.pos(1) - (Scene.my.Beats" + e.this._name + ") > (-0.0001) ?  {Scene.my.Current" + e.this._name + " = Scene.my.Beats" + e.this._name + "}  : {Scene.my.Current" + e.this._name + " = Scene.my.Current" + e.this._name + " + (((e.this._changeY) * 1.0) / (Scene.my.numSeconds * 1.0))}")
~~~
