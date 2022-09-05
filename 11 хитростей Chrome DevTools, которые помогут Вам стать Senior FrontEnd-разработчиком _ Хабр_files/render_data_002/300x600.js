(function (cjs, an) {

var p; // shortcut to reference prototypes
var lib={};var ss={};var img={};
lib.ssMetadata = [
		{name:"300x600_atlas_P_1", frames: [[94,444,60,60],[182,0,108,174],[0,212,150,195],[152,212,150,195],[0,409,92,72],[0,0,180,210],[386,222,120,140],[304,0,80,220],[386,0,80,220],[304,222,80,220],[386,364,72,105]]},
		{name:"300x600_atlas_NP_1", frames: [[0,0,420,660],[422,0,210,690]]}
];


(lib.AnMovieClip = function(){
	this.actionFrames = [];
	this.ignorePause = false;
	this.gotoAndPlay = function(positionOrLabel){
		cjs.MovieClip.prototype.gotoAndPlay.call(this,positionOrLabel);
	}
	this.play = function(){
		cjs.MovieClip.prototype.play.call(this);
	}
	this.gotoAndStop = function(positionOrLabel){
		cjs.MovieClip.prototype.gotoAndStop.call(this,positionOrLabel);
	}
	this.stop = function(){
		cjs.MovieClip.prototype.stop.call(this);
	}
}).prototype = p = new cjs.MovieClip();
// symbols:



(lib.hand3006001 = function() {
	this.initialize(ss["300x600_atlas_NP_1"]);
	this.gotoAndStop(0);
}).prototype = p = new cjs.Sprite();



(lib.logomi300600 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(0);
}).prototype = p = new cjs.Sprite();



(lib.woman3006001 = function() {
	this.initialize(ss["300x600_atlas_NP_1"]);
	this.gotoAndStop(1);
}).prototype = p = new cjs.Sprite();



(lib.woman30060021 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(1);
}).prototype = p = new cjs.Sprite();



(lib.woman30060031 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(2);
}).prototype = p = new cjs.Sprite();



(lib.woman30060033 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(3);
}).prototype = p = new cjs.Sprite();



(lib.woman3006004 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(4);
}).prototype = p = new cjs.Sprite();



(lib.womanglowmin300600 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(5);
}).prototype = p = new cjs.Sprite();



(lib.womanglowminnew1 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(6);
}).prototype = p = new cjs.Sprite();



(lib.womanglowrhand1 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(7);
}).prototype = p = new cjs.Sprite();



(lib.womanglowrhand2 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(8);
}).prototype = p = new cjs.Sprite();



(lib.womanglowrhand3 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(9);
}).prototype = p = new cjs.Sprite();



(lib.womanglowrhandphone300600 = function() {
	this.initialize(ss["300x600_atlas_P_1"]);
	this.gotoAndStop(10);
}).prototype = p = new cjs.Sprite();
// helper functions:

function mc_symbol_clone() {
	var clone = this._cloneProps(new this.constructor(this.mode, this.startPosition, this.loop, this.reversed));
	clone.gotoAndStop(this.currentFrame);
	clone.paused = this.paused;
	clone.framerate = this.framerate;
	return clone;
}

function getMCSymbolPrototype(symbol, nominalBounds, frameBounds) {
	var prototype = cjs.extend(symbol, cjs.MovieClip);
	prototype.clone = mc_symbol_clone;
	prototype.nominalBounds = nominalBounds;
	prototype.frameBounds = frameBounds;
	return prototype;
	}


(lib.whandphonephone = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.instance = new lib.womanglowrhandphone300600();
	this.instance.setTransform(0,0,0.6667,0.6667);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whandphonephone, new cjs.Rectangle(0,0,48,70), null);


(lib.whandphoneglow3 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.womanglowrhand3();

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whandphoneglow3, new cjs.Rectangle(0,0,80,220), null);


(lib.whandphoneglow2 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.womanglowrhand2();

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whandphoneglow2, new cjs.Rectangle(0,0,80,220), null);


(lib.whandphoneglow1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.womanglowrhand1();

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whandphoneglow1, new cjs.Rectangle(0,0,80,220), null);


(lib.whandminladon = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.instance = new lib.woman3006004();
	this.instance.setTransform(0,0,0.663,0.6632);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whandminladon, new cjs.Rectangle(0,0,61,47.8), null);


(lib.whandminglow1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.instance = new lib.womanglowminnew1();

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whandminglow1, new cjs.Rectangle(0,0,120,140), null);


(lib.whand31 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.instance = new lib.woman30060033();
	this.instance.setTransform(0,0,0.6667,0.6667);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whand31, new cjs.Rectangle(0,0,100,130), null);


(lib.whand21 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.instance = new lib.woman30060031();
	this.instance.setTransform(0,0,0.6667,0.6667);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whand21, new cjs.Rectangle(0,0,100,130), null);


(lib.whand11 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.instance = new lib.woman30060021();
	this.instance.setTransform(0,0,0.6667,0.6667);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.whand11, new cjs.Rectangle(0,0,72,116), null);


(lib.wbody1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_4 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("EgC1AiaQhGkigkiiQgciAgnjDQgnjKgMhSQgMhLAGiPQAEh8AKg1QAFgeBSkRQBQkNABgLQAJhBgCgjQgBgQgZg0QgjhJgHgSIhcjrIhBhqQhIh3gjhGQglhLgHhtQgFhSALhSQAHg1ALgjIAJgYIg3hpQgLgVAHgOQAEgHAUgQQAMgLAYgHQAMgEAKgCQgDgGgEgMQgEgRAXghQAJgNADgMIAIggIASg3IgOgVQgNgYACgNQACgMALgMIAegiQAVgaAWg1QAYg3ARhBQAThIA0h3QA4iAAignQAhglBTgYQBJgUAkAGQAYAEAXAAIA0gBQAgAAAoAYQAjAUAyArQArAlAtBOQAoBFAJAnIAVBwQARBUANAfQAMAcAaAyQAdA2AIASQANAcAHA5QAFApAAAiQAAAUgEAIIgQARQgIAJAMAKQAYATAHAKQAPAUgKAlQgGAWgRAkQgJAUgVAVQgKALgIAHIALAmQANAtAHAeIAWBbQAOA+AJAdIAgBlQAWBJAGAqQAHAugMBAQgLA2gRAkQgIARgSAeQgNATgDAOQgGAfgCAUQgEApABA0QABAygDBBIgDBXQgCAmAJBjQAJBrAKAiQAPAwARCLQAVCnACCPQACCFgjD/QgSCAgTBlIiCLzg");
	mask.setTransform(71.6269,239.1821);

	// Layer_3
	this.instance = new lib.woman3006001();
	this.instance.setTransform(0,0,0.6667,0.6667);

	var maskedShapeInstanceList = [this.instance];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.wbody1, new cjs.Rectangle(8.9,19,125.5,440.4), null);


