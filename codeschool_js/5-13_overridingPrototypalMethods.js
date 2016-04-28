/* CHALLENGE 5.13 - Override the valueOf() method using Fencepost prototype to return the exact distance that a post is from the ranch */
//Distance forumla: square root of [ (x1 - x2)^2 + (y1 - y2)^2 ]
Fencepost.prototype.valueOf = function (x1, y1, x2, y2) {
  return Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
};
