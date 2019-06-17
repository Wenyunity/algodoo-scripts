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
