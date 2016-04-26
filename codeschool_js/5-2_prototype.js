/* Create a function for the array prototype that counts number of cattle based on type in an array of cattle objects */

Array.prototype.countCattle = function (kind) {
  //keeps track of number of bulls, cows, and calves
  var numKind = 0;
  for (var i = 0; i < this.length; i++) {
    if (this[i].type == kind) {
      numKind++;
    }
  }

  return numKind;
};

/*alert the sum of calfs from canyonCows, bulls from valleyCows, and cows from forestCows */
alert(canyonCows.countCattle("calf") + valleyCows.countCattle("bull") + forestCows.countCattle("cow"));
