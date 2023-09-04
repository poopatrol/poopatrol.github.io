noStroke();

var eyeSize = 40;
var x = 200;
var y = 200;

// face
fill(255, 255, 0);
ellipse(x, y, 300, 300);

// eyes
fill(46, 46, 41);
ellipse(x - 50, y - 50, eyeSize, eyeSize);
ellipse(x + 100, y - 60, eyeSize, eyeSize);

// mouth
fill(252, 65, 65);
ellipse(x + 50, y + 40, 150, 150);