(lib.text6 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AAAAVIARgUIgRgTIAAgUIAgAjIAAAHIggAjgAgeAUIAQgUIgQgSIAAgTIAeAiIAAAHIgeAig");
	this.shape.setTransform(129.65,81.775);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AglBBIAAgOIADgEIAJgLIAKgNIAKgLIAFgGQAGgIAEgJQAFgJAAgJQAAgKgFgFQgEgFgJAAIgIABIgHACIAAASIgPAAIAAgbQAGgFAIgCQAJgCAJAAQARAAAIAJQAJAJAAAPQAAAJgDAIQgDAHgEAHIgLAOIgFAFIgHAKIgJALIgIAKIA3AAIAAAPg");
	this.shape_1.setTransform(121.3,80.025);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgYAiQgLgLAAgXQAAgNAFgKQAFgKAIgFQAJgFAKAAQAKAAAHADQAIAEAEAIQAFAIAAAMIAAAGIgBAEIg0AAQAAAOAHAHQAGAHAMAAQAHAAAGgCQAHgCAFgEIAAAPQgEAEgHACQgIABgJAAQgSAAgLgKgAATgJQAAgLgFgFQgFgFgIAAQgHAAgFAFQgFAFgBALIAkAAIAAAAg");
	this.shape_2.setTransform(112.775,82.225);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("AgHBAIAAhxIgNAAIAAgOIAcAAIAABxIANAAIAAAOg");
	this.shape_3.setTransform(105.925,80.125);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AgYAiQgLgLAAgXQAAgNAFgKQAFgKAIgFQAJgFAKAAQAKAAAHADQAIAEAEAIQAFAIAAAMIAAAGIgBAEIg0AAQAAAOAHAHQAGAHAMAAQAHAAAGgCQAHgCAFgEIAAAPQgEAEgHACQgIABgJAAQgSAAgLgKgAATgJQAAgLgFgFQgFgFgIAAQgHAAgFAFQgFAFgBALIAkAAIAAAAg");
	this.shape_4.setTransform(99.625,82.225);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AgXBAIAAgPIAPAAIAAhhIgYAAIAAAUIgPAAIAAgjIBfAAIAAAjIgPAAIAAgUIgYAAIAABhIAPAAIAAAPg");
	this.shape_5.setTransform(90.325,80.125);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AAGA7IAAgOIANAAIAAguIgBAAIgjA8IgeAAIAAgOIAOAAIAAg5IgOAAIAAgOIAqAAIAAAOIgMAAIAAAwIAAAAIAkg+IAdAAIAAAOIgNAAIAAA5IANAAIAAAOgAgRgpQgHgFAAgMIAOAAQAAAFADADQACADAFABQAGgBADgDQADgDAAgFIAOAAQAAAMgHAGQgHAGgMAAQgKAAgHgHg");
	this.shape_6.setTransform(74.925,80.6);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AgTAnQgJgFgFgKQgFgKAAgOQAAgNAFgKQAFgKAJgFQAJgFAKAAQALAAAJAFQAJAFAFAKQAFAKAAANQAAAOgFAKQgFAKgJAFQgJAFgLAAQgKAAgJgFgAgKgaQgFADgDAHQgDAHAAAJQAAALADAGQADAHAFADQAFADAFAAQAGAAAFgDQAFgDADgHQADgGAAgLQAAgJgDgHQgDgHgFgDQgFgDgGAAQgFAAgFADg");
	this.shape_7.setTransform(65.025,82.225);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AApBAIAAhvIgBAAIgiBvIgOAAIgihvIgBAAIAABvIgdAAIAAgPIAOAAIAAhhIgOAAIAAgPIArAAIAdBjIABAAIAehjIAqAAIAAAPIgPAAIAABhIAPAAIAAAPg");
	this.shape_8.setTransform(52.675,80.125);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AgeAEIAAgHIAfgjIAAASIgRAUIARATIAAAUgAAAAEIAAgHIAggiIAAATIgSASIASATIAAATg");
	this.shape_9.setTransform(40.85,81.775);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("AAGArIAAgOIANAAIAAgvIgBAAIgjA9IgeAAIAAgOIAOAAIAAg5IgOAAIAAgOIAqAAIAAAOIgMAAIAAAwIAAAAIAkg+IAdAAIAAAOIgNAAIAAA5IANAAIAAAOg");
	this.shape_10.setTransform(162.925,60.375);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AAWArIgagmIgIACIAAAWIALAAIAAAOIgpAAIAAgOIAOAAIAAg5IgOAAIAAgOIAeAAIAAAlIAIgCIAQgVIgHAAIAAgOIAjAAIAAAOIgLAAIgVAZIAZAgIAKAAIAAAOg");
	this.shape_11.setTransform(152.925,60.375);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AAGA7IAAgOIANAAIAAgvIgBAAIgjA9IgeAAIAAgOIAOAAIAAg5IgOAAIAAgOIAqAAIAAAOIgMAAIAAAwIAAAAIAkg+IAdAAIAAAOIgNAAIAAA5IANAAIAAAOgAgRgoQgHgHAAgLIAOAAQAAAFADADQACADAFAAQAGAAADgDQADgDAAgFIAOAAQAAAMgHAGQgHAGgMAAQgKAAgHgGg");
	this.shape_12.setTransform(142.625,58.75);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#FFFFFF").s().p("AgYAiQgLgLAAgXQAAgNAFgKQAFgKAIgFQAJgFAKAAQAKAAAHADQAIAEAEAIQAFAIAAAMIAAAGIgBAEIg0AAQAAAOAHAHQAGAHAMAAQAHAAAGgCQAHgCAFgEIAAAPQgEAEgHACQgIABgJAAQgSAAgLgKgAATgJQAAgLgFgFQgFgFgIAAQgHAAgFAFQgFAFgBALIAkAAIAAAAg");
	this.shape_13.setTransform(133.075,60.375);

	this.shape_14 = new cjs.Shape();
	this.shape_14.graphics.f("#FFFFFF").s().p("AAQArIAAgmIgfAAIAAAYIAMAAIAAAOIgpAAIAAgOIANAAIAAg5IgNAAIAAgOIAdAAIAAAjIAfAAIAAgVIgMAAIAAgOIApAAIAAAOIgNAAIAAA5IANAAIAAAOg");
	this.shape_14.setTransform(123.725,60.375);

	this.shape_15 = new cjs.Shape();
	this.shape_15.graphics.f("#FFFFFF").s().p("AAGArIAAgOIANAAIAAgvIgBAAIgjA9IgeAAIAAgOIAOAAIAAg5IgOAAIAAgOIAqAAIAAAOIgMAAIAAAwIAAAAIAkg+IAdAAIAAAOIgNAAIAAA5IANAAIAAAOg");
	this.shape_15.setTransform(113.175,60.375);

	this.shape_16 = new cjs.Shape();
	this.shape_16.graphics.f("#FFFFFF").s().p("AgoArIgCAAIAAgQIACABIADAAQAIAAAEgPQAEgOAAgcIgNAAIAAgNIBNAAIAAANIgOAAIAAA6IAOAAIAAANIgeAAIAAhGIgTAAIgBAcQgBAMgEAKQgCAKgHAGQgFAFgJAAIgFAAg");
	this.shape_16.setTransform(102.9,60.425);

	this.shape_17 = new cjs.Shape();
	this.shape_17.graphics.f("#FFFFFF").s().p("AAUArIgVghIgMATIAIAAIAAAOIghAAIAAgOIAKAAIATgdIgSgcIgMAAIAAgOIAVAAIAVAhIAMgTIgJAAIAAgOIAhAAIAAAOIgJAAIgUAcIAUAdIAKAAIAAAOg");
	this.shape_17.setTransform(89.1,60.375);

	this.shape_18 = new cjs.Shape();
	this.shape_18.graphics.f("#FFFFFF").s().p("AgbApQgGgDgDgFQgCgFAAgHQgBgPANgGQAMgHAYAAIAAgEQAAgJgFgFQgFgEgJAAIgMABQgGACgGAEIAAgPQAGgEAHgBIANgBQARAAAIAIQAIAJAAAPIAAAoIANAAIAAAOIgcAAIAAgOIgBAAIgGAIQgDAEgEACQgEABgHAAQgIAAgFgDgAgOAHQgIAEABAJQAAAEADADQADAEAGAAQAGAAADgDQAEgCADgGQADgFAAgIIAAgEQgRAAgHAEg");
	this.shape_18.setTransform(80.324,60.375);

	this.shape_19 = new cjs.Shape();
	this.shape_19.graphics.f("#FFFFFF").s().p("AgWBVIAAgNIAPAAIAAgcQgPAAgKgGQgJgFgGgKQgFgKAAgNQAAgMAFgKQAFgKAKgFQAKgGAPAAIAAgcIgNAAIAAgNIAcAAIAAApQAOAAAKAGQAKAFAFAKQAGAKAAAMQgBANgFAKQgFAKgKAFQgKAGgOAAIAAAcIAPAAIAAANgAAIAfQANgBAHgIQAHgIAAgOQAAgOgHgHQgHgIgNgBgAgbgVQgIAIAAANQAAAPAIAHQAHAIANABIAAg9QgNABgHAIg");
	this.shape_19.setTransform(69.925,60.375);

	this.shape_20 = new cjs.Shape();
	this.shape_20.graphics.f("#FFFFFF").s().p("AAGArIAAgOIANAAIAAgvIgBAAIgjA9IgeAAIAAgOIAOAAIAAg5IgOAAIAAgOIAqAAIAAAOIgMAAIAAAwIAAAAIAkg+IAdAAIAAAOIgNAAIAAA5IANAAIAAAOg");
	this.shape_20.setTransform(58.675,60.375);

	this.shape_21 = new cjs.Shape();
	this.shape_21.graphics.f("#FFFFFF").s().p("AgsBBIAAgOIANAAIAAhkIgNAAIAAgNIAdAAIAAAMIABAAQADgGAHgEQAFgEAKAAQAKAAAIAFQAHAGAEAJQAFAKAAAOQAAAOgFAJQgEAKgHAGQgIAFgKAAQgJAAgGgEQgGgDgEgHIgBAAIABAOIAAAbIANAAIAAAOgAgIgsQgHAGABAMIAAAMQAAAIACAGQADAEAFADQAEADAGAAQAHAAAEgDQAFgEADgFQADgHAAgLQAAgKgEgHQgCgHgFgDQgEgDgHAAQgIAAgGAGg");
	this.shape_21.setTransform(48.25,62.425);

	this.shape_22 = new cjs.Shape();
	this.shape_22.graphics.f("#FFFFFF").s().p("AgbApQgGgDgDgFQgCgFAAgHQgBgPANgGQAMgHAYAAIAAgEQAAgJgFgFQgFgEgJAAIgMABQgGACgGAEIAAgPQAGgEAHgBIANgBQARAAAIAIQAIAJAAAPIAAAoIANAAIAAAOIgcAAIAAgOIgBAAIgGAIQgDAEgEACQgEABgHAAQgIAAgFgDgAgOAHQgIAEABAJQAAAEADADQADAEAGAAQAGAAADgDQAEgCADgGQADgFAAgIIAAgEQgRAAgHAEg");
	this.shape_22.setTransform(39.024,60.375);

	this.shape_23 = new cjs.Shape();
	this.shape_23.graphics.f("#FFFFFF").s().p("AgWArIAAgOIAPAAIAAg5IgRAAIAAARIgNAAIAAgfIBLAAIAAAfIgNAAIAAgRIgRAAIAAA5IAPAAIAAAOg");
	this.shape_23.setTransform(30.3,60.375);

	this.shape_24 = new cjs.Shape();
	this.shape_24.graphics.f("#FFFFFF").s().p("AgbApQgGgDgDgFQgCgFAAgHQgBgPANgGQAMgHAYAAIAAgEQAAgJgFgFQgFgEgJAAIgMABQgGACgGAEIAAgPQAGgEAHgBIANgBQARAAAIAIQAIAJAAAPIAAAoIANAAIAAAOIgcAAIAAgOIgBAAIgGAIQgDAEgEACQgEABgHAAQgIAAgFgDgAgOAHQgIAEABAJQAAAEADADQADAEAGAAQAGAAADgDQAEgCADgGQADgFAAgIIAAgEQgRAAgHAEg");
	this.shape_24.setTransform(16.974,60.375);

	this.shape_25 = new cjs.Shape();
	this.shape_25.graphics.f("#FFFFFF").s().p("AAQArIAAgmIgfAAIAAAYIAMAAIAAAOIgpAAIAAgOIANAAIAAg5IgNAAIAAgOIAdAAIAAAjIAfAAIAAgVIgMAAIAAgOIApAAIAAAOIgNAAIAAA5IANAAIAAAOg");
	this.shape_25.setTransform(7.225,60.375);

	this.shape_26 = new cjs.Shape();
	this.shape_26.graphics.f("#FFFFFF").s().p("AglBBIAAgOIAEgEIAIgLIAKgNIAKgLIAFgGQAGgIAFgJQAEgJAAgJQAAgKgFgFQgEgFgJAAIgIABIgHACIAAASIgPAAIAAgbQAGgFAIgCQAJgCAJAAQAQAAAJAJQAJAJAAAPQAAAJgDAIQgDAHgEAHIgLAOIgFAFIgHAKIgJALIgIAKIA3AAIAAAPg");
	this.shape_26.setTransform(134,36.325);

	this.shape_27 = new cjs.Shape();
	this.shape_27.graphics.f("#FFFFFF").s().p("AglBBIAAgOIADgEIAJgLIAKgNIAJgLIAGgGQAGgIAEgJQAFgJAAgJQAAgKgFgFQgFgFgIAAIgIABIgHACIAAASIgPAAIAAgbQAGgFAIgCQAJgCAJAAQARAAAIAJQAJAJAAAPQAAAJgDAIQgCAHgFAHIgMAOIgEAFIgHAKIgJALIgIAKIA3AAIAAAPg");
	this.shape_27.setTransform(125.25,36.325);

	this.shape_28 = new cjs.Shape();
	this.shape_28.graphics.f("#FFFFFF").s().p("AAABBQgUABgKgRQgLgQAAggQAAghALgRQAKgQAUABQAVgBALAQQAKARAAAgQAAAigKAPQgLARgUAAIgBgBgAgNgrQgGAGgCALQgCAMAAAPQAAAPACALQACALAGAHQAFAFAIABQAJgBAFgFQAGgHADgLQABgLAAgQQAAgOgBgMQgDgLgGgGQgFgGgJgBQgIABgFAGg");
	this.shape_28.setTransform(116,36.4);

	this.shape_29 = new cjs.Shape();
	this.shape_29.graphics.f("#FFFFFF").s().p("AglBBIAAgOIADgEIAJgLIAKgNIAJgLIAGgGQAGgIAEgJQAFgJAAgJQAAgKgFgFQgFgFgIAAIgIABIgHACIAAASIgPAAIAAgbQAGgFAJgCQAIgCAJAAQARAAAIAJQAJAJAAAPQAAAJgDAIQgCAHgFAHIgMAOIgEAFIgHAKIgJALIgIAKIA3AAIAAAPg");
	this.shape_29.setTransform(106.7,36.325);

	this.shape_30 = new cjs.Shape();
	this.shape_30.graphics.f("#FFFFFF").s().p("AgHAIQgDgDAAgFQAAgEADgDQAEgDADgBQAFABADADQADADAAAEQAAAFgDADQgDAEgFAAQgDAAgEgEg");
	this.shape_30.setTransform(100.2,41.85);

	this.shape_31 = new cjs.Shape();
	this.shape_31.graphics.f("#FFFFFF").s().p("AgTA9QgJgEgEgHQgEgHgBgKIAQAAQABAJAFAEQAGAFAJAAQAJgBAFgGQAGgHACgLQACgLABgNIgBAAQgDAFgHAFQgHAEgJAAQgMAAgIgFQgJgFgFgIQgEgJAAgMQAAgNAEgJQAGgJAJgFQAJgFAMAAQATgBAMAOQAKAPABAdQAAAUgFARQgDAQgJAKQgKAJgQAAQgLAAgHgEgAgLgvQgFADgDAGQgEAGAAAJQAAAIAEAGQADAGAFADQAFACAGAAQAKAAAGgGQAHgHAAgNQAAgHgEgGQgCgGgGgEQgFgDgGAAQgGAAgFADg");
	this.shape_31.setTransform(93.3,36.4241);

	this.shape_32 = new cjs.Shape();
	this.shape_32.graphics.f("#FFFFFF").s().p("AAABBQgUABgKgRQgLgQAAggQAAghALgRQAKgQAUABQAVgBALAQQAKARAAAgQAAAigKAPQgLARgUAAIgBgBgAgNgrQgGAGgCALQgCAMAAAPQAAAPACALQACALAGAHQAFAFAIABQAJgBAFgFQAGgHADgLQABgLAAgQQAAgOgBgMQgDgLgGgGQgFgGgJgBQgIABgFAGg");
	this.shape_32.setTransform(83.6,36.4);

	this.shape_33 = new cjs.Shape();
	this.shape_33.graphics.f("#FFFFFF").s().p("AgHAIQgDgDAAgFQAAgEADgDQADgDAEgBQAFABADADQAEADgBAEQABAFgEADQgDAEgFAAQgEAAgDgEg");
	this.shape_33.setTransform(76.55,41.85);

	this.shape_34 = new cjs.Shape();
	this.shape_34.graphics.f("#FFFFFF").s().p("AAABBQgUABgKgRQgLgQAAggQAAghALgRQAKgQAUABQAVgBALAQQAKARAAAgQAAAigKAPQgLARgUAAIgBgBgAgNgrQgGAGgCALQgCAMAAAPQAAAPACALQACALAGAHQAFAFAIABQAJgBAGgFQAFgHADgLQABgLABgQQgBgOgBgMQgDgLgFgGQgGgGgJgBQgIABgFAGg");
	this.shape_34.setTransform(69.55,36.4);

	this.shape_35 = new cjs.Shape();
	this.shape_35.graphics.f("#FFFFFF").s().p("AgSA+QgIgEgFgHQgFgIgBgNIAQAAQABAJAFAGQAFAFAKABQAFAAAFgDQAFgDACgGQADgFAAgIQAAgLgGgGQgHgGgKAAIgGAAIgFABIAAgOQAPgCAHgGQAHgGAAgJQAAgIgFgFQgFgEgHAAIgIABIgHACIAAASIgPAAIAAgbQAGgEAIgDQAIgCAKAAQAKAAAIAEQAHAEAEAGQAEAHAAAIQAAAIgEAGQgDAGgGAEQgFAEgGACIAAAAQAOACAIAIQAHAIAAAOQAAAKgEAJQgEAJgJAGQgIAFgNAAIgCABQgIAAgIgEg");
	this.shape_35.setTransform(60.125,36.4031);

	this.shape_36 = new cjs.Shape();
	this.shape_36.graphics.f("#FFFFFF").s().p("AgTAnQgJgFgFgKQgFgKAAgOQAAgNAFgKQAFgKAJgFQAJgFAKAAQALAAAJAFQAJAFAFAKQAFAKAAANQAAAOgFAKQgFAKgJAFQgJAFgLAAQgKAAgJgFgAgKgaQgFADgDAHQgDAHAAAJQAAALADAGQADAHAFADQAFADAFAAQAGAAAFgDQAFgDADgHQADgGAAgLQAAgJgDgHQgDgHgFgDQgFgDgGAAQgFAAgFADg");
	this.shape_36.setTransform(46.375,38.525);

	this.shape_37 = new cjs.Shape();
	this.shape_37.graphics.f("#FFFFFF").s().p("AAfA2IgBgWIg7AAIgBAWIgOAAIAAgkIAIAAQAEgFADgHIAEgSIADgbIgOAAIAAgOIBPAAIAAAOIgMAAIAAA5IAOAAIAAAkgAgKgRQgBALgCAIQgCAJgFAHIAiAAIAAg5IgXAAIgBAWg");
	this.shape_37.setTransform(36.7,39.65);

	this.shape_38 = new cjs.Shape();
	this.shape_38.graphics.f("#FFFFFF").s().p("AgWArIAAgOIAPAAIAAg5IgRAAIAAARIgOAAIAAgfIBNAAIAAAfIgOAAIAAgRIgRAAIAAA5IAPAAIAAAOg");
	this.shape_38.setTransform(148.6,16.675);

	this.shape_39 = new cjs.Shape();
	this.shape_39.graphics.f("#FFFFFF").s().p("AgYAiQgLgLAAgXQAAgNAFgKQAFgKAIgFQAJgFAKAAQAKAAAHADQAIAEAEAIQAFAIAAAMIAAAGIgBAEIg0AAQAAAOAHAHQAGAHAMAAQAHAAAGgCQAHgCAFgEIAAAPQgEAEgHACQgIABgJAAQgSAAgLgKgAATgJQAAgLgFgFQgFgFgIAAQgHAAgFAFQgFAFgBALIAkAAIAAAAg");
	this.shape_39.setTransform(140.275,16.675);

	this.shape_40 = new cjs.Shape();
	this.shape_40.graphics.f("#FFFFFF").s().p("AgcBAIAAgNIAMAAIAKgcIgbhIIgKAAIAAgOIAWAAIAWA/IABAAIARgxIgJAAIAAgOIAiAAIAAAOIgJAAIgkBkIAKAAIAAANg");
	this.shape_40.setTransform(131.675,18.8);

	this.shape_41 = new cjs.Shape();
	this.shape_41.graphics.f("#FFFFFF").s().p("AglArIAAgNIANAAIAAg6IgNAAIAAgOIAmAAQANAAAHADQAHADAEAFQADAFAAAGQAAAHgFAFQgEAFgHACIAAABQAJAAAFAFQAFAGAAAHQAAAHgDAFQgDAGgHADQgIAEgMAAgAgIAfIAMAAQAIgBAFgDQAEgDAAgGQAAgHgFgDQgEgDgIAAIgMAAgAgIgGIAJAAQAJAAAEgDQAEgEgBgFQABgFgFgDQgEgDgIAAIgJAAg");
	this.shape_41.setTransform(122.725,16.675);

	this.shape_42 = new cjs.Shape();
	this.shape_42.graphics.f("#FFFFFF").s().p("AgWArIAAgOIAPAAIAAg5IgRAAIAAARIgNAAIAAgfIBLAAIAAAfIgMAAIAAgRIgSAAIAAA5IAPAAIAAAOg");
	this.shape_42.setTransform(114.15,16.675);

	this.shape_43 = new cjs.Shape();
	this.shape_43.graphics.f("#FFFFFF").s().p("AgUAhQgLgMAAgVQAAgNAFgKQAGgKAJgFQAJgFALAAIAOABIAJADIAAAcIgOAAIAAgSIgDAAIgFAAQgHAAgFADQgGADgDAHQgDAHAAAJQAAAQAHAHQAHAHALAAQAGAAAGgCQAGgBADgDIAAAPIgIAEQgGABgJAAQgSAAgLgLg");
	this.shape_43.setTransform(106,16.675);

	this.shape_44 = new cjs.Shape();
	this.shape_44.graphics.f("#FFFFFF").s().p("AAGA7IAAgNIANAAIAAgwIgBAAIgjA9IgeAAIAAgNIAOAAIAAg6IgOAAIAAgNIAqAAIAAANIgMAAIAAAwIAAAAIAkg9IAdAAIAAANIgNAAIAAA6IANAAIAAANgAgRgpQgHgFAAgMIAOAAQAAAFADADQACADAFAAQAGAAADgDQADgDAAgFIAOAAQAAAMgHAGQgHAGgMAAQgKAAgHgHg");
	this.shape_44.setTransform(96.775,15.05);

	this.shape_45 = new cjs.Shape();
	this.shape_45.graphics.f("#FFFFFF").s().p("AgYAiQgLgLAAgXQAAgNAFgKQAFgKAIgFQAJgFAKAAQAKAAAHADQAIAEAEAIQAFAIAAAMIAAAGIgBAEIg0AAQAAAOAHAHQAGAHAMAAQAHAAAGgCQAHgCAFgEIAAAPQgEAEgHACQgIABgJAAQgSAAgLgKgAATgJQAAgLgFgFQgFgFgIAAQgHAAgFAFQgFAFgBALIAkAAIAAAAg");
	this.shape_45.setTransform(87.225,16.675);

	this.shape_46 = new cjs.Shape();
	this.shape_46.graphics.f("#FFFFFF").s().p("AAfA2IgCgWIg5AAIgCAWIgOAAIAAgkIAIAAQAEgFADgHIAEgSIACgbIgNAAIAAgOIBQAAIAAAOIgOAAIAAA5IAPAAIAAAkgAgKgRQgBALgDAJQgBAIgFAHIAiAAIAAg5IgXAAIgBAWg");
	this.shape_46.setTransform(77.9,17.8);

	this.shape_47 = new cjs.Shape();
	this.shape_47.graphics.f("#FFFFFF").s().p("AABArIAAgOIAKAAIAAgTIgLAAIgUAhIgTAAIAAgOIAKAAIAPgWQgKgDgFgFQgFgGgBgIQAAgHAEgGQADgGAIgEQAGgEANAAIAqAAIAAAOIgOAAIAAA5IAOAAIAAAOgAgMgZQgFAEAAAGQAAAGAFAEQAEADAIABIALAAIAAgbIgLAAQgIAAgEADg");
	this.shape_47.setTransform(63.7,16.675);

	this.shape_48 = new cjs.Shape();
	this.shape_48.graphics.f("#FFFFFF").s().p("AAGArIAAgOIANAAIAAgvIgBAAIgjA9IgeAAIAAgOIAOAAIAAg5IgOAAIAAgOIAqAAIAAAOIgMAAIAAAwIAAAAIAkg+IAdAAIAAAOIgNAAIAAA5IANAAIAAAOg");
	this.shape_48.setTransform(53.775,16.675);

	this.shape_49 = new cjs.Shape();
	this.shape_49.graphics.f("#FFFFFF").s().p("AAgA2IgCgWIhKAAIAAgOIANAAIAAg5IgNAAIAAgOIAdAAIAABHIAdAAIAAg5IgMAAIAAgOIAqAAIAAAOIgNAAIAAA5IAOAAIAAAkg");
	this.shape_49.setTransform(43.225,17.8);

	this.shape_50 = new cjs.Shape();
	this.shape_50.graphics.f("#FFFFFF").s().p("AAWArIgagmIgIACIAAAWIALAAIAAAOIgpAAIAAgOIAOAAIAAg5IgOAAIAAgOIAeAAIAAAlIAIgCIAQgVIgHAAIAAgOIAjAAIAAAOIgLAAIgVAZIAZAgIAKAAIAAAOg");
	this.shape_50.setTransform(33.475,16.675);

	this.shape_51 = new cjs.Shape();
	this.shape_51.graphics.f("#FFFFFF").s().p("AAeBAIgLgnIgoAAIgGAYIAMAAIAAAPIgmAAIAAgPIALAAIAdhhIgNAAIAAgPIAlAAIAhBwIAKAAIAAAPgAAPALIgPg2IAAAAIgQA2IAfAAg");
	this.shape_51.setTransform(23.15,14.575);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_51},{t:this.shape_50},{t:this.shape_49},{t:this.shape_48},{t:this.shape_47},{t:this.shape_46},{t:this.shape_45},{t:this.shape_44},{t:this.shape_43},{t:this.shape_42},{t:this.shape_41},{t:this.shape_40},{t:this.shape_39},{t:this.shape_38},{t:this.shape_37},{t:this.shape_36},{t:this.shape_35},{t:this.shape_34},{t:this.shape_33},{t:this.shape_32},{t:this.shape_31},{t:this.shape_30},{t:this.shape_29},{t:this.shape_28},{t:this.shape_27},{t:this.shape_26},{t:this.shape_25},{t:this.shape_24},{t:this.shape_23},{t:this.shape_22},{t:this.shape_21},{t:this.shape_20},{t:this.shape_19},{t:this.shape_18},{t:this.shape_17},{t:this.shape_16},{t:this.shape_15},{t:this.shape_14},{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.text6, new cjs.Rectangle(0,0,170.4,93.4), null);


