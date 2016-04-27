/* CHALLENGE 5.7 - Create objects from object prototype, and modify properties and use methods. */
//Generic fence post object
var genericPost = {
  x: 0,
  y: 0,
  postNum: undefined,
  connectionsTo: undefined,
  sendRopeTo: function(connectedPost) {
    if (this.connectionsTo == undefined) {
      var postArray = [];
      postArray.push(connectedPost);
      this.connectionsTo = postArray;
    } else {
      this.connectionsTo.push(connectedPost);
    }
  }
};

// create post1 and post2
var post1 = Object.create(genericPost);
var post2 = Object.create(genericPost);

// modify the post properties
post1.x = -2;
post1.y = 4;
post1.postNum = 1;

post2.x = 5;
post2.y = 1;
post2.postNum = 2;

// connect the posts together
post1.sendRopeTo(post2);
post2.sendRopeTo(post1);

/* CHALLENGE 5.8 - Create fence posts with special properties from object prototype genericPost */

/* Three new posts :
x: 0,
y: -3,
postNum: 8,
connectionsTo: 10

x: 6,
y: 8,
postNum: 9,
connectionsTo: 10

x: -2,
y: 3,
postNum: 10,
connectionsTo: 8, 9
*/

//Post 8
var post8 = Object.create(genericPost);
  post8.x = 0;
  post8.y = -3;
  post8.postNum = 8;
  post8.lightsOn = false;

//Post 9
var post9 = Object.create(genericPost);
  post9.x = 6;
  post9.y = 8;
  post9.postNum = 9;
  post9.numBirds = 0;

//Post 10
var post10 = Object.create(genericPost);
  post10.x = -2;
  post10.y = 3;
  post10.postNum = 10;
  post10.weathervane = "N";
  post10.lightsOn = false;

//Make post connections
post8.sendRopeTo(post10);
post9.sendRopeTo(post10);
post10.sendRopeTo(post8);
post10.sendRopeTo(post9);

/* CHALLENGE 5.9 - Rebuild genericPost prototype into a constructor function */
/* Original Post:
var genericPost = {
  x: 0,
  y: 0,
  postNum: undefined,
  connectionsTo: undefined,
  sendRopeTo: function(connectedPost) {
    if (this.connectionsTo == undefined) {
      var postArray = [];
      postArray.push(connectedPost);
      this.connectionsTo = postArray;
    } else {
      this.connectionsTo.push(connectedPost);
    }
  }
};
*/

//Create Fencepost function with parameters x, y, postNum
function Fencepost (x, y, postNum) {
  this.x = x;
  this.y = y;
  this.postNum = postNum;
  this.connectionsTo = [];
  this.sendRopeTo = function (connectedPost) {
    connectedPost.push(connectionsTo);
  };
}

/* CHALLENGE 5.10 - Construct some objects with new Fencepost constructor */
//Create new fence posts
var post18 = new Fencepost(-3, 4, 18);
var post19 = new Fencepost(5, -1, 19);
var post20 = new Fencepost(-2, 10, 20);

//Connect fence posts based on the following criteria:
//  1. If two posts both have even-numbered y coordinates, they should be connected.
//  2. If two posts both have odd-numbered x coordinates, they should be connected.
post18.sendRopeTo(post20);
post20.sendRopeTo(post18);
post18.sendRopeTo(post19);
post19.sendRopeTo(post18);


/* CHALLENGE 5.11 - Optimize constructor function for memory by putting repeated properties and methods in a prototype */
/* Original
function Fencepost(x, y, postNum) {
  this.x = x;
  this.y = y;
  this.postNum = postNum;
  this.connectionsTo = [];
  this.sendRopeTo = function(connectedPost) {
    this.connectionsTo.push(connectedPost);
  };
  this.removeRope = function(removeTo) {
    var temp = [];
    for (var i = 0; i < this.connectionsTo.length; i++) {
      if (this.connectionsTo[i].postNum != removeTo) {
        temp.push(this.connectionsTo[i]);
      }
    }
    this.connectionsTo = temp;
  };
  this.movePost = function(x, y) {
    this.x = x;
    this.y = y;
  };
}
*/

function Fencepost(x, y, postNum) {
  this.x = x;
  this.y = y;
  this.postNum = postNum;
  this.connectionsTo = [];
}

//Fencepost prototype
Fencepost.prototype = {
  sendRopeTo: function (connectedPost) {
    this.connectionsTo.push(connectedPost);
  },

  removeRope: function (removeTo) {
    var temp = [];
    for (var i = 0; i < this.connectionsTo.length; i++) {
      if (this.connectionsTo[i].postNum != removeTo) {
        temp.push(this.connectionsTo[i]);
      }
    }

    this.connectionsTo = temp;
  },

  movePost: function (x, y) {
    this.x = x;
    this.y = y;
  }
};
