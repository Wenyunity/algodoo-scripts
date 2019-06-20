# Algicosathlon Scoreboard Code

This is an explanation of the code behind the Algicosathlon scoreboard.

**If you're looking for an explanation on how to use it, read the README instead.**

## General

I have no idea why, but making objects not glued to background speeds up the scene a lot. So that was done.

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

### Code

#### Horizontal Movement
```
    Scene.my.playAnimation ? {
        e.this._start1 ? {
            Scene.my.startTime = sim.time;
            e.this._start1 = false
        } : {
            Scene.my.animationTime = (sim.time - Scene.my.startTime) / (Scene.my.numSeconds * 1.0)
        };
        Scene.my.animationTime > 1.1 ? {
            Scene.my.playAnimation = false;
            Scene.my.playSwap = true;
            e.this._start1 = true;
            Scene.my.animationTime2 = 0.0
        } : {}
    } : {};
```
This code handles timing for the first section, updating Scene.my.animationTime from 0 to 1. Once the timing is done, it moves to the next section.

The formula used for timing is (currentTime - startTime) / (duration). This results in a linear movement from 0 to 1. This formula should be changed if a different type of movement is preferred.

#### Vertical Swapping
```
    Scene.my.playSwap ? {
        e.this._start2 ? {
            Scene.my.startTime2 = sim.time;
            e.this._start2 = false
        } : {
            Scene.my.animationTime2 = (sim.time - Scene.my.startTime2) / (Scene.my.swapSeconds * 1.0)
        };
        Scene.my.animationTime2 > 1.1 ? {
            Scene.my.playSwap = false;
            Scene.my.done = true;
            e.this._start2 = true
        } : {}
    } : {};
    Scene.my.done ? {
        e.this._timer3 = e.this._timer3 + 1
    } : {};
```
This is mostly the same as the piece of code in the horizontal version.

This piece of code updates where the bars are in their animation using Scene.my.animationTime2. It goes from 0 (when sim.time = Scene.my.startTime2) up to 1. Scene.my.swapSeconds is used to determine how long going from 0 to 1 takes. After that, it starts the cleanup function with Scene.my.done.

#### Cleanup Code
```
    Scene.my.done ? {
        e.this._timer3 = e.this._timer3 + 1
    } : {};
    e.this._timer3 > 4 ? {
        Scene.my.animationTime2 = 0.0;
        Scene.my.animationTime = 0.0;
        Scene.my.done = false;
        e.this._timer3 = 0
    } : {}
```
Scene.my.done is just a cleanup stage, so it does not need to last for very long. It lasts long enough to get the cleanup message out to the other interested parties, and then it turns itself off.

# Scoreboard Movement

The main chunk of the code is handled by the number on the scoreboard.

#### Variables

- `Scene.my.Display (+ _name)` holds the current display score.
- `Scene.my.Initial (+ _name)` holds the name of the previous score, before the event.
- `Scene.my.Point (+ _name)` holds the name of the score after the event.
- `Scene.my.Current (+ _name)` holds the current Y-Position of the bar.
- `Scene.my.Beats (+ _name)` holds the place of the athlete after the event.
- `e.this._originalY` holds the place of the athlete before the event.

## Code

The code for this section is loaded in three parts.

Scene.my.waitForAnimation -> Scene.my.horizontalAnimation -> Scene.my.verticalAnimation -> Scene.my.waitForAnimation.

## Scene.my.waitForAnimation

This part waits for the animation to happen.

There is positioning code here, although it is not 100% necessary.

#### Waiting Code

```
        Scene.my.playAnimation ? {
            e.this.postStep = Scene.my.horizontalAnimation
        } : {}
```
Waits for playAnimation before swapping the postStep to a more heavy one.

## Scene.my.HorizontalAnimation

This part handles the horizontal animation.

#### Text
```
        eval("Scene.my.Display" + e.this._name) > (-1) ? {
            eval("Scene.my.Display" + e.this._name) < 10 ? {
                e.this.size = [1.1, 1]
            } : {
                eval("Scene.my.Display" + e.this._name) < 100 ? {
                    e.this.size = [1.7, 1]
                } : {
                    eval("Scene.my.Display" + e.this._name) < 1000 ? {
                        e.this.size = [2.3, 1]
                    } : {
                        e.this.size = [2.9, 1]
                    }
                }
            }
        } : {
            eval("Scene.my.Display" + e.this._name) > (-10) ? {
                e.this.size = [1.7, 1]
            } : {
                e.this.size = [2.3, 1]
            }
        };
        textScale = 1.1;
```
In order to simulate right-align text the best I could, I change the size of the text bar when more digits are necessary.