(lib.text11 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AgiA5IAAgTIADgDIAJgJIAJgLIAIgJQAGgIAEgGQADgIAAgHQAAgHgDgEQgDgDgHAAIgEAAIgFACIAAAPIgTAAIAAgdQAGgDAIgCQAJgCAJAAQAPgBAJAJQAIAIAAAPQAAAIgDAIQgDAHgEAFIgMAPIgIAKIgJAKIArAAIAAATg");
	this.shape.setTransform(118.525,13);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AgWAeQgKgKAAgUQAAgRAJgLQAJgLAQAAQAJABAHADQAHADAEAIQAEAGAAALIAAAHIgBAFIgpAAQAAAHAFAEQAEAFAJAAIALgBQAFgBAFgEIAAATQgEACgGACQgGABgIAAQgSAAgKgJgAAMgIQAAgHgDgEQgCgCgGgBQgFABgCADQgDADgBAHIAWAAIAAAAg");
	this.shape_1.setTransform(110.775,14.95);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgKA4IAAheIgLAAIAAgRIAgAAIAABeIALAAIAAARg");
	this.shape_2.setTransform(104.4,13.125);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("AgWAeQgKgKAAgUQAAgRAJgLQAJgLAQAAQAJABAHADQAHADAEAIQAEAGAAALIAAAHIgBAFIgpAAQAAAHAFAEQAEAFAJAAIALgBQAFgBAFgEIAAATQgEACgGACQgGABgIAAQgSAAgKgJgAAMgIQAAgHgDgEQgCgCgGgBQgFABgCADQgDADgBAHIAWAAIAAAAg");
	this.shape_3.setTransform(98.725,14.95);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AgZA4IAAgSIAPAAIAAhJIgPAAIAAAOIgTAAIAAgiIBZAAIAAAiIgTAAIAAgOIgPAAIAABJIAPAAIAAASg");
	this.shape_4.setTransform(90.225,13.125);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AAWAmIAAg7IgLAAIAAgQIAsAAIAAAQIgLAAIAAAqIALAAIAAARgAg1AmIAAgRIAKAAIAAgqIgKAAIAAgQIArAAIAAAQIgMAAIAAAKIAHAAQAMAAAGAEQAIADADAEQADAGABAGQgBAIgDAFQgDAHgIACQgGAEgMAAgAgWAWIAHAAQAGgBACgCQADgCAAgEQAAgDgDgDQgCgCgGAAIgHAAg");
	this.shape_5.setTransform(75.55,14.95);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AgWAmIAAgRIANAAIAAgpIgKAAIAAAPIgRAAIAAggIBJAAIAAAgIgRAAIAAgPIgKAAIAAApIANAAIAAARg");
	this.shape_6.setTransform(65.65,14.95);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AgbA5IAAgRIAMAAIAHgTIgXg8IgIAAIAAgRIAYAAIAQAxIABAAIALggIgIAAIAAgRIAjAAIAAARIgIAAIgcBPIAIAAIAAARg");
	this.shape_7.setTransform(57.625,16.825);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AAKAmIAAgfIgTAAIAAAOIAJAAIAAARIgpAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAcIATAAIAAgMIgJAAIAAgQIApAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_8.setTransform(48.925,14.95);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AAEAmIAAgRIAJAAIAAgaIgBAAIgZArIgeAAIAAgRIALAAIAAgqIgLAAIAAgQIApAAIAAAQIgKAAIAAAbIABAAIAZgrIAeAAIAAAQIgKAAIAAAqIAKAAIAAARg");
	this.shape_9.setTransform(39.4,14.95);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("AAZAmIAAgzIgBAAIgQAzIgSAAIgQgzIgBAAIAAAzIgeAAIAAgRIALAAIAAgqIgLAAIAAgQIArAAIAOAwIABAAIAOgwIArAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_10.setTransform(28.35,14.95);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AgfAhQgFgFAAgKQgBgOALgGQALgGAUAAIAAgCQABgFgEgCQgCgDgIAAQgGAAgGABQgGACgFAEIAAgUQAGgDAGgCIAOgBQAPAAAJAHQAHAIABAOIAAAfIALAAIAAARIggAAIAAgMIgBAAIgEAHQgCADgEACQgEABgGAAQgKABgGgHgAgKAHQgEADgBAEQAAABABABQAAAAAAABQAAAAABABQAAAAAAABQADABAEABQAFAAADgDQADgFAAgHIAAgCQgLABgEACg");
	this.shape_11.setTransform(14.15,14.95);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AgWA4QgGgCgGgDIAAgUIANAGQAGACAIAAQAJAAAEgEQAGgDAAgIQAAgIgGgDQgFgEgHAAIgLAAIAAgTIALAAQAHAAAEgEQAEgEAAgGQAAgHgFgEQgEgDgIAAIgEAAIgDAAIAAARIgSAAIAAgcQAFgDAHgCQAJgDAJAAQAMAAAIAFQAHAEAEAHQAEAGgBAIQAAAJgEAHQgGAGgIADIAAABQAMACAFAHQAFAHAAAKQgBAKgEAHQgFAIgJAEQgKAEgLAAQgKAAgHgCg");
	this.shape_12.setTransform(6.05,13.125);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.text11, new cjs.Rectangle(0,0,124.5,25.1), null);


(lib.strelka = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("AAAAAQAAABhoBKIBoiVIBpCVg");
	this.shape.setTransform(10.525,7.5);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.strelka, new cjs.Rectangle(0,0,21.1,15), null);


(lib.sparkl = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.shape = new cjs.Shape();
	this.shape.graphics.rf(["#299FE3","rgba(41,159,227,0)"],[0,0.749],0,0,0,0,0,1.4).s().p("AgGAHQgDgDAAgEQAAgDADgDQADgDADAAQAEAAADADQADADAAADQAAAEgDADQgDADgEAAQgDAAgDgDg");
	this.shape.setTransform(1,1);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.sparkl, new cjs.Rectangle(0,0,2,2), null);


(lib.phoneblick = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("EgvMBH5MAAAiPxMBeZAAAMAAACPxg");
	mask.setTransform(482.125,304.1);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.rf(["#FFFFFF","rgba(255,255,255,0)"],[0,1],0,0,0,0,0,181.4).s().p("Az4T5QoPoQAArpQAArpIPoPQIQoPLoAAQLpAAIQIPQIPIPAALpQAALpoPIQQoQIPrpAAQroAAoQoPg");
	this.shape.setTransform(180,180);

	var maskedShapeInstanceList = [this.shape];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.phoneblick, new cjs.Rectangle(180.1,0,179.9,360), null);


(lib.min = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_3
	this.instance = new lib.womanglowmin300600();
	this.instance.setTransform(0,0,0.6667,0.6667);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.min, new cjs.Rectangle(0,0,120,140), null);


(lib.logotext = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Слой_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AhGBRQgOgOAAgWQAAggAagPQAagPA1AAIAAgIQAAgngqAAQgcAAgXAQIgBghQAYgOAhAAQBIAAAABHIAABXIAcABIABAcIg+AAIAAgdIgCAAQgJARgLAHQgMAJgUAAQgZAAgOgPgAgfAPQgQAIAAATQAAALAHAGQAHAHANAAQASAAALgMQAMgOAAgZIAAgIQgkAAgQAIg");
	this.shape.setTransform(53.2948,-1.8719,0.42,0.42);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AhOBdIgMgBIAAgiIAIABQATAAAJggQAHgcACg+IgcgBIAAgcICkAAIAAAdIgcAAIAAB9IAcAAIAAAdIg/AAIAAiZIgrAAQgBBMgLAhQgOAugkAAIgBAAg");
	this.shape_1.setTransform(44.9686,-1.8193,0.42,0.42);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AAOBcIAAgcIAbAAIAAhoIgCAAIhOCEIg+AAIAAgcIAcAAIAAh+IgcAAIAAgdIBZAAIAAAdIgbAAIAABoIACAAIBNiFIA/AAIAAAdIgcAAIAAB+IAcgBIAAAdg");
	this.shape_2.setTransform(35.981,-1.8614,0.42,0.42);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("AhRBcIAAgdIAcABIAAh+IgcAAIAAgdIBUAAQBHAAAAAuQAAAigiAHIAAACQAVACALAMQAKALAAAQQAAAYgQANQgSAQgkAAgAgRBCIAaAAQARAAAJgIQAKgHAAgNQAAgbgkAAIgaAAgAgRgNIATAAQAjAAAAgcQAAgXgjAAIgTAAg");
	this.shape_3.setTransform(27.2559,-1.8719,0.42,0.42);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AhGBRQgNgOAAgWQAAggAagPQAagPA1AAIAAgIQAAgngrAAQgbAAgZAQIAAghQAXgOAjAAQBIAAAABHIAABXIAcAAIAAAdIg+AAIAAgdIgCAAQgJARgLAHQgMAJgUAAQgYAAgPgPgAgfAPQgQAIAAATQAAALAHAGQAHAHANAAQASAAALgMQANgOAAgZIAAgIQgmAAgPAIg");
	this.shape_4.setTransform(19.5807,-1.8719,0.42,0.42);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AhgCLIAAgcIAcAAIAAjZIgcgBIAAgcIA9AAIAAAaIADAAQASgeAmAAQAgAAAUAaQAUAaABAqQgBAtgUAaQgUAaggAAQgkAAgUgeIgDAAIACBZIAdAAIAAAdgAgThfQgOANAAAYIAAAaQABAaAOANQAMAOAUAAQAUAAAMgQQAOgQAAghQAAgggOgRQgMgPgUAAQgVAAgMANg");
	this.shape_5.setTransform(11.097,-0.024,0.42,0.42);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AAgBcIAAiaIg/AAIAAB9IAaAAIAAAdIhZAAIAAgdIAcABIAAh+IgcAAIAAgdIC9AAIAAAcIgcABIAAB9IAcAAIAAAdg");
	this.shape_6.setTransform(2.0149,-1.8614,0.42,0.42);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("Ag0BIQgYgYAAgvQAAgsAXgaQAVgaAkABQAhgBATATQAVAUAAAlQAAASgCAFIhxAAQABA9A2AAQAhAAAWgRIAAAgQgVAQgoAAQgoAAgXgYgAgmgVIBQAAQgCgtgmAAQgjAAgFAtg");
	this.shape_7.setTransform(-10.8681,-1.8617,0.42,0.42);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AAOBcIAAgdIAbABIAAhoIgDAAIhNCEIg+AAIAAgdIAcAAIAAh9IgcgBIAAgcIBZAAIAAAcIgbABIAABoIACAAIBNiFIA+AAIAAAdIgcAAIAAB+IAcgBIAAAdg");
	this.shape_8.setTransform(-19.2888,-1.8614,0.42,0.42);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AhIBcIAAgdIAcABIABh+IgdAAIAAgdICQAAIAABDIgdAAIAAgmIgzAAIAAB+IAhAAIAAAcg");
	this.shape_9.setTransform(-27.5624,-1.8614,0.42,0.42);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("Ag/CJIAAgcIAbAAIAXg9Ig8icIgUAAIAAgdIAvAAIAvCJIAEAAIAlhsIgVAAIAAgdIBKAAIAAAdIgUAAIhNDZIAWAAIAAAdg");
	this.shape_10.setTransform(-35.2691,0.06,0.42,0.42);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AhgBvIAcAAIAAjZIgcAAIAAgdIA9AAIAAAaIADAAQASgeAmAAQAgAAAUAaQAVAaAAAqQAAAtgVAaQgTAaghAAQgkAAgUgeIgDAAIACBZIAeAAIAAAcIhdABgAgThfQgOANAAAYIAAAaQAAAaAOANQAOAOATAAQAUAAAMgQQAOgQAAghQAAgggOgRQgMgPgUAAQgUAAgNANg");
	this.shape_11.setTransform(-43.6268,-0.024,0.42,0.42);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("ABDB0IgDgwIh+AAIgEAwIgeAAIAAhNIASAAQAOgRAFgbQAIgfABgyIgcAAIAAgdICsAAIAAAdIgcAAIAAB9IAfAAIAABNgAgsAnIBLAAIgBh9IgyAAQgBBcgXAhg");
	this.shape_12.setTransform(-52.7824,-0.8535,0.42,0.42);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.logotext, new cjs.Rectangle(-56.8,-5.9,113.69999999999999,11.8), null);


(lib.logomi = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_2
	this.instance = new lib.logomi300600();
	this.instance.setTransform(0,0,0.4664,0.4664);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.logomi, new cjs.Rectangle(0,0,28,28), null);


(lib.logo = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Слой_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AhJhFQBFhmCLgdIAADSQglAPgQAeQgWArAGBVIjHASQgIioBEhmg");
	this.shape.setTransform(20.9099,-7.2876,0.27,0.27);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AlBBsIAAjEIKDgUIAADYg");
	this.shape_1.setTransform(25.767,10.0775,0.27,0.27);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AivD8QCDh9Azg9QApgxAPguQAPgxgRgiQgKgVgXgLQgVgKgdABIAAjPQBIgKA/ARQA/ARAtAqQApAnAUA0QAUA1gGA5QgJBrg9BjQg9BkiRCNIk9ALg");
	this.shape_2.setTransform(26.1652,-3.106,0.27,0.27);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("Ah2BZIAAiqIDtgIIAACyg");
	this.shape_3.setTransform(-2.6799,10.5904,0.27,0.27);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AhRF/IAArmICjgYIAAL+g");
	this.shape_4.setTransform(-8.9497,2.6536,0.27,0.27);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AiJBiIAAi6IETgJIAADDg");
	this.shape_5.setTransform(11.6954,10.3677,0.27,0.27);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AhZhWIC0gQIAADDIi0AKg");
	this.shape_6.setTransform(10.4131,1.4185,0.27,0.27);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AiJhJIETgnIAADCIkTAfg");
	this.shape_7.setTransform(11.6954,-7.7735,0.27,0.27);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AheGjIAAsrIC9gbIAANGg");
	this.shape_8.setTransform(4.4538,1.6818,0.27,0.27);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AhnBSIAAidIDPgGIAACjg");
	this.shape_9.setTransform(-15.4827,10.7929,0.27,0.27);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("AhDhJICHgMIAACjIiHAIg");
	this.shape_10.setTransform(-16.4478,3.3217,0.27,0.27);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("Ahng/IDPgdIAACiIjPAXg");
	this.shape_11.setTransform(-15.4827,-4.3518,0.27,0.27);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AhHFfIAAqqICPgUIAAK+g");
	this.shape_12.setTransform(-20.9763,3.5175,0.27,0.27);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#FFFFFF").s().p("Ai6gqIF1g1IAACVIl1Aqg");
	this.shape_13.setTransform(-29.345,-2.6443,0.27,0.27);

	this.shape_14 = new cjs.Shape();
	this.shape_14.graphics.f("#FFFFFF").s().p("AhDD1IAAnbICHgOIAAHpg");
	this.shape_14.setTransform(-29.3248,6.3925,0.27,0.27);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_14},{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.logo, new cjs.Rectangle(-34.4,-12.9,68.9,25.9), null);


