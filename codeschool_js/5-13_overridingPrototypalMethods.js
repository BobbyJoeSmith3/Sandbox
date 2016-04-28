/* CHALLENGE 5.13 - Override the valueOf() method using Fencepost prototype to return the exact distance that a post is from the ranch */
//Distance forumla: square root of [ (x1 - x2)^2 + (y1 - y2)^2 ]
Fencepost.prototype.valueOf = function (x1, y1, x2, y2) {
  return Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
};

/* CHALLENGE 5.14 - Override toString method for Fencepost prototype */
/* String should read:
Fence post #10:
Connected to posts:
11
12
13
Distance from ranch: 5 yards
*/

//Original code
function Fencepost(x, y, postNum) {
  this.x = x;
  this.y = y;
  this.postNum = postNum;
  this.connectionsTo = [];
}

Fencepost.prototype = {
  sendRopeTo: function(connectedPost) {
    this.connectionsTo.push(connectedPost);
  },
  removeRope: function(removeTo) {
    var temp = [];
    for (var i = 0; i < this.connectionsTo.length; i++) {
      if (this.connectionsTo[i].postNum != removeTo) {
        temp.push(this.connectionsTo[i]);
      }
    }
    this.connectionsTo = temp;
  },
  movePost: function(x, y) {
    this.x = x;
    this.y = y;
  },
  valueOf: function() {
  return Math.sqrt(this.x * this.x +
                   this.y * this.y);
  }
};

//Override
Fencepost.prototype.toString = function () {
  var list = "Fence post #" + this.postNum + ":\n" + "Connected to posts:\n";

  //List array of post connections
  for (var i = 0; i < this.connectionsTo.length; i++) {
    list += this.connectionsTo[i] + "\n";
  }

  //Specify distance from ranch
  list += "Distance from ranch: " + this.valueOf() + " yards";

  //return phrase
  return list;
};