The bottom deals with negative numbers up to -99.

textScale is a fallback incase switching digits causes the text size to decrease; it will increase the size back.

#### Position
```
        eval("Scene.my.Display" + e.this._name) > 0 ? {
            eval("e.this.pos = [Scene.my.finishSize*(Scene.my.Display" + e.this._name + ")/ (Scene.my.finishScore * 1.0), Scene.my.Current" + e.this._name + "] - [e.this.size(0) / 2, 0]")
        } : {
            eval("e.this.pos = [0, Scene.my.Current" + e.this._name + "] - [e.this.size(0) / 2, 0]")
        };
```
The order of the code matters here. If this was placed after the following code, the number would be 1 frame "ahead" of the rest of it. Otherwise, it places the numbers to the left of the end of the bar.

The positioning code also has a fallback for negative scores, so the numbers do not fly off the left.

#### Horizontal Movement
```
        e.this.text = "<markup><b>" + Math.toString(Math.toInt(eval("Scene.my.Display" + e.this._name))) + "</b></markup>";
        Scene.my.animationTime < 1 ? {
            eval("Scene.my.Display" + e.this._name + " = (Scene.my.Initial" + e.this._name + " * (1.0 - Scene.my.animationTime)) +  (Scene.my.Point" + e.this._name + " * (Scene.my.animationTime))")
        } : {
            eval("Scene.my.Display" + e.this._name + " = Scene.my.Point" + e.this._name)
        }
    } : {};
```
The first line in this statement updates the text. Since this is the only time the text needs updating, it is only present in the horizontal movement section.

Scene.my.Display is calculated as follows: Initial * (1 - animationTime) + Point * (animationTime). This means, when the animation has begun (animationTime = 0), it'll be at the Initial position, while when the animation is over (animationTime = 1), it'll be at the Point position. In between, it takes the proper ratio between the two positions.

#### Switch Code
```
        Scene.my.playSwap ? {
            e.this.postStep = Scene.my.verticalAnimation
        } : {}
```
When the horizontal animation is done, the postStep is switched to the verticalAnimation.

## Scene.my.verticalAnimation

This handles the vertical movement.

The positioning code from above is in this section.

#### Vertical Movement
```
        Scene.my.animationTime < 1 ? {
            eval("Scene.my.Current" + e.this._name + " = ((e.this._originalY) * (1.0 - Scene.my.animationTime2)) +  ((Scene.my.Beats" + e.this._name + ") * (Scene.my.animationTime2))")
        } : {
            eval("Scene.my.Current" + e.this._name + " = Scene.my.Beats" + e.this._name)
        }
```
The vertical movement is calculated in the exact same way as the horizontal movement and makes for linear movement between the starting position and the desired finishing position.

#### Cleanup
```
        Scene.my.done ? {
            e.this._originalY = e.this.pos(1);
            eval("Scene.my.Current" + e.this._name + " = e.this.pos(1)");
            e.this.postStep = Scene.my.waitForAnimation
        } : {}
    }
```
Setting variables up that will be used for future runs.

### Namebar Code
```
    eval("Scene.my.Display" + e.this._name) > 0 ? {
        eval("e.this.pos = [Scene.my.finishSize*(Scene.my.Display" + e.this._name + ")/ (Scene.my.finishScore * 1.0), Scene.my.Current" + e.this._name + "] + [e.this.size(0) / 2, 0]")
    } : {
        eval("e.this.pos = [0, Scene.my.Current" + e.this._name + "] + [e.this.size(0) / 2, 0]")
    }
```
This is the exact same as the number's positioning code except we place it to the right by adding half of the X-size instead of subtracting half of it.

### Bar Code
```
    eval("Scene.my.Display" + e.this._name) > (-1) ? {
        eval("e.this.size = [1 + Scene.my.finishSize*(Scene.my.Display" + e.this._name + ")/ (Scene.my.finishScore * 1.0), e.this.size(1)]")
    } : {};
    eval("e.this.pos = [- 0.5 + (Scene.my.finishSize * Scene.my.Display" + e.this._name + " * 1.0) / (Scene.my.finishScore * 2.0), Scene.my.Current" + e.this._name + "]")
```
The size code and the positioning code combine such that the bar looks like it's only increasing from the right side. The multiplication by 1.0 and 2.0 are to prevent integer division from happening.

There is negative handling for the size but not for the position; the latter is not entirely necessary as the position display is hidden behind the placement text.