(lib.handcifrosn1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_4 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("EgSJAiVQAQgdAHgQQAIgUALgkQANgnAGgYQAGgXARgbQAOgWASgTQAMgNAQhKQAciEAJgkIBBj1QAoiUANgsQAKgfA8imQA/itAMglQAQgwAjilIAfidQgCgVAAgeQAAgTARhNIAXhlQAGgXAWggIAVgbQAIgKAIgNQALgRAfhkIAviRQAjhsAIgTIA5h+IAwhoQgehTgHgoQgEgaAAgaIADgwIADhHQAEgvAGgOQAIgRAZgKQAagLAVAGQASAGAXARIATARIgCkUIgBmUQgBmZABgdQABglAEgVQAEgYAMgZQALgWApgRQAVgJATgFQMJgCAWAFQAQAEAWAPQAVAPAOAQQAMAOAHAfQADAQACANIgEJ+IAKgHQALgHANgEQAMgEATABIARADIAKgGQAMgEAPADQARAEAGAQQAGAPgDAcQgCAagSAlQgQAhgTAYQgNASgpAoIglAlIABCHIAgAGQAiAHALAGQAJAEAOASQANASAJABQAsAJAlALQBHAUASAUQAUAWAIAoQAHAlgHASQgIAWgwAyIANAKQASARAbAmQAdAngRArQgKAZgjAnQgVAXhhA8IhcA4IgEAUQgHAXgOAPQgPAPgUAwQgKAYgHAVIAAAfQgCAjgLAaQgMAagTAQQgKAIgIADIgGAQQgIAUgLAPQgMASgaARQgbASghAMQgxASh5BFQgfARiCBWIh8BSIADAoQADAugEAbQgDAQgtBsQg1B+gfBpQg2C7AAF4QAABVgGCFQgICjgNBiQgLBageB3QgNA0gLAng");
	mask.setTransform(83.2656,219.6683);

	// Layer_3
	this.instance = new lib.hand3006001();
	this.instance.setTransform(-40,0,0.6667,0.6667);

	var maskedShapeInstanceList = [this.instance];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.handcifrosn1, new cjs.Rectangle(-40,0,280,440), null);


