# Other Functions

Some functions that work but don't need the use of README.md

# Integer Aligning
Aligns objects to the nearest integer. Aligning across x = 0 or y = 0 is not recommended because toInt rounds by truncation.
```
pos = [math.toint(pos(0)), math.toint(pos(1))]
```

# Teleport (With slightly random position)
Scene.my.restartPoint = The center of the possible teleportation.

Replace the 4.0 with the desired side-length of the teleportation variance. Both sides do not have to be the same number.
```
e.other.pos = Scene.my.restartPoint + [(rand.uniform01 - 0.5) * 4.0, (rand.uniform01 - 0.5) * 4.0]
```

# WuigiBaka's Timer
Uses M:SS.x format.

### In OnSpawn
```
Scene.my.timer = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
```

### In postStep
```
e.this.text = math.toString(math.toInt(sim.time / 60)) + ":" + Scene.my.timer(math.toInt(sim.time % 60)) + "." + math.toString(math.toInt((sim.time % 1) * 10))
```

# WuigiBaka's Countdown Timer
Uses M:SS.x format.

Set Scene.my.FinishTime to the number of _seconds_ the timer should start counting down at. Ex: 60 = 1 min., 120 = 2 min.

### In OnSpawn
```
Scene.my.timer = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
```

### In postStep
```
e.this._timer = scene.my.FinishTime - sim.time;
e.this.text = math.toString(math.toInt(_timer / 60)) + ":" + scene.my.timer(math.toInt(_timer % 60)) + "." + math.toString(math.toInt((_timer % 1) * 10));
```

Add this if you want the simulation to stop when the time is over.
### Stop Sim When Time Is Up (postStep)
```
e.this._timer < 0 ? {
    sim.running = false
} : {}
```
