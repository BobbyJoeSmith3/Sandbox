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