(lib.text5 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AgiA6IAAgTIADgFIAJgJIAJgKIAIgJQAGgIAEgHQADgGAAgIQAAgGgDgEQgDgEgHgBIgEABIgFACIAAAOIgTAAIAAgcQAGgEAIgCQAJgCAJAAQAPABAJAIQAIAJAAAOQAAAJgDAGQgDAIgEAGIgMANIgIAKIgJALIArAAIAAAUg");
	this.shape.setTransform(117.325,30.05);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AgWAeQgKgKAAgUQAAgSAJgKQAJgKAQAAQAJgBAHAEQAHADAEAHQAEAHAAAKIAAAIIgBAFIgpAAQAAAIAFAEQAEAEAJAAIALgCQAFgBAFgCIAAASQgEADgGABQgGABgIAAQgSABgKgKgAAMgJQAAgGgDgDQgCgDgGgBQgFAAgCAEQgDADgBAGIAWAAIAAAAg");
	this.shape_1.setTransform(109.575,32);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgJA4IAAheIgLAAIAAgRIAfAAIAABeIALAAIAAARg");
	this.shape_2.setTransform(103.2,30.175);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("AgWAeQgKgKAAgUQAAgSAJgKQAJgKAQAAQAJgBAHAEQAHADAEAHQAEAHAAAKIAAAIIgBAFIgpAAQAAAIAFAEQAEAEAJAAIALgCQAFgBAFgCIAAASQgEADgGABQgGABgIAAQgSABgKgKgAAMgJQAAgGgDgDQgCgDgGgBQgFAAgCAEQgDADgBAGIAWAAIAAAAg");
	this.shape_3.setTransform(97.525,32);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AgZA4IAAgSIAPAAIAAhJIgPAAIAAAOIgTAAIAAgiIBZAAIAAAiIgTAAIAAgOIgPAAIAABJIAPAAIAAASg");
	this.shape_4.setTransform(89.025,30.175);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AAWAmIAAg6IgKAAIAAgRIArAAIAAARIgMAAIAAApIAMAAIAAARgAg1AmIAAgRIALAAIAAgpIgLAAIAAgRIAqAAIAAARIgLAAIAAAKIAIAAQALAAAGACQAHAEAEAEQAEAGAAAGQAAAIgEAGQgEAFgHAEQgGADgLAAgAgWAVIAHAAQAGAAADgCQACgCAAgEQAAgDgCgCQgDgDgGAAIgHAAg");
	this.shape_5.setTransform(74.35,32);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AgWAmIAAgRIAMAAIAAgoIgJAAIAAANIgSAAIAAgfIBLAAIAAAfIgSAAIAAgNIgJAAIAAAoIAMAAIAAARg");
	this.shape_6.setTransform(64.45,32);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AgbA5IAAgRIAMAAIAHgTIgXg8IgIAAIAAgRIAYAAIAQAxIABAAIALggIgIAAIAAgRIAjAAIAAARIgIAAIgcBPIAIAAIAAARg");
	this.shape_7.setTransform(56.425,33.875);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AAKAmIAAgeIgTAAIAAANIAJAAIAAARIgpAAIAAgRIALAAIAAgpIgLAAIAAgRIAgAAIAAAcIATAAIAAgLIgJAAIAAgRIApAAIAAARIgLAAIAAApIALAAIAAARg");
	this.shape_8.setTransform(47.725,32);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AADAmIAAgRIAKAAIAAgbIgBAAIgZAsIgeAAIAAgRIALAAIAAgpIgLAAIAAgRIApAAIAAARIgKAAIAAAbIABAAIAZgsIAeAAIAAARIgKAAIAAApIAKAAIAAARg");
	this.shape_9.setTransform(38.2,32);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("AAZAmIAAg0IAAAAIgRA0IgRAAIgRg0IgBAAIAAA0IgdAAIAAgRIALAAIAAgpIgLAAIAAgRIAqAAIAOAvIABAAIAPgvIAqAAIAAARIgMAAIAAApIAMAAIAAARg");
	this.shape_10.setTransform(27.15,32);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AgeAiQgHgHAAgJQAAgOALgFQAKgIAWAAIAAgBQgBgFgDgDQgDgCgHAAQgGAAgGACQgFABgGADIAAgTQAGgDAGgBIAOgBQAQAAAHAGQAIAIAAAOIAAAfIAMAAIAAARIggAAIAAgMIgBAAIgFAHQgBADgEABQgEACgFAAQgLAAgFgFgAgKAHQgFADABAFQAAAAAAABQAAAAAAABQAAAAABABQAAABABAAQABACAFAAQAFAAADgDQADgFABgGIAAgCQgMAAgEACg");
	this.shape_11.setTransform(12.95,32);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AgKAnIgJgCIgIgCIAAgTQAGAEAGABQAFACAHAAQAEAAADgCQADgCAAgEQAAgEgCgCQgDgBgEAAIgKAAIAAgQIAKAAQADAAACgBQACgCAAgEQAAgDgDgCQgCgCgEAAIgDABIgDAAIAAAKIgQAAIAAgYIALgCIAMgBQAKAAAGACQAHADADAFQADAEAAAGQAAAFgDAEQgDAFgHADIAAABQAHABAEAEQAEAEAAAHQAAAHgDAFQgEAFgHADQgGADgKAAIgIAAg");
	this.shape_12.setTransform(5.275,32);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#FFFFFF").s().p("AAWAmIAAg7IgKAAIAAgQIArAAIAAAQIgMAAIAAAqIAMAAIAAARgAg1AmIAAgRIALAAIAAgqIgLAAIAAgQIAqAAIAAAQIgLAAIAAAKIAIAAQALAAAHAEQAGADAEAEQAEAGAAAGQAAAIgEAFQgEAHgGACQgHAEgLAAgAgWAWIAHAAQAGgBADgCQACgCAAgEQAAgDgCgDQgDgCgGAAIgHAAg");
	this.shape_13.setTransform(159.4,14.95);

	this.shape_14 = new cjs.Shape();
	this.shape_14.graphics.f("#FFFFFF").s().p("AAKAmIAAgfIgTAAIAAAOIAJAAIAAARIgpAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAcIATAAIAAgMIgJAAIAAgQIApAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_14.setTransform(148.825,14.95);

	this.shape_15 = new cjs.Shape();
	this.shape_15.graphics.f("#FFFFFF").s().p("AgSAjQgIgEgFgJQgFgJAAgNQAAgLAFgKQAFgIAIgFQAIgEAKgBQAKABAJAEQAIAFAFAIQAFAKAAALQAAAMgFAKQgFAIgIAFQgJAEgKAAQgKAAgIgEgAgKgPQgEAFAAAKQAAALAEAEQAEAGAGAAQAGAAAEgGQAFgEAAgLQAAgKgFgFQgEgFgGAAQgGAAgEAFg");
	this.shape_15.setTransform(140.075,14.95);

	this.shape_16 = new cjs.Shape();
	this.shape_16.graphics.f("#FFFFFF").s().p("AgWBMIAAgSIAMAAIAAgTQgMAAgJgGQgJgEgEgJQgFgIAAgMQAAgKAFgJQAEgIAJgFQAJgGAMgBIAAgTIgLAAIAAgRIAfAAIAAAkQANACAJAFQAJAEAEAJQAFAJAAAKQAAALgFAJQgEAIgJAFQgJAGgNAAIAAATIANAAIAAASgAAKAVQAJAAAEgHQAFgFAAgJQAAgIgFgGQgFgFgIgBgAgWgOQgFAGAAAIQAAAJAFAGQAEAFAIABIAAgpQgIABgEAFg");
	this.shape_16.setTransform(130.575,14.95);

	this.shape_17 = new cjs.Shape();
	this.shape_17.graphics.f("#FFFFFF").s().p("AgWAmIAAgRIANAAIAAgpIgKAAIAAAPIgSAAIAAggIBKAAIAAAgIgRAAIAAgPIgKAAIAAApIANAAIAAARg");
	this.shape_17.setTransform(121.2,14.95);

	this.shape_18 = new cjs.Shape();
	this.shape_18.graphics.f("#FFFFFF").s().p("AgpA6IAAgSIALAAIAAhPIgLAAIAAgQIAfAAIAAALIACAAQADgGAFgDQAEgDAIgBQAKAAAGAGQAHAEADAJQAEAIgBAMQABAMgEAJQgDAJgHAEQgHAGgJgBQgIABgEgDQgFgEgDgFIgCAAIACALIAAATIALAAIAAASgAgEghQgFADABAKIAAAFQAAAKADAEQAFADAFABQAGgBAEgDQAFgFAAgLQAAgIgCgEQgDgFgDgBQgDgDgEAAQgFAAgEAFg");
	this.shape_18.setTransform(112.6,16.75);

	this.shape_19 = new cjs.Shape();
	this.shape_19.graphics.f("#FFFFFF").s().p("AgeAhQgHgFAAgKQAAgOALgGQAKgGAWAAIAAgCQgBgFgDgCQgDgDgHAAQgGAAgFABQgGACgGAEIAAgUQAGgDAGgCIANgBQARAAAHAHQAJAIgBAOIAAAfIALAAIAAARIgfAAIAAgMIgBAAIgFAHQgBADgEACQgEABgGAAQgKABgFgHgAgKAHQgFADAAAEQAAABABABQAAAAAAABQAAAAABABQAAAAABABQACABADABQAGAAACgDQAEgFABgHIAAgCQgLABgFACg");
	this.shape_19.setTransform(104.1,14.95);

	this.shape_20 = new cjs.Shape();
	this.shape_20.graphics.f("#FFFFFF").s().p("AAZAmIAAgzIgBAAIgQAzIgSAAIgQgzIgBAAIAAAzIgeAAIAAgRIALAAIAAgqIgLAAIAAgQIArAAIAOAwIABAAIAOgwIArAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_20.setTransform(93.6,14.95);

	this.shape_21 = new cjs.Shape();
	this.shape_21.graphics.f("#FFFFFF").s().p("AgTAdQgKgKAAgTQAAgLAFgJQAEgJAJgFQAIgEALgBIANABIAJAEIAAAAIAAAcIgSAAIAAgOIgBAAIgCAAQgIABgEAFQgEAFAAAJQAAALAFAEQAEAGAJAAIAKgCQAEgCAFgDIAAAUQgDADgGABQgGABgGAAQgSABgKgLg");
	this.shape_21.setTransform(83.8,14.95);

	this.shape_22 = new cjs.Shape();
	this.shape_22.graphics.f("#FFFFFF").s().p("AgeAhQgHgFAAgKQAAgOALgGQAKgGAWAAIAAgCQgBgFgDgCQgDgDgHAAQgGAAgGABQgFACgGAEIAAgUQAGgDAGgCIAOgBQAQAAAHAHQAIAIAAAOIAAAfIAMAAIAAARIggAAIAAgMIgBAAIgFAHQgBADgEACQgEABgFAAQgLABgFgHgAgKAHQgFADABAEQAAABAAABQAAAAAAABQAAAAABABQAAAAABABQABABAFABQAFAAADgDQADgFABgHIAAgCQgMABgEACg");
	this.shape_22.setTransform(72.35,14.95);

	this.shape_23 = new cjs.Shape();
	this.shape_23.graphics.f("#FFFFFF").s().p("AAKAmIAAgfIgTAAIAAAOIAJAAIAAARIgpAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAcIATAAIAAgMIgJAAIAAgQIApAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_23.setTransform(63.375,14.95);

	this.shape_24 = new cjs.Shape();
	this.shape_24.graphics.f("#FFFFFF").s().p("AgeAhQgHgFAAgKQAAgOALgGQAKgGAVAAIAAgCQAAgFgDgCQgDgDgHAAQgGAAgGABQgFACgGAEIAAgUQAGgDAGgCIAOgBQAQAAAHAHQAIAIAAAOIAAAfIAMAAIAAARIggAAIAAgMIgBAAIgFAHQgBADgEACQgEABgFAAQgLABgFgHgAgKAHQgFADABAEQAAABAAABQAAAAAAABQAAAAABABQAAAAABABQABABAFABQAFAAADgDQADgFAAgHIAAgCQgLABgEACg");
	this.shape_24.setTransform(50.75,14.95);

	this.shape_25 = new cjs.Shape();
	this.shape_25.graphics.f("#FFFFFF").s().p("AASAmIgUgfIgFACIAAAMIAHAAIAAARIgnAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAfIAFgBIAKgOIgGAAIAAgQIAkAAIAAAQIgJAAIgOASIASAYIAHAAIAAARg");
	this.shape_25.setTransform(42.225,14.95);

	this.shape_26 = new cjs.Shape();
	this.shape_26.graphics.f("#FFFFFF").s().p("AAXAwIgCgUIgpAAIgBAUIgTAAIAAglIAGAAQAFgGADgKQADgKABgPIgLAAIAAgRIBKAAIAAARIgLAAIAAApIALAAIAAAlgAgFgVIgCANIgDAKQgBAFgCAEIAWAAIAAgpIgOAAIAAAJg");
	this.shape_26.setTransform(33.2,15.95);

	this.shape_27 = new cjs.Shape();
	this.shape_27.graphics.f("#FFFFFF").s().p("AAEAmIAAgRIAJAAIAAgaIgBAAIgZArIgeAAIAAgRIALAAIAAgqIgLAAIAAgQIApAAIAAAQIgKAAIAAAbIABAAIAZgrIAeAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_27.setTransform(24.1,14.95);

	this.shape_28 = new cjs.Shape();
	this.shape_28.graphics.f("#FFFFFF").s().p("AASAmIgUgfIgFACIAAAMIAHAAIAAARIgnAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAfIAFgBIAKgOIgGAAIAAgQIAkAAIAAAQIgJAAIgOASIASAYIAHAAIAAARg");
	this.shape_28.setTransform(15.025,14.95);

	this.shape_29 = new cjs.Shape();
	this.shape_29.graphics.f("#FFFFFF").s().p("AgOAzQgLgHgGgNQgGgNAAgRQAAgQAGgNQAGgNALgIQAMgIAQAAQAHAAAHACIAKACIAAAgIgTAAIAAgQIgCAAIgCAAQgKAAgGAFQgGAFgEAIQgDAJAAAKQAAATAJAKQAHAJAPAAIAMgBIAJgEIAAATQgEADgHABIgOACQgQAAgLgHg");
	this.shape_29.setTransform(6.225,13.125);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_29},{t:this.shape_28},{t:this.shape_27},{t:this.shape_26},{t:this.shape_25},{t:this.shape_24},{t:this.shape_23},{t:this.shape_22},{t:this.shape_21},{t:this.shape_20},{t:this.shape_19},{t:this.shape_18},{t:this.shape_17},{t:this.shape_16},{t:this.shape_15},{t:this.shape_14},{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.text5, new cjs.Rectangle(0,0,171.5,42.1), null);


(lib.text4 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AgQBUIAAinIAiAAIAACng");
	this.shape.setTransform(118.65,61.5);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AAuBUIAAg7IAhhYIAACTgAgPBUIg/inIAhAAIA9CngAhOBUIAAiTIAhBYIAAA7gAAEAeIAqhxIAhAAIg7Ccg");
	this.shape_1.setTransform(105.9,61.5);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AADA4QALgBAJgGQAJgGAFgMQAGgMAAgTQAAgTgGgMQgGgNgJgFQgKgFgJgBIAAghQANABANAFQANAEAMAKQALALAHAQQAIARAAAYQAAAXgHAQQgGARgMAKQgLALgNAGQgNAFgPABgAgfBSQgNgFgLgMQgLgKgGgRQgHgQAAgWQAAgXAHgRQAHgQAMgLQALgKANgFQAOgFAMgBIAAAhQgJABgJAFQgJAGgGAMQgGAMgBATQABATAFALQAGANAJAFQAJAHAKABIAAAhQgOgBgOgGg");
	this.shape_2.setTransform(87.675,61.5);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("AAnBUIg6inIAkAAIA7CngAhLBUIA0icIARAwIgRA2IAkAAIAKAcIg3AAIgIAag");
	this.shape_3.setTransform(70.925,61.5);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AgQBUIAAinIAiAAIAACng");
	this.shape_4.setTransform(59.7,61.5);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AAlBUIhqinIAoAAIBrCngAhNBUIA1hUIAUAfIghA1gAAFgrIAZgoIAoAAIgtBJg");
	this.shape_5.setTransform(48.225,61.5);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AAnBUIg6inIAkAAIA7CngAhLBUIA0icIARAwIgRA2IAkAAIAKAcIg3AAIgIAag");
	this.shape_6.setTransform(26.475,61.5);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AAhBUIAAhJIgeAAIAAgdIAeAAIAAhBIAjAAIAACngAhDBUIAAinIAjAAIAABBIAdAAIAAAdIgdAAIAABJg");
	this.shape_7.setTransform(10.225,61.5);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AA2BUIAAinIAiAAIAACngAguBUIAAgfIAXAAQANAAAIgHQAGgHAAgMQAAgLgDgGQgEgHgGgCQgGgCgIAAIgXAAIAAgcIAbAAQATgBANAJQAMAHAGANQAGAMAAAQQAAALgDAKQgDAJgHAJQgGAIgMAFQgKAFgRAAgAhXBUIAAinIAjAAIAACng");
	this.shape_8.setTransform(94.15,38.95);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AgRBUIAAinIAiAAIAACngAAYg0IAAgfIAoAAIAAAfgAhAg0IAAgfIAoAAIAAAfg");
	this.shape_9.setTransform(76.75,38.95);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("Ag6BUIAAgfIAHAAIATgBQAHgBAEgDQAEgEADgGIA0h5IAmAAIg7CIQgGAMgGAHQgGAHgLACQgKADgRAAgAhLhTIAoAAIAjBIIgSApg");
	this.shape_10.setTransform(62.025,38.95);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AAhBUIAAhJIgeAAIAAgeIAeAAIAAhAIAjAAIAACngAhDBUIAAinIAjAAIAABAIAdAAIAAAeIgdAAIAABJg");
	this.shape_11.setTransform(45.775,38.95);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AAhBUIAAinIAjAAIAACngAhDBUIAAinIAjAAIAACngAgZAPIAzhWIAAA6IgzBVg");
	this.shape_12.setTransform(29.125,38.95);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#FFFFFF").s().p("AAuBUIAAg7IAhhYIAACTgAgPBUIg/inIAhAAIA9CngAhOBUIAAiTIAhBXIAAA8gAAEAeIAqhxIAhAAIg6Ccg");
	this.shape_13.setTransform(11.35,38.95);

	this.shape_14 = new cjs.Shape();
	this.shape_14.graphics.f("#FFFFFF").s().p("AgQBUIAAgfIBKAAIAAAfgAg6BUIAAinIAjAAIAACngAgQANIAAgdIBEAAIAAAdgAgQg0IAAgfIBHAAIAAAfg");
	this.shape_14.setTransform(105.7,16.4);

	this.shape_15 = new cjs.Shape();
	this.shape_15.graphics.f("#FFFFFF").s().p("AgRBUIAAinIAjAAIAACngAAZg0IAAgfIAnAAIAAAfgAg/g0IAAgfIAnAAIAAAfg");
	this.shape_15.setTransform(91.3,16.4);

	this.shape_16 = new cjs.Shape();
	this.shape_16.graphics.f("#FFFFFF").s().p("AAhBqIAAinIAjAAIAACngAhDBqIAAinIAjAAIAACngAgZAkIAzhUIAAA4IgzBWgAgVhKQgIgDgEgHQgEgIgBgNIAUAAQAAAGADADQACACAEACIAIAAIAKAAQAEgCACgCQACgDABgGIAUAAQgBANgFAIQgFAHgJADQgIACgLAAQgLAAgJgCg");
	this.shape_16.setTransform(75.925,14.2);

	this.shape_17 = new cjs.Shape();
	this.shape_17.graphics.f("#FFFFFF").s().p("AAgBUIAAinIAjAAIAACngAhCBUIAkhCQgNgFgIgMQgIgLAAgUQAAgZAPgOQAPgOAbAAIAbAAIAAAeIgbAAQgJAAgHAFQgGAGAAAMQAAAOAGAGQAHAGAJAAIAbAAIAAAbIgVAAIggA9g");
	this.shape_17.setTransform(59.325,16.4);

	this.shape_18 = new cjs.Shape();
	this.shape_18.graphics.f("#FFFFFF").s().p("AAhBUIAAhJIgeAAIAAgdIAeAAIAAhBIAjAAIAACngAhDBUIAAinIAjAAIAABBIAdAAIAAAdIgdAAIAABJg");
	this.shape_18.setTransform(43.425,16.4);

	this.shape_19 = new cjs.Shape();
	this.shape_19.graphics.f("#FFFFFF").s().p("AgQBUIAAgfIBKAAIAAAfgAg6BUIAAinIAjAAIAACngAgQANIAAgdIBEAAIAAAdgAgQg0IAAgfIBIAAIAAAfg");
	this.shape_19.setTransform(28.2,16.4);

	this.shape_20 = new cjs.Shape();
	this.shape_20.graphics.f("#FFFFFF").s().p("AAuBUIAAg7IAhhYIAACTgAgPBUIg/inIAhAAIA9CngAhOBUIAAiTIAhBXIAAA8gAAEAeIAqhxIAhAAIg6Cdg");
	this.shape_20.setTransform(11.35,16.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_20},{t:this.shape_19},{t:this.shape_18},{t:this.shape_17},{t:this.shape_16},{t:this.shape_15},{t:this.shape_14},{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.text4, new cjs.Rectangle(0,0,124.3,77.7), null);


(lib.text3 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AADAmIAAgRIAKAAIAAgaIgBAAIgZArIgeAAIAAgRIALAAIAAgqIgLAAIAAgQIAoAAIAAAQIgJAAIAAAbIABAAIAZgrIAeAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape.setTransform(160.3,14.95);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AASAmIgUgfIgFACIAAAMIAHAAIAAARIgnAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAfIAFgBIAKgOIgGAAIAAgQIAkAAIAAAQIgJAAIgOASIASAYIAHAAIAAARg");
	this.shape_1.setTransform(151.125,14.95);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AAXAwIgCgUIgpAAIgBAUIgTAAIAAglIAGAAQAFgGADgKQADgKABgPIgLAAIAAgRIBKAAIAAARIgLAAIAAApIAMAAIAAAlgAgFgVIgCANIgDAKQgBAFgCAEIAWAAIAAgpIgOAAIAAAJg");
	this.shape_2.setTransform(142,15.95);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("AADAmIAAgRIAKAAIAAgaIgBAAIgZArIgeAAIAAgRIALAAIAAgqIgLAAIAAgQIApAAIAAAQIgKAAIAAAbIABAAIAZgrIAeAAIAAAQIgKAAIAAAqIAKAAIAAARg");
	this.shape_3.setTransform(132.8,14.95);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AASAmIgUgfIgFACIAAAMIAHAAIAAARIgnAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAfIAFgBIAKgOIgGAAIAAgQIAkAAIAAAQIgJAAIgOASIASAYIAHAAIAAARg");
	this.shape_4.setTransform(123.625,14.95);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AgTAdQgKgKAAgTQAAgLAEgJQAGgJAIgFQAJgEAKgBIANABIAJAEIAAAAIAAAcIgRAAIAAgOIgCAAIgCAAQgIABgDAFQgFAFAAAJQAAALAFAEQAEAGAJAAIAKgCQAFgCAEgDIAAAUQgDADgGABQgFABgIAAQgRABgKgLg");
	this.shape_5.setTransform(115.45,14.95);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AgbA4IAAgTIgQAAIAAgRIAQAAIAAgIIgQAAIAAgPIAQAAIAAgiIgNAAIAAgSIAtAAQAOAAAJAFQAJAFADAHQAEAIAAAIQAAAJgEAIQgDAHgJAFQgJAFgOAAIgKAAIAAAIIAaAAIAAARIgaAAIAAATgAgFgDIAJAAQAFAAAEgCQADgCADgEQACgDABgGQgBgGgCgDQgDgDgDgCQgEgBgFAAIgJAAg");
	this.shape_6.setTransform(103.05,13.125);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AgiA5IAAgTIADgDIAJgJIAJgLIAIgJQAGgIAEgGQADgIAAgHQAAgHgDgEQgDgDgHAAIgEAAIgFACIAAAPIgTAAIAAgdQAGgDAIgCQAJgCAJAAQAPgBAJAJQAIAIAAAPQAAAIgDAIQgDAHgEAFIgMAPIgIAKIgJAKIArAAIAAATg");
	this.shape_7.setTransform(90.025,13);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AgeAYIAAgRIA9AAIAAARgAgegGIAAgRIA9AAIAAARg");
	this.shape_8.setTransform(77.825,13.45);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AgfAhQgFgFAAgKQAAgOAKgGQAKgGAWAAIAAgCQAAgFgEgCQgDgDgHAAQgGAAgFABQgHACgFAEIAAgUQAFgDAHgCIANgBQAQAAAIAHQAJAIAAAOIAAAfIAKAAIAAARIgfAAIAAgMIgBAAIgFAHQgBADgEACQgEABgGAAQgKABgGgHgAgKAHQgEADgBAEQAAABABABQAAAAAAABQAAAAABABQAAAAAAABQADABADABQAGAAACgDQAEgFABgHIAAgCQgLABgFACg");
	this.shape_9.setTransform(65.65,14.95);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("AgWAmIAAgRIAMAAIAAgpIgJAAIAAAPIgSAAIAAggIBLAAIAAAgIgSAAIAAgPIgJAAIAAApIAMAAIAAARg");
	this.shape_10.setTransform(57.25,14.95);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AgbA5IAAgRIAMAAIAHgTIgXg8IgIAAIAAgRIAYAAIAQAxIABAAIALggIgIAAIAAgRIAjAAIAAARIgIAAIgcBPIAIAAIAAARg");
	this.shape_11.setTransform(49.125,16.825);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AAKAmIAAgfIgTAAIAAAOIAJAAIAAARIgpAAIAAgRIALAAIAAgqIgLAAIAAgQIAgAAIAAAcIATAAIAAgMIgJAAIAAgQIApAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_12.setTransform(40.325,14.95);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#FFFFFF").s().p("AADAmIAAgRIAKAAIAAgaIgBAAIgZArIgeAAIAAgRIALAAIAAgqIgLAAIAAgQIAoAAIAAAQIgJAAIAAAbIABAAIAZgrIAeAAIAAAQIgLAAIAAAqIALAAIAAARg");
	this.shape_13.setTransform(30.7,14.95);

	this.shape_14 = new cjs.Shape();
	this.shape_14.graphics.f("#FFFFFF").s().p("AAZAmIAAgzIgBAAIgQAzIgRAAIgRgzIgBAAIAAAzIgeAAIAAgRIAMAAIAAgqIgMAAIAAgQIArAAIAOAwIABAAIAOgwIAqAAIAAAQIgKAAIAAAqIAKAAIAAARg");
	this.shape_14.setTransform(19.55,14.95);

	this.shape_15 = new cjs.Shape();
	this.shape_15.graphics.f("#FFFFFF").s().p("AgcA5IAAgTIAUAAIAAhFIgWAJIAAgVIAdgNIANAAIAABeIASAAIAAATg");
	this.shape_15.setTransform(5.6,13.05);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_15},{t:this.shape_14},{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.text3, new cjs.Rectangle(0,0,167.5,25.1), null);


(lib.text2 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AgQA+IAAgjIAhAAIAAAjgAgQgaIAAgjIAhAAIAAAjg");
	this.shape.setTransform(123.225,43.15);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("Ag6BUIAAgfIAHAAIATgBQAHgBAEgDQAEgDADgHIA0h5IAmAAIg7CIQgGANgGAGQgGAHgLADQgKACgRAAgAhLhTIAoAAIAjBIIgSApg");
	this.shape_1.setTransform(112.325,40.95);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AAGA4QAOgBAJgJQAKgJAEgOIAiAQQgFAMgJAKQgJALgOAIQgOAHgUABgAgpBMQgRgNgJgTQgJgUAAgYQAAgXAHgRQAHgRAMgKQALgKANgFQAOgFAMAAIAAAgQgLABgJAGQgJAIgFALQgFAMgBARQAAAPAFAMQAEAMAJAIQAJAIANABIAAAgQgYAAgRgMgAAjgnQgFgGgHgEQgHgFgKgBIAAggQATABANAGQANAGAJALQAIALAGAMIggAPQgCgHgFgHg");
	this.shape_2.setTransform(96.025,40.95);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("Ag+BUIAAinIAjAAIAACngAgUAdIAAgdIAUAAQAHAAAGgDQAGgCAFgGQAEgHAAgLQAAgLgIgIQgHgGgNAAIgUAAIAAgdIAWAAQAWAAANAIQAOAIAGAMQAGANAAANQAAARgHAMQgGANgNAIQgNAHgVABg");
	this.shape_3.setTransform(80.425,40.95);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("Ag6BUIAAgfIAHAAIATgBQAHgBAEgDQAEgDADgHIA0h5IAmAAIg7CIQgGANgGAGQgGAHgLADQgKACgRAAgAhLhTIAoAAIAjBIIgSApg");
	this.shape_4.setTransform(64.925,40.95);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AAcBUIg0hJIAAggIAxg+IAmAAIg9BMIBBBbgAhCBUIAAinIAjAAIAACng");
	this.shape_5.setTransform(49.8,40.95);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AADA4QALgBAJgGQAJgGAFgMQAGgMAAgTQAAgUgGgLQgGgMgJgGQgKgFgJgBIAAggQANAAANAEQANAGAMAKQALAKAHARQAIAQAAAYQAAAXgHARQgGAQgMALQgLAKgNAGQgNAFgPAAgAgfBSQgNgFgLgLQgLgLgGgQQgHgRAAgWQAAgXAHgRQAHgRAMgKQALgKANgFQAOgFAMAAIAAAgQgJABgJAFQgJAGgGAMQgGAMgBATQABASAFANQAGALAJAHQAJAGAKABIAAAgQgOAAgOgGg");
	this.shape_6.setTransform(27.125,40.95);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AAfBUIAAiIIgcAAIAAgfIA/AAIAACngAhCBUIAAinIA/AAIAAAfIgcAAIAACIg");
	this.shape_7.setTransform(10.1,40.95);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AgUBUIAAgfIAWAAQANAAAIgHQAHgGAAgNQAAgLgEgGQgEgGgGgDQgHgCgHABIgWAAIAAgeIAaAAQAUABANAHQAMAIAGANQAGAMAAAQQAAAKgDAKQgDAKgHAIQgHAJgLAFQgLAFgRAAgAg+BUIAAinIAjAAIAACng");
	this.shape_8.setTransform(83.675,16.4);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("Ag+BUIAAinIAjAAIAACngAgUAdIAAgdIAUAAQAHAAAGgDQAGgCAFgGQAEgHAAgLQAAgLgIgIQgHgGgNAAIgUAAIAAgdIAWAAQAWAAANAIQAOAIAGAMQAGAMAAAOQAAARgHAMQgGANgNAHQgNAIgVABg");
	this.shape_9.setTransform(68.775,16.4);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("AgQBUIAAgfIBLAAIAAAfgAg5BUIAAinIAiAAIAACngAgQANIAAgdIBEAAIAAAdgAgQg0IAAgfIBHAAIAAAfg");
	this.shape_10.setTransform(54.05,16.4);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AAfBUIAAiIIgcAAIAAgfIA/AAIAACngAhCBUIAAinIA/AAIAAAfIgcAAIAACIg");
	this.shape_11.setTransform(38.45,16.4);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AgQBUIAAgfIBKAAIAAAfgAg6BUIAAinIAjAAIAACngAgQANIAAgdIBEAAIAAAdgAgQg0IAAgfIBHAAIAAAfg");
	this.shape_12.setTransform(23.35,16.4);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#FFFFFF").s().p("AgRBUIAAinIAjAAIAACngAAZg0IAAgfIAnAAIAAAfgAg/g0IAAgfIAnAAIAAAfg");
	this.shape_13.setTransform(8.95,16.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.text2, new cjs.Rectangle(0,0,128.7,57.1), null);


(lib.text1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AgQBUIAAinIAhAAIAACng");
	this.shape.setTransform(121.05,39.95);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AAuBUIAAg7IAhhYIAACTgAgPBUIg/inIAhAAIA9CngAhOBUIAAiTIAhBXIAAA8gAAEAeIAqhxIAhAAIg6Cdg");
	this.shape_1.setTransform(108,39.95);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AADA4QALgBAJgGQAJgGAFgMQAGgNAAgSQAAgUgGgLQgGgMgJgGQgKgFgJgBIAAggQANAAANAEQANAFAMALQALAKAHARQAIAQAAAYQAAAXgHARQgGAQgMALQgLAKgNAGQgNAFgPAAgAgfBSQgNgGgLgKQgLgLgGgQQgHgRAAgWQAAgXAHgRQAHgQAMgLQALgKANgFQAOgFAMAAIAAAgQgJABgJAGQgJAFgGAMQgGAMgBATQABASAFANQAGALAJAHQAJAGAKABIAAAgQgOAAgOgGg");
	this.shape_2.setTransform(89.475,39.95);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#FFFFFF").s().p("AAnBUIg6inIAkAAIA7CngAhLBUIA0icIARAwIgRA3IAkAAIAKAcIg3AAIgIAZg");
	this.shape_3.setTransform(72.425,39.95);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#FFFFFF").s().p("AgRBUIAAinIAiAAIAACng");
	this.shape_4.setTransform(60.9,39.95);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AAlBUIhqinIAoAAIBrCngAhNBUIA1hUIAUAfIghA1gAAFgqIAZgpIAoAAIgtBIg");
	this.shape_5.setTransform(49.125,39.95);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#FFFFFF").s().p("AAnBUIg6inIAkAAIA7CngAhLBUIA0icIARAwIgRA3IAkAAIAKAcIg3AAIgIAZg");
	this.shape_6.setTransform(26.775,39.95);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#FFFFFF").s().p("AAhBUIAAhJIgeAAIAAgeIAeAAIAAhAIAjAAIAACngAhDBUIAAinIAjAAIAABAIAdAAIAAAeIgdAAIAABJg");
	this.shape_7.setTransform(10.225,39.95);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#FFFFFF").s().p("AAnBUIg6inIAkAAIA7CngAhLBUIA0icIARAwIgRA2IAkAAIAKAcIg3AAIgIAag");
	this.shape_8.setTransform(93.775,16.4);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#FFFFFF").s().p("AAbBUIgzhJIAAggIAxg+IAmAAIg9BMIBBBbgAhCBUIAAinIAjAAIAACng");
	this.shape_9.setTransform(78.35,16.4);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#FFFFFF").s().p("AAxBoIAAgoIgsAAIAAggIAVAAIAAhpIgVAAIAAgeIA4AAIAACHIAXAAIAABIgAhTBoIAAhIQANgBAFgIQAGgIABgPQACgQAAgZIAAg+IA3AAIAAAeIgUAAIAAAkQgBAYgCAQQgCASgEALIAdAAIAAAgIgvAAIAAAog");
	this.shape_10.setTransform(60.8,18.45);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#FFFFFF").s().p("AAhBUIAAinIAjAAIAACngAhDBUIAAinIAjAAIAACngAgZAOIAzhUIAAA5IgzBVg");
	this.shape_11.setTransform(43.175,16.4);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#FFFFFF").s().p("AAbBUIgzhJIAAggIAwg+IAnAAIg8BMIBABbgAhCBUIAAinIAjAAIAACng");
	this.shape_12.setTransform(27.35,16.4);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#FFFFFF").s().p("AAGA4QAOgCAJgIQAKgIAEgPIAiAQQgFALgJAMQgJAKgOAIQgOAHgUACgAgpBLQgRgLgJgUQgJgTAAgZQAAgYAHgQQAHgRAMgKQALgKANgFQAOgFAMAAIAAAgQgLABgJAGQgJAIgFALQgFAMgBARQAAAOAFANQAEAMAJAIQAJAHANACIAAAhQgYgCgRgMgAAjgnQgFgGgHgFQgHgEgKgBIAAggQATABANAGQANAHAJAKQAIALAGAMIggAPQgCgHgFgHg");
	this.shape_13.setTransform(10.425,16.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.text1, new cjs.Rectangle(0,0,127,56.1), null);


(lib.color_white = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AnzH0IAAvnIPnAAIAAPng");

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.color_white, new cjs.Rectangle(-50,-50,100,100), null);


(lib.color_pink = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#CF2C91").s().p("AnzH0IAAvnIPnAAIAAPng");

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.color_pink, new cjs.Rectangle(-50,-50,100,100), null);


(lib.color_black = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Слой_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("AxLNSIAA6jMAiXAAAIAAajg");
	this.shape.setTransform(-110,-85);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.color_black, new cjs.Rectangle(-220,-170,220,170), null);


(lib.cifrline = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_3
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("AAJHrIAAivIAkAAIAABrIAXAAIAAAaIgXAAIAAAqgAhCHBIAAgZIBEhiIAAAtIgkA0IAkAAIAAAagAgpDgIApggIA/AAIAAAggAg/DgIAAggIAzgmQAPgNAJgJQAJgIADgHQACgHAAgJQAAgFgCgGQgDgGgFgEQgFgFgIgBIAAgeQAUABANAIQANAIAHANQAHAMAAARQAAAOgGAMQgGALgKAJQgJAJgLAIIhKA6gAg/B0IAAgPQAAgJAEgKQADgJAIgJQAHgIALgGQAMgGAPAAIAAAeQgIABgFAEQgGAEgDAHQgEAGAAAHIABAJIAAAHgAgFgrIAAhwQAAgGgCgBQgCgBgGAAIgYAAIAAgYQAOAAAJgGQAIgEAFgHQADgHACgHIAcAAIAACvgAAElRQAIgBAHgGQAHgGAEgNQAEgMAAgYQAAgdgIgPQgJgOgNgCIAAgfQATABAPAKQAPALAJATQAJAUAAAeQAAAfgKAUQgJAVgPAJQgPALgSABgAgkk9QgPgKgKgUQgJgVAAgeQAAgeAKgUQAJgUAPgLQAPgKASgBIAAAfQgOACgIAPQgIAQAAAcQAAAeAJAPQAIAPANABIAAAfQgSgBgPgKg");
	this.shape.setTransform(9.875,56.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.cifrline, new cjs.Rectangle(0,0,19.8,132.5), null);


(lib.bluegr = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.rf(["#299FE3","rgba(41,159,227,0)"],[0,1],0,0,0,0,0,32.6).s().p("AjhDiQhehdAAiFQAAiDBeheQBdheCEAAQCEAABeBeQBeBeAACDQAACFheBdQheBeiEAAQiEAAhdheg");
	this.shape.setTransform(32,32);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.bluegr, new cjs.Rectangle(0,0,64,64), null);


(lib.blueball = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.rf(["#E3F7F9","rgba(146,214,248,0)"],[0.294,0.682],0,0,0,0,0,33.3).s().p("AjpDpQhghgAAiJQAAiIBghhQBhhgCIAAQCJAABgBgQBhBhAACIQAACJhhBgQhgBhiJAAQiIAAhhhhg");
	this.shape.setTransform(33,33);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.blueball, new cjs.Rectangle(0,0,66,66), null);


(lib.agelimit = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#9A9A9A").s().p("AgFAjIAAgeIgbAAIAAgLIAbAAIAAgcIAMAAIAAAcIAaAAIAAALIgaAAIAAAeg");
	this.shape.setTransform(19.425,14.25);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#9A9A9A").s().p("AgbAxQgKgOgBgbQAAgUAEgPQAEgQAIgIQAJgJAPAAQAKAAAIADQAHAEAEAHQAEAHABAJIgPAAQgCgIgFgEQgFgFgHAAQgJABgFAGQgGAGgCALQgCAKgBAMIACAAQADgFAGgEQAGgEAJAAQALAAAIAEQAIAGAFAHQAEAJAAALQAAAMgEAIQgGAJgIAFQgJAFgMgBQgRABgKgNgAgOAFQgGAHAAALQAAAHADAGQACAFAGAEQAEADAGAAQAGAAAEgDQAFgDAEgGQACgFAAgIQAAgIgCgGQgEgFgFgCQgEgDgGAAQgJABgGAFg");
	this.shape_1.setTransform(10.55,13.85);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.agelimit, new cjs.Rectangle(4,0,22,26.5), null);


(lib.whandphonephone2 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.whandphonephone();
	this.instance.setTransform(24,35,1,1,0,0,0,24,35);

	this.timeline.addTween(cjs.Tween.get(this.instance).to({y:33},19).to({y:35},20).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,-2,48,72);


(lib.whandphoneglow21 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.whandphoneglow2();
	this.instance.setTransform(40,110,1,1,0,0,0,40,110);
	this.instance.alpha = 0.5508;
	this.instance.compositeOperation = "lighter";

	this.timeline.addTween(cjs.Tween.get(this.instance).to({scaleX:1.04,scaleY:1.04},24).to({scaleX:1,scaleY:1},25).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-1.6,-4.4,83.19999999999999,228.8);


(lib.whandphoneglow3anim2 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.whandphoneglow3();
	this.instance.setTransform(40,110,1,1,0,0,0,40,110);
	this.instance.alpha = 0;

	this.timeline.addTween(cjs.Tween.get(this.instance).to({alpha:1},8).wait(12).to({alpha:0},9).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,80,220);


(lib.whandphone1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// whandphoneglow2
	this.instance = new lib.whandphoneglow21();
	this.instance.setTransform(40,110,1,1,0,0,0,40,110);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(200));

	// whandphoneglow1
	this.instance_1 = new lib.whandphoneglow1();
	this.instance_1.setTransform(40,110,1,1,0,0,0,40,110);
	this.instance_1.alpha = 0.6992;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(200));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,80,220);


(lib.strelkanim = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.strelka();
	this.instance.setTransform(10.5,7.5,1,1,0,0,0,10.5,7.5);

	this.timeline.addTween(cjs.Tween.get(this.instance).to({y:5.5},9).to({y:7.5},9).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,-2,21.1,17);


(lib.sparklanim = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.sparkl();
	this.instance.setTransform(1,1,1,1,0,0,0,1,1);
	this.instance.compositeOperation = "lighter";

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1).to({y:-0.6,alpha:0.992},0).wait(1).to({y:-2.2,alpha:0.9817},0).wait(1).to({y:-3.8,alpha:0.9686},0).wait(1).to({y:-5.4,alpha:0.9516},0).wait(1).to({y:-7,alpha:0.9296},0).wait(1).to({y:-8.6,alpha:0.9008},0).wait(1).to({y:-10.25,alpha:0.8633},0).wait(1).to({y:-11.85,alpha:0.8139},0).wait(1).to({y:-13.45,alpha:0.749},0).wait(1).to({y:-15.05,alpha:0.6636},0).wait(1).to({y:-16.65,alpha:0.5518},0).wait(1).to({y:-18.25,alpha:0.407},0).wait(1).to({y:-19.85,alpha:0.2239},0).wait(1).to({y:-21.5,alpha:0},0).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,-22.5,2,24.5);


(lib.sparklall = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// sparkl
	this.instance = new lib.sparklanim("synched",4);
	this.instance.setTransform(57.75,45.9,0.9998,0.9998,53.9991,0,0,1.1,1);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(15));

	// sparkl
	this.instance_1 = new lib.sparklanim("synched",10);
	this.instance_1.setTransform(51.5,38.4,0.9999,0.9999,43.0001,0,0,1.1,1);

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(15));

	// sparkl
	this.instance_2 = new lib.sparklanim("synched",5);
	this.instance_2.setTransform(33.2,18.35,0.9999,0.9999,14.9991,0,0,1,1.1);

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(15));

	// sparkl
	this.instance_3 = new lib.sparklanim("synched",1);
	this.instance_3.setTransform(23.25,15.9,0.9999,0.9999,2.9996,0,0,1,1.1);

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(15));

	// sparkl
	this.instance_4 = new lib.sparklanim("synched",13);
	this.instance_4.setTransform(12.3,19.95,0.9999,0.9999,-9.9991,0,0,1,1.1);

	this.timeline.addTween(cjs.Tween.get(this.instance_4).wait(15));

	// sparkl
	this.instance_5 = new lib.sparklanim("synched",0);
	this.instance_5.setTransform(14.7,42.3,0.9999,0.9999,-62.0018,0,0,1,1);

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(15));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-6.2,-7.6,83.10000000000001,54.4);


(lib.minanim = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {a1:9};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// timeline functions:
	this.frame_48 = function() {
		this.gotoAndPlay('a1');
	}

	// actions tween:
	this.timeline.addTween(cjs.Tween.get(this).wait(48).call(this.frame_48).wait(1));

	// Layer_1
	this.instance = new lib.min();
	this.instance.setTransform(60,70,1,1,0,0,0,60,70);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(9).to({scaleX:1.06,scaleY:1.06,x:60.05,y:70.55},19,cjs.Ease.cubicOut).to({scaleX:1,scaleY:1,x:60,y:70},20,cjs.Ease.cubicOut).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-3.5,-3.6,127.2,148.4);


(lib.fon_color = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.color_pink();

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(1));

	this._renderFirstFrame();

}).prototype = getMCSymbolPrototype(lib.fon_color, new cjs.Rectangle(-50,-50,100,100), null);


(lib.cifrlineanim_rub = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_6
	this.shape = new cjs.Shape();
	this.shape.graphics.lf(["#FFFFFF","rgba(255,255,255,0)"],[0.176,1],-0.4,0.6,-0.4,-2).s().p("AlJAgIAAg/IKTAAIAAA/g");
	this.shape.setTransform(33,29.25);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.lf(["#FFFFFF","rgba(255,255,255,0)"],[0.176,1],0.4,0.7,0.4,3.3).s().p("AlJAtIAAhZIKTAAIAABZg");
	this.shape_1.setTransform(33,4.5);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(141));

	// Layer_1 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("AlJB9IAAj5IKTAAIAAD5g");
	mask.setTransform(33,17.5);

	// cifrline
	this.instance = new lib.cifrline();
	this.instance.setTransform(9.9,97.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(34).to({y:70.6},10).wait(97));

	// cifrline
	this.instance_1 = new lib.cifrline();
	this.instance_1.setTransform(24.9,150.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance_1];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(141));

	// cifrline
	this.instance_2 = new lib.cifrline();
	this.instance_2.setTransform(40.9,150.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance_2];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(141));

	// cifrline
	this.instance_3 = new lib.cifrline();
	this.instance_3.setTransform(56.9,150.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance_3];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(141));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,66,32.5);