## Sorter

### Code

`Scene.my.Beats` counts what place the marble will be in, but multiplied by negative 1 (so that first is on top and last is on the bottom.)

#### Main Comparison
```
    (eval("Scene.my.Point" + e.this._name + " < Scene.my.Point" + e.other._name)) ? {
        eval("Scene.my.Beats" + e.this._name + " = Scene.my.Beats" + e.this._name + " - 1")
    } : {};
```
This one checks if the score of the sorter bar is less than the score of the marble hitting it. If so, it subtracts 1, since the sorter has been beat.

#### Tiebreaker
```
    (eval("Scene.my.Point" + e.this._name + " == Scene.my.Point" + e.other._name)) ? {
        e.this._name > e.other._name ? {} : {
            eval("Scene.my.Beats" + e.this._name + " = Scene.my.Beats" + e.this._name + " - 1")
        }
    } : {};
    e.other.pos = e.other.pos - [0, 3]
```
In the case of the sorter bar and the marble having the same score, we use the names as a tiebreaker, since all athletes have unique names. If the name is earlier (by lexicographical sorting), then for the purposes of the tiebreaker, the sorter loses.

In the case that the sorter bar and the marble are the same, the sorter bar considers it a loss. This is because placement starts at 1; it ensures that first is properly placed at -1, and so on.

The last line of code just moves the marble down to the next sorter.

## Add Score

### Code
```
    e.other.pos = [e.other.pos(0), Scene.my.neededY];
    eval("Scene.my.Point" + e.other._name + " = Scene.my.Point" + e.other._name + " + " + e.this._pointGain);
    eval("Scene.my.Point" + e.other._name) > Scene.my.finishScore ? {
        Scene.my.finishScore = eval("Scene.my.Point" + e.other._name)
    } : {}
```
This code moves the marble down, adds the score to the marble's Point, and updates finishScore if a marble's score is higher than the current finishScore.

The ELIM box is the same, except it removes the score addition.

# How It Runs

- Step 1: Initial Score is added to Scene.my.Initial, Scene.my.Display, and Scene.my.Score.
- Step 2: Marbles add their event score to Scene.my.Score.
- Step 3: Using Scene.my.Score, the marbles go through the sorter, which finds out Scene.my.Beats for each athlete.
- Step 4: The marbles activate Scene.my.playAnimation.
- Step 5: Scene.my.Display is updated during the animation. At the end, it matches Scene.my.Score. Since the scoreboard uses Scene.my.Display, the result is a transition between Scene.my.Initial and Scene.my.Score.
- Step 6: Scene.my.playAnimation ends, starting Scene.my.swapAnimation.
- Step 7: The bars move to their proper places, using Scene.my.Beats to know where they're going to end up. Scene.my.Current is used to have a smooth transition from their original place to their new place.
- Step 8: Scene.my.swapAnimation ends, starting Scene.my.done.
- Step 9: Variables are reset. Scene.my.Initial is updated to Scene.my.Score.

# Old Code

This code had been removed because it added variables that were not necessary.

## Increase Displayed Score (For Animations) (Not Final)
```
eval("Scene.my.Display" + e.this._name + " > Scene.my.Point" + e.this._name + " ? {Scene.my.Display" + e.this._name + " = Scene.my.Display" + e.this._name + " + Scene.my.Increase" + e.this._name + " / (Scene.my.numSeconds * 1.0)} : {}")
```
This one increases the display score by Scene.my.Increase (which was Point - Display) divided by the number of seconds. While this does work, it desyncs the Increase from the animation timer. Float inefficiencies can cause the increase to lag behind the animation timer.

Also, there wasn't a failsafe installed here, meaning float inefficiencies could cause the score to be higher than initially reported.

## Move Bars Up And Down
```
eval("e.this.pos(1) - (Scene.my.Beats" + e.this._name + ") < 0.0001 && e.this.pos(1) - (Scene.my.Beats" + e.this._name + ") > (-0.0001) ?  {Scene.my.Current" + e.this._name + " = Scene.my.Beats" + e.this._name + "}  : {Scene.my.Current" + e.this._name + " = Scene.my.Current" + e.this._name + " + (((e.this._changeY) * 1.0) / (Scene.my.numSeconds * 1.0))}")
```
This one is very similar to above code, because it takes the amount it "should" move per frame using various factors. Again, it's desynced from the animation timer.

The good news is, this one does have an if statement, and a failsafe, which means that (given the time), it should end up in the correct position. However; the if statement might not work if the bar moves too fast.
