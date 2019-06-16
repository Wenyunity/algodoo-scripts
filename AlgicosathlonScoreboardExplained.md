# AlgicosathlonScoreboardExplained

Work in Progress. Explanations and more functions to be added.

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