(lib.cifrlineanim_min = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_6
	this.shape = new cjs.Shape();
	this.shape.graphics.lf(["#FFFFFF","rgba(255,255,255,0)"],[0.176,1],-0.4,0.6,-0.4,-2).s().p("AlJAgIAAg/IKTAAIAAA/g");
	this.shape.setTransform(33,29.25);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.lf(["#FFFFFF","rgba(255,255,255,0)"],[0.176,1],0.4,0.7,0.4,3.3).s().p("AlJAtIAAhZIKTAAIAABZg");
	this.shape_1.setTransform(33,4.5);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(141));

	// Layer_1 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("AlJB9IAAj5IKTAAIAAD5g");
	mask.setTransform(33,17.5);

	// cifrline
	this.instance = new lib.cifrline();
	this.instance.setTransform(9.9,123.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(34).to({y:97.6},10).wait(97));

	// cifrline
	this.instance_1 = new lib.cifrline();
	this.instance_1.setTransform(24.9,150.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance_1];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(141));

	// cifrline
	this.instance_2 = new lib.cifrline();
	this.instance_2.setTransform(40.9,150.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance_2];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(141));

	// cifrline
	this.instance_3 = new lib.cifrline();
	this.instance_3.setTransform(56.9,150.6,1,1,0,0,0,9.9,150.6);

	var maskedShapeInstanceList = [this.instance_3];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(141));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,66,32.5);


(lib.button = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// text
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AhuAxIAAgTIgVAAIAAgOIAKAAIAAgvIgKAAIAAgPIAaAAIAAA+IALAAIAAAhgAisAxIAAghQAGgBADgDQACgEABgHIABgSIAAgdIAZAAIAAAPIgJAAIAAAQIgBARQgBAIgCAGIANAAIAAAOIgVAAIAAATgAAQARQAEAAAFgDQAEgDACgFQADgGAAgHQAAgKgDgFQgDgGgEgCQgEgDgEAAIAAgPQAFAAAGADQAGACAGAEQAFAFADAIQAEAHAAAMQAAAJgDAIQgDAHgFAFQgFAFgHADQgGACgGAAgAAAAdQgFgCgFgFQgFgFgDgIQgDgHAAgJQAAgLADgIQADgIAFgEQAGgFAFgCQAGgDAGAAIAAAPQgFAAgEADQgEADgCAFQgDAGAAAJQAAAHADAGQACAFAEADQAEADAFAAIAAAPQgHAAgGgDgAjUARQAEAAAFgDQAEgDACgFQADgGAAgHQAAgKgDgFQgDgGgEgCQgEgDgEAAIAAgPQAFAAAGADQAGACAGAEQAFAFADAIQAEAHAAAMQAAAJgDAIQgDAHgFAFQgFAFgHADQgGACgGAAgAjkAdQgGgCgFgFQgFgFgDgIQgDgHAAgJQAAgLADgIQADgIAFgEQAGgFAGgCQAGgDAGAAIAAAPQgFAAgEADQgEADgDAFQgDAGAAAJQAAAHADAGQADAFAEADQAEADAFAAIAAAPQgHAAgGgDgAEgAeIAAgOIAiAAIAAAOgAEMAeIAAhMIAQAAIAABMgADfAeIAAgOIAjAAIAAAOgADMAeIAAhMIAQAAIAABMgACuAeIAAggIgNAAIAAgOIANAAIAAgeIARAAIAABMgACAAeIAAhMIAQAAIAAAeIAOAAIAAAOIgOAAIAAAggABQAeIAAgOIALAAQAGAAADgDQAEgDAAgGQAAgEgCgCQgCgDgDgBIgGAAIgLAAIAAgNIAMAAQAKAAAFADQAGADADAFQACAGAAAGIgBAJQgBAFgDAEQgDAEgGACQgFACgHAAgAA9AeIAAhMIAQAAIAABMgAhWAeIAAhMIAQAAIAABMgAkUAeIAAg9IgNAAIAAgPIAdAAIAABMgAlBAeIAAhMIAdAAIAAAPIgNAAIAAA9gAhCAFIAAgNIAJAAIAGgBQADgBACgDQACgDAAgFQAAgFgEgDQgDgDgGAAIgJAAIAAgOIAKAAQAKAAAGAEQAGADADAGQADAGAAAGQAAAIgDAGQgDAGgGACQgGAEgJAAgAEggBIAAgOIAfAAIAAAOgADfgBIAAgOIAfAAIAAAOgAEggfIAAgPIAhAAIAAAPgADfgfIAAgPIAhAAIAAAPgABQgfIAAgPIAgAAIAAAPg");
	this.shape.setTransform(1.225,0.875);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#CF2C91").s().p("AhuAxIAAgTIgVAAIAAgOIAKAAIAAgvIgKAAIAAgPIAaAAIAAA+IALAAIAAAhgAisAxIAAghQAGgBADgDQACgEABgHIABgSIAAgdIAZAAIAAAPIgJAAIAAAQIgBARQgBAIgCAGIANAAIAAAOIgVAAIAAATgAAQARQAEAAAFgDQAEgDACgFQADgGAAgHQAAgKgDgFQgDgGgEgCQgEgDgEAAIAAgPQAFAAAGADQAGACAGAEQAFAFADAIQAEAHAAAMQAAAJgDAIQgDAHgFAFQgFAFgHADQgGACgGAAgAAAAdQgFgCgFgFQgFgFgDgIQgDgHAAgJQAAgLADgIQADgIAFgEQAGgFAFgCQAGgDAGAAIAAAPQgFAAgEADQgEADgCAFQgDAGAAAJQAAAHADAGQACAFAEADQAEADAFAAIAAAPQgHAAgGgDgAjUARQAEAAAFgDQAEgDACgFQADgGAAgHQAAgKgDgFQgDgGgEgCQgEgDgEAAIAAgPQAFAAAGADQAGACAGAEQAFAFADAIQAEAHAAAMQAAAJgDAIQgDAHgFAFQgFAFgHADQgGACgGAAgAjkAdQgGgCgFgFQgFgFgDgIQgDgHAAgJQAAgLADgIQADgIAFgEQAGgFAGgCQAGgDAGAAIAAAPQgFAAgEADQgEADgDAFQgDAGAAAJQAAAHADAGQADAFAEADQAEADAFAAIAAAPQgHAAgGgDgAEgAeIAAgOIAiAAIAAAOgAEMAeIAAhMIAQAAIAABMgADfAeIAAgOIAjAAIAAAOgADMAeIAAhMIAQAAIAABMgACuAeIAAggIgNAAIAAgOIANAAIAAgeIARAAIAABMgACAAeIAAhMIAQAAIAAAeIAOAAIAAAOIgOAAIAAAggABQAeIAAgOIALAAQAGAAADgDQAEgDAAgGQAAgEgCgCQgCgDgDgBIgGAAIgLAAIAAgNIAMAAQAKAAAFADQAGADADAFQACAGAAAGIgBAJQgBAFgDAEQgDAEgGACQgFACgHAAgAA9AeIAAhMIAQAAIAABMgAhWAeIAAhMIAQAAIAABMgAkUAeIAAg9IgNAAIAAgPIAdAAIAABMgAlBAeIAAhMIAdAAIAAAPIgNAAIAAA9gAhCAFIAAgNIAJAAIAGgBQADgBACgDQACgDAAgFQAAgFgEgDQgDgDgGAAIgJAAIAAgOIAKAAQAKAAAGAEQAGADADAGQADAGAAAGQAAAIgDAGQgDAGgGACQgGAEgJAAgAEggBIAAgOIAfAAIAAAOgADfgBIAAgOIAfAAIAAAOgAEggfIAAgPIAhAAIAAAPgADfgfIAAgPIAhAAIAAAPgABQgfIAAgPIAgAAIAAAPg");
	this.shape_1.setTransform(1.225,0.875);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape}]}).to({state:[{t:this.shape_1}]},1).wait(3));

	// fon_color
	this.instance = new lib.fon_color();
	this.instance.setTransform(0,-0.05,0.8,0.2,0,0,0,0,-0.2);

	this.timeline.addTween(cjs.Tween.get(this.instance).to({_off:true},1).wait(3));

	// color_white
	this.instance_1 = new lib.color_white();
	this.instance_1.setTransform(0,0.05,0.8,0.2,0,0,0,0,0.2);
	this.instance_1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(1).to({_off:false},0).wait(3));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-40,-10,80,20);


(lib.bluegranim = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.bluegr();
	this.instance.setTransform(32,32,1,1,0,0,0,32,32);
	this.instance.alpha = 0.3516;
	this.instance.compositeOperation = "lighter";

	this.timeline.addTween(cjs.Tween.get(this.instance).to({scaleX:1.23,scaleY:1.23},14).to({scaleX:1,scaleY:1},15).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-7.3,-7.3,78.7,78.7);


(lib.whandphoneglow3anim3 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_1
	this.instance = new lib.whandphoneglow3anim2("synched",0,false);
	this.instance.setTransform(40,140,1,1,0,0,0,40,110);

	this.timeline.addTween(cjs.Tween.get(this.instance).to({y:80,startPosition:29},29).wait(1));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,-30,80,280);


(lib.whandphoneglow3anim = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_6
	this.instance = new lib.whandphoneglow3anim3("synched",19);
	this.instance.setTransform(25,99.5,1,1,0,0,0,40,110);
	this.instance.alpha = 0.3516;

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(30));

	// Layer_5
	this.instance_1 = new lib.whandphoneglow3anim3("synched",9);
	this.instance_1.setTransform(46,90.5,1,1,0,0,0,40,110);
	this.instance_1.alpha = 0.3516;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(30));

	// Layer_1
	this.instance_2 = new lib.whandphoneglow3anim3("synched",0);
	this.instance_2.setTransform(35,90,1,1,0,0,0,40,110);
	this.instance_2.alpha = 0.3516;

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(30));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-15,-50,101,289.5);


(lib.whandmin = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_7
	this.instance = new lib.blueball();
	this.instance.setTransform(58.15,74.65,0.094,0.094,0,0,0,33.5,34);

	this.timeline.addTween(cjs.Tween.get(this.instance).to({regX:33.1,regY:33,scaleX:0.5127,scaleY:0.5127,x:58.1,y:74.6},4).wait(2).to({alpha:0.3008},14).to({_off:true},354).wait(61));

	// whandminglow3
	this.instance_1 = new lib.minanim();
	this.instance_1.setTransform(58.1,81.45,0.188,0.188,0,0,0,60.1,86.2);
	this.instance_1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(2).to({_off:false},0).to({regX:60,regY:86,scaleX:0.94,scaleY:0.94,x:59,y:84.05},14,cjs.Ease.cubicOut).to({_off:true},358).wait(61));

	// sparkl
	this.instance_2 = new lib.sparklall("synched",0);
	this.instance_2.setTransform(55.05,43.35,0.94,0.94,0,0,0,29.5,23.3);
	this.instance_2.alpha = 0;
	this.instance_2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(6).to({_off:false},0).to({alpha:1},14).to({_off:true},354).wait(61));

	// Layer_2
	this.instance_3 = new lib.bluegranim("synched",0);
	this.instance_3.setTransform(56.4,51.1,0.94,0.94,0,0,0,32,32);
	this.instance_3.alpha = 0;
	this.instance_3._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(6).to({_off:false},0).to({alpha:0.3008},14).to({_off:true},354).wait(61));

	// whandminglow1
	this.instance_4 = new lib.whandminglow1();
	this.instance_4.setTransform(58.1,81.45,0.188,0.188,0,0,0,60.1,86.2);
	this.instance_4._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_4).wait(2).to({_off:false},0).to({regX:60,regY:86,scaleX:0.94,scaleY:0.94,x:59,y:84.05,alpha:0.5},14,cjs.Ease.cubicOut).to({_off:true},358).wait(61));

	// whandminladon
	this.instance_5 = new lib.whandminladon();
	this.instance_5.setTransform(55.2,92.6,1,1,0,0,0,30.5,24);

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(419).to({_off:true},1).wait(15));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(2.5,3.1,112.9,131.70000000000002);


(lib.handcifranim1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_4 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("Al9P4QhQAAAAhQIAA9PQAAhQBQAAIL7AAQBQAAAABQIAAdPQAABQhQAAg");
	mask.setTransform(154,111.875);

	// Layer_5
	this.instance = new lib.phoneblick();
	this.instance.setTransform(41.95,95.1,0.5,1.5379,-149.9999,0,0,180.8,179.8);
	this.instance.alpha = 0.8008;
	this.instance._off = true;

	var maskedShapeInstanceList = [this.instance];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(4).to({_off:false},0).to({regX:180.5,scaleY:1.538,rotation:-149.9995,x:307.95,y:208.15},40,cjs.Ease.cubicOut).wait(116));

	// Layer_6
	this.instance_1 = new lib.phoneblick();
	this.instance_1.setTransform(171.85,293.15,0.3994,1.5381,20.0006,0,0,180.7,179.8);
	this.instance_1.alpha = 0.6016;
	this.instance_1._off = true;

	var maskedShapeInstanceList = [this.instance_1];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(19).to({_off:false},0).to({regX:180.6,rotation:29.9996,x:156.95,y:63.1},25,cjs.Ease.cubicOut).wait(116));

	// str
	this.instance_2 = new lib.strelkanim();
	this.instance_2.setTransform(153.75,132.35,1,1,0,0,0,10.5,7.5);

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(160));

	// podp
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("AgNA4IAAgVIAOAAQAJAAAFgEQAFgEAAgJQAAgHgCgDQgDgFgEgBIgKgBIgOAAIAAgSIAQAAQAPABAIAEQAIAEAEAIQAEAHAAALQAAAHgCAGQgCAIgEAFQgFAGgIADQgHADgLAAgAgpA4IAAhvIAYAAIAABvgAgNgiIAAgVIAtAAIAAAVg");
	this.shape.setTransform(163.2,106.6);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#000000").s().p("AgmA4IAAgVIAFAAQAHAAAFAAQAFgBADgCQACgCACgEIAihRIAZAAIgnBaQgDAIgFAFQgDAEgHACQgHACgLAAgAgxg3IAaAAIAXAwIgMAag");
	this.shape_1.setTransform(153,106.6);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("AgpA4IAAhvIAYAAIAABvgAgNATIAAgTIANAAQAEAAAFgBQAEgCADgEQACgFAAgGQAAgJgEgEQgGgEgIAAIgNAAIAAgUIAOAAQAPAAAJAFQAJAGAEAIQAEAIAAAKQAAALgFAHQgEAJgIAEQgJAGgOAAg");
	this.shape_2.setTransform(143.15,106.6);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#000000").s().p("AAWA4IAAgxIgUAAIAAgTIAUAAIAAgrIAXAAIAABvgAgsA4IAAhvIAXAAIAAArIAUAAIAAATIgUAAIAAAxg");
	this.shape_3.setTransform(164.875,180.6);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("AAWA4IAAhvIAXAAIAABvgAgsA4IAAhvIAXAAIAABvgAgQAKIAhg5IAAAmIghA5g");
	this.shape_4.setTransform(153.925,180.6);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#000000").s().p("AAfA4IAAgnIAWg7IAABigAgKA4IgqhvIAWAAIApBvgAg0A4IAAhiIAWA7IAAAngAADAUIAchLIAWAAIgnBog");
	this.shape_5.setTransform(142.225,180.6);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(160));

	// cifrlineanim_min
	this.instance_3 = new lib.cifrlineanim_min("synched",0,false);
	this.instance_3.setTransform(153.4,293.6,1,1,0,0,0,33.4,150.6);

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(160));

	// cifrlineanim
	this.instance_4 = new lib.cifrlineanim_rub("synched",0,false);
	this.instance_4.setTransform(153.4,219.6,1,1,0,0,0,33.4,150.6);

	this.timeline.addTween(cjs.Tween.get(this.instance_4).wait(160));

	// logo
	this.instance_5 = new lib.logo();
	this.instance_5.setTransform(154.05,35,0.5376,0.5365,0,0,0,0.1,0);

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(160));

	// Layer_10 (mask)
	var mask_1 = new cjs.Shape();
	mask_1._off = true;
	mask_1.graphics.p("AirEhIAApBIFXAAIAACxQgJADgHAFIgMAHQgHADgDAYQgDASABATIADAiQADAXAIAMIAPAYQAJAOACACIAADUg");
	mask_1.setTransform(186.375,158.4);

	// Layer_12
	this.instance_6 = new lib.handcifrosn1();
	this.instance_6.setTransform(160,200,1,1,0,0,0,120,200);

	this.timeline.addTween(cjs.Tween.get(this.instance_6).wait(160));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,280,440);


(lib.woman1 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// Layer_5 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	var mask_graphics_24 = new cjs.Graphics().p("AFjMXQg/gfjpjRIjZjLIk3ySIbQBaIAUNbQg0BchCBnQiBDPg/A1QhRBFhTA1QhdA7hLAZQhdAfg3ADIgTABQhCAAhBggg");
	var mask_graphics_67 = new cjs.Graphics().p("AFjMXQg/gfjpjRIjZjLIk3ySIbQBaIAUNbQg0BchCBnQiBDPg/A1QhRBFhTA1QhdA7hLAZQhdAfg3ADIgTABQhCAAhBggg");

	this.timeline.addTween(cjs.Tween.get(mask).to({graphics:null,x:0,y:0}).wait(24).to({graphics:mask_graphics_24,x:129.5,y:57.3555}).wait(43).to({graphics:mask_graphics_67,x:129.5,y:57.3555}).wait(313).to({graphics:null,x:0,y:0}).wait(40));

	// whandphone11
	this.instance = new lib.whandphoneglow3anim("synched",0);
	this.instance.setTransform(197.5,110,1,1,0,0,0,40,110);
	this.instance.alpha = 0;
	this.instance._off = true;

	var maskedShapeInstanceList = [this.instance];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(24).to({_off:false},0).to({alpha:1,startPosition:8},8).to({startPosition:15},37).to({alpha:0,startPosition:23},8).to({startPosition:5},102).to({alpha:1,startPosition:14},9).to({_off:true},161).wait(71));

	// whandphone2
	this.instance_1 = new lib.whandphonephone2("synched",0);
	this.instance_1.setTransform(197.1,106.75,0.85,0.85,0,0,0,24.1,35);
	this.instance_1.alpha = 0;
	this.instance_1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(24).to({_off:false},0).to({y:82.35,alpha:1,startPosition:16},16,cjs.Ease.cubicOut).to({startPosition:5},29).to({regX:24.2,regY:35.2,scaleX:0.7697,scaleY:0.7697,rotation:-5.8141,x:189.4,y:135.5,startPosition:17},12,cjs.Ease.quadInOut).to({alpha:0,startPosition:20},3).to({startPosition:35},95).to({regX:24.1,regY:35.1,scaleX:0.85,scaleY:0.85,rotation:-3.9994,x:188.65,y:136.85,startPosition:36},1).to({regY:35,rotation:0,x:197.1,y:106.75,startPosition:37},1).wait(1).to({regX:24,regY:34,x:197,y:105.3,alpha:0.0237,startPosition:38},0).wait(1).to({y:104.35,alpha:0.0621,startPosition:39},0).wait(1).to({y:103,alpha:0.1176,startPosition:0},0).wait(1).to({y:101.2,alpha:0.1917,startPosition:1},0).wait(1).to({y:98.95,alpha:0.2832,startPosition:2},0).wait(1).to({y:96.45,alpha:0.3865,startPosition:3},0).wait(1).to({y:93.85,alpha:0.4926,startPosition:4},0).wait(1).to({y:91.4,alpha:0.5926,startPosition:5},0).wait(1).to({y:89.25,alpha:0.6809,startPosition:6},0).wait(1).to({y:87.45,alpha:0.7558,startPosition:7},0).wait(1).to({y:85.9,alpha:0.8177,startPosition:8},0).wait(1).to({y:84.7,alpha:0.868,startPosition:9},0).wait(1).to({y:83.7,alpha:0.908,startPosition:10},0).wait(1).to({y:82.95,alpha:0.9393,startPosition:11},0).wait(1).to({y:82.4,alpha:0.963,startPosition:12},0).wait(1).to({y:81.95,alpha:0.9801,startPosition:13},0).wait(1).to({y:81.7,alpha:0.9915,startPosition:14},0).wait(1).to({y:81.5,alpha:0.998,startPosition:15},0).wait(1).to({regX:24.1,regY:35,x:197.1,y:82.35,alpha:1,startPosition:16},0).to({_off:true},149).wait(71));

	// whandphone1
	this.instance_2 = new lib.whandphone1("synched",0);
	this.instance_2.setTransform(194,89.9,1,1,0,0,0,36,92.9);
	this.instance_2.alpha = 0;
	this.instance_2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(24).to({_off:false},0).to({alpha:1,startPosition:8},8).to({startPosition:45},37).to({alpha:0,startPosition:53},8).to({startPosition:155},102).to({alpha:1,startPosition:164},9).to({_off:true},161).wait(71));

	// Layer_2
	this.instance_3 = new lib.handcifranim1("synched",0);
	this.instance_3.setTransform(190.9,133.5,0.23,0.23,11.0005,0,0,157.1,110.8);
	this.instance_3.alpha = 0;
	this.instance_3._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(79).to({_off:false},0).to({alpha:1,startPosition:1},1).to({startPosition:95},94).to({alpha:0,startPosition:98},3).to({_off:true},172).wait(71));

	// wbody1
	this.instance_4 = new lib.wbody1();
	this.instance_4.setTransform(70,200,1,1,0,0,0,70,200);

	this.timeline.addTween(cjs.Tween.get(this.instance_4).wait(420));

	// whand31
	this.instance_5 = new lib.whand31();
	this.instance_5.setTransform(108.3,236,1,1,144.0159,0,0,11.7,115.4);

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(4).to({regX:11.8,regY:115.5,rotation:0,x:147.05,y:225.25},20,cjs.Ease.cubicInOut).wait(55).to({alpha:0},1).wait(94).to({alpha:1},3).wait(203).to({regX:11.7,regY:115.4,rotation:144.0159,x:108.3,y:236},0).wait(40));

	// whand21
	this.instance_6 = new lib.whand21();
	this.instance_6.setTransform(108.15,235.95,1,1,144.2552,0,0,12.2,115.7);

	this.timeline.addTween(cjs.Tween.get(this.instance_6).wait(4).to({regY:115.8,rotation:0,x:147.05,y:224.95},20,cjs.Ease.cubicInOut).wait(67).to({alpha:0},3).wait(74).to({alpha:1},3).wait(209).to({regY:115.7,rotation:144.2552,x:108.15,y:235.95},0).wait(40));

	// whand11
	this.instance_7 = new lib.whand11();
	this.instance_7.setTransform(107.15,136.65,1,1,22.7431,0,0,16.4,13.5);

	this.timeline.addTween(cjs.Tween.get(this.instance_7).wait(4).to({regY:13.4,rotation:0,x:107.2,y:136.55},20,cjs.Ease.cubicInOut).wait(356).to({regY:13.5,rotation:22.7431,x:107.15,y:136.65},0).wait(40));

	this._renderFirstFrame();

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,-24.9,278.3,484.9);


// stage content:
(lib._300x600 = function(mode,startPosition,loop,reversed) {
if (loop == null) { loop = true; }
if (reversed == null) { reversed = false; }
	var props = new Object();
	props.mode = mode;
	props.startPosition = startPosition;
	props.labels = {};
	props.loop = loop;
	props.reversed = reversed;
	cjs.MovieClip.apply(this,[props]);

	// bord
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#DADADA").ss(2,1,1).p("EgXbgu3MAu3AAAMAAABdvMgu3AAAg");
	this.shape.setTransform(150,300);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(420));

	// agelimit
	this.instance = new lib.agelimit();
	this.instance.setTransform(0,16,1.25,1.25);

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(420));

	// Layer_3
	this.instance_1 = new lib.text6();
	this.instance_1.setTransform(153,286,1.25,1.25,0,0,0,87.4,35.8);
	this.instance_1.alpha = 0;
	this.instance_1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(324).to({_off:false},0).to({alpha:1},15).wait(50).to({alpha:0},15).wait(16));

	// button
	this.instance_2 = new lib.button();
	this.instance_2.setTransform(81.1,556.5,1.25,1.25,0,0,0,0.4,0.2);
	this.instance_2.alpha = 0;
	this.instance_2._off = true;
	new cjs.ButtonHelper(this.instance_2, 0, 1, 2, false, new lib.button(), 3);

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(174).to({_off:false},0).to({alpha:1},15).wait(55).to({alpha:0},15).to({_off:true},1).wait(160));

	// text5
	this.instance_3 = new lib.text5();
	this.instance_3.setTransform(125,499.25,1.25,1.25,0,0,0,78,20.2);
	this.instance_3.alpha = 0;
	this.instance_3._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(169).to({_off:false},0).to({alpha:1},15).wait(60).to({alpha:0},15).to({_off:true},1).wait(160));

	// text4
	this.instance_4 = new lib.text4();
	this.instance_4.setTransform(128,427.25,1.25,1.25,0,0,0,81.4,41.4);
	this.instance_4.alpha = 0;
	this.instance_4._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_4).wait(164).to({_off:false},0).to({alpha:1},15).wait(65).to({alpha:0},15).wait(161));

	// text3
	this.instance_5 = new lib.text3();
	this.instance_5.setTransform(121.5,488.5,1.25,1.25,0,0,0,75.2,14.6);
	this.instance_5.alpha = 0;
	this.instance_5._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(79).to({_off:false},0).to({alpha:1},15).wait(50).to({alpha:0},15).to({_off:true},1).wait(260));

	// text2
	this.instance_6 = new lib.text2();
	this.instance_6.setTransform(131.65,424,1.25,1.25,0,0,0,83.3,37.8);
	this.instance_6.alpha = 0;
	this.instance_6._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_6).wait(79).to({_off:false},0).to({alpha:1},15).wait(50).to({alpha:0},15).to({_off:true},1).wait(260));

	// text3
	this.instance_7 = new lib.text11();
	this.instance_7.setTransform(131.75,491.95,1.375,1.375,0,0,0,75.2,14.7);
	this.instance_7.alpha = 0;
	this.instance_7._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_7).wait(9).to({_off:false},0).to({alpha:1},15).wait(35).to({alpha:0},15).to({_off:true},1).wait(345));

	// text1
	this.instance_8 = new lib.text1();
	this.instance_8.setTransform(118,434.2,1.375,1.375,0,0,0,66.2,42.5);
	this.instance_8.alpha = 0;
	this.instance_8._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_8).wait(9).to({_off:false},0).to({alpha:1},15).wait(35).to({alpha:0},15).to({_off:true},1).wait(345));

	// logomi
	this.instance_9 = new lib.logomi();
	this.instance_9.setTransform(45.75,554.5,1.25,1.25,0,0,0,14.1,14.1);
	this.instance_9.alpha = 0;
	this.instance_9._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_9).wait(9).to({_off:false},0).to({alpha:1},15).wait(120).to({alpha:0},15).to({_off:true},1).wait(260));

	// sublogo
	this.instance_10 = new lib.logotext();
	this.instance_10.setTransform(229.9,579.9,0.75,0.75,0,0,0,0,0.1);
	this.instance_10.alpha = 0;
	this.instance_10._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_10).wait(9).to({_off:false},0).wait(245).to({regX:-0.1,regY:-0.1,scaleX:1.3188,scaleY:1.3188,x:152.7,y:334.9,alpha:1},15,cjs.Ease.quadInOut).wait(40).to({alpha:0},15,cjs.Ease.quadInOut).wait(96));

	// Logo
	this.instance_11 = new lib.logo();
	this.instance_11.setTransform(270,568.8,1.25,1.25,0,0,0,34.3,13);
	this.instance_11.alpha = 0;
	this.instance_11._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_11).wait(9).to({_off:false},0).to({alpha:1},15).wait(230).to({regX:34,regY:12.9,scaleX:2.2519,scaleY:2.2519,x:225.55,y:317},15,cjs.Ease.quadInOut).wait(40).to({scaleX:2.2518,scaleY:2.2518},0).to({alpha:0},15,cjs.Ease.quadInOut).wait(96));

	// Black
	this.instance_12 = new lib.color_black();
	this.instance_12.setTransform(149.75,497.45,1.2385,1.2707,0,0,0,-110.2,-69.9);

	this.timeline.addTween(cjs.Tween.get(this.instance_12).wait(254).to({regX:-109.8,regY:-69.5,scaleX:1.4207,scaleY:3.6176,x:151.5,y:356.1},15,cjs.Ease.quadInOut).wait(130).to({regX:-110.1,regY:-69.9,scaleX:1.1,scaleY:1.1285,x:149.85,y:497.4},14,cjs.Ease.quadInOut).to({regX:-110.2,scaleX:1.2385,scaleY:1.2707,x:149.75,y:497.45},6,cjs.Ease.cubicInOut).wait(1));

	// whandlmin
	this.instance_13 = new lib.whandmin("synched",0,false);
	this.instance_13.setTransform(78.5,264.1,1.2726,1.2726,0,0,0,60.1,70);

	this.timeline.addTween(cjs.Tween.get(this.instance_13).to({startPosition:72},72).to({regX:60,scaleX:7.0688,scaleY:7.0688,rotation:-11,x:-665.75,y:758.55,startPosition:94},22,cjs.Ease.cubicInOut).to({x:-655.75,startPosition:159},65).to({regX:60.1,scaleX:1.2726,scaleY:1.2726,rotation:0,x:78.55,y:264.05,startPosition:179},20,cjs.Ease.cubicInOut).to({x:81.55,startPosition:214},35,cjs.Ease.cubicInOut).to({startPosition:259},45,cjs.Ease.cubicInOut).to({x:78.55,startPosition:299},40,cjs.Ease.cubicInOut).to({startPosition:339},40).to({startPosition:340},1).to({startPosition:398},58).to({x:78.5,y:264.1,startPosition:399},1).wait(21));

	// pink
	this.instance_14 = new lib.color_pink();
	this.instance_14.setTransform(345,530,4.9996,7.4992,51.9974);
	this.instance_14.compositeOperation = "multiply";

	this.timeline.addTween(cjs.Tween.get(this.instance_14).wait(420));

	// woman1
	this.instance_15 = new lib.woman1("synched",0,false);
	this.instance_15.setTransform(146.2,275.75,1.2726,1.2726,0,0,0,117.4,200);

	this.timeline.addTween(cjs.Tween.get(this.instance_15).to({startPosition:72},72).to({scaleX:7.0688,scaleY:7.0688,rotation:-11,x:-271,y:740.8,startPosition:94},22,cjs.Ease.cubicInOut).to({x:-261,startPosition:159},65).to({scaleX:1.2726,scaleY:1.2726,rotation:0,x:146.2,y:275.75,startPosition:179},20,cjs.Ease.cubicInOut).to({startPosition:339},160).to({startPosition:340},1).wait(80));

	// wh
	this.instance_16 = new lib.color_white();
	this.instance_16.setTransform(150,300,3,5.9999);

	this.timeline.addTween(cjs.Tween.get(this.instance_16).wait(420));

	// stageBackground
	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f().s("rgba(0,0,0,0)").ss(1,1,1,3,true).p("EgY/gwbMAx/AAAMAAABg3Mgx/AAAg");
	this.shape_1.setTransform(150,300);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("EgY/AwcMAAAhg3MAx/AAAMAAABg3g");
	this.shape_2.setTransform(150,300);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1}]}).wait(420));

	this._renderFirstFrame();

}).prototype = p = new lib.AnMovieClip();
p.nominalBounds = new cjs.Rectangle(-1004.1,-645.9,1798.5,3272.6);
// library properties:
lib.properties = {
	id: '5AE02FC9E23D7748848E69BB1A16368B',
	width: 300,
	height: 600,
	fps: 25,
	color: "#FFFFFF",
	opacity: 1.00,
	manifest: [
		{src:"300x600_atlas_P_1.png", id:"300x600_atlas_P_1"},
		{src:"300x600_atlas_NP_1.jpg", id:"300x600_atlas_NP_1"}
	],
	preloads: []
};



// bootstrap callback support:

(lib.Stage = function(canvas) {
	createjs.Stage.call(this, canvas);
}).prototype = p = new createjs.Stage();

p.setAutoPlay = function(autoPlay) {
	this.tickEnabled = autoPlay;
}
p.play = function() { this.tickEnabled = true; this.getChildAt(0).gotoAndPlay(this.getTimelinePosition()) }
p.stop = function(ms) { if(ms) this.seek(ms); this.tickEnabled = false; }
p.seek = function(ms) { this.tickEnabled = true; this.getChildAt(0).gotoAndStop(lib.properties.fps * ms / 1000); }
p.getDuration = function() { return this.getChildAt(0).totalFrames / lib.properties.fps * 1000; }

p.getTimelinePosition = function() { return this.getChildAt(0).currentFrame / lib.properties.fps * 1000; }

an.bootcompsLoaded = an.bootcompsLoaded || [];
if(!an.bootstrapListeners) {
	an.bootstrapListeners=[];
}

an.bootstrapCallback=function(fnCallback) {
	an.bootstrapListeners.push(fnCallback);
	if(an.bootcompsLoaded.length > 0) {
		for(var i=0; i<an.bootcompsLoaded.length; ++i) {
			fnCallback(an.bootcompsLoaded[i]);
		}
	}
};

an.compositions = an.compositions || {};
an.compositions['5AE02FC9E23D7748848E69BB1A16368B'] = {
	getStage: function() { return exportRoot.stage; },
	getLibrary: function() { return lib; },
	getSpriteSheet: function() { return ss; },
	getImages: function() { return img; }
};

an.compositionLoaded = function(id) {
	an.bootcompsLoaded.push(id);
	for(var j=0; j<an.bootstrapListeners.length; j++) {
		an.bootstrapListeners[j](id);
	}
}

an.getComposition = function(id) {
	return an.compositions[id];
}


an.makeResponsive = function(isResp, respDim, isScale, scaleType, domContainers) {		
	var lastW, lastH, lastS=1;		
	window.addEventListener('resize', resizeCanvas);		
	resizeCanvas();		
	function resizeCanvas() {			
		var w = lib.properties.width, h = lib.properties.height;			
		var iw = window.innerWidth, ih=window.innerHeight;			
		var pRatio = window.devicePixelRatio || 1, xRatio=iw/w, yRatio=ih/h, sRatio=1;			
		if(isResp) {                
			if((respDim=='width'&&lastW==iw) || (respDim=='height'&&lastH==ih)) {                    
				sRatio = lastS;                
			}				
			else if(!isScale) {					
				if(iw<w || ih<h)						
					sRatio = Math.min(xRatio, yRatio);				
			}				
			else if(scaleType==1) {					
				sRatio = Math.min(xRatio, yRatio);				
			}				
			else if(scaleType==2) {					
				sRatio = Math.max(xRatio, yRatio);				
			}			
		}
		domContainers[0].width = w * pRatio * sRatio;			
		domContainers[0].height = h * pRatio * sRatio;
		domContainers.forEach(function(container) {				
			container.style.width = w * sRatio + 'px';				
			container.style.height = h * sRatio + 'px';			
		});
		stage.scaleX = pRatio*sRatio;			
		stage.scaleY = pRatio*sRatio;
		lastW = iw; lastH = ih; lastS = sRatio;            
		stage.tickOnUpdate = false;            
		stage.update();            
		stage.tickOnUpdate = true;		
	}
}
an.handleSoundStreamOnTick = function(event) {
	if(!event.paused){
		var stageChild = stage.getChildAt(0);
		if(!stageChild.paused || stageChild.ignorePause){
			stageChild.syncStreamSounds();
		}
	}
}
an.handleFilterCache = function(event) {
	if(!event.paused){
		var target = event.target;
		if(target){
			if(target.filterCacheList){
				for(var index = 0; index < target.filterCacheList.length ; index++){
					var cacheInst = target.filterCacheList[index];
					if((cacheInst.startFrame <= target.currentFrame) && (target.currentFrame <= cacheInst.endFrame)){
						cacheInst.instance.cache(cacheInst.x, cacheInst.y, cacheInst.w, cacheInst.h);
					}
				}
			}
		}
	}
}


})(createjs = createjs||{}, AdobeAn = AdobeAn||{});
var createjs, AdobeAn;