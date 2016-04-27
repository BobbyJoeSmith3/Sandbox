/* Cattle objects */
var canyonCows = [
  { name: "Bessie", type: "cow", hadCalf: "Burt" },
  { name: "Donald", type: "bull", hadCalf: null },
  { name: "Esther", type: "calf", hadCalf: null },
  { name: "Burt", type: "calf", hadCalf: null },
  { name: "Sarah", type: "cow", hadCalf: "Esther" },
  { name: "Samson", type: "bull", hadCalf: null },
  { name: "Delilah", type: "cow", hadCalf: null }
];

var valleyCows = [
  { name: "Danielle", type: "cow", hadCalf: null },
  { name: "Brittany", type: "cow", hadCalf: "Christina" },
  { name: "Jordan", type: "bull", hadCalf: null },
  { name: "Trevor", type: "bull", hadCalf: null },
  { name: "Christina", type: "calf", hadCalf: null },
  { name: "Lucas", type: "bull", hadCalf: null }
];

var forestCows = [
  { name: "Legolas", type: "calf", hadCalf: null },
  { name: "Gimli", type: "bull", hadCalf: null },
  { name: "Arwen", type: "cow", hadCalf: null },
  { name: "Galadriel", type: "cow", hadCalf: null },
  { name: "Eowyn", type: "cow", hadCalf: "Legolas" }
];

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

//alert the sum of calfs from canyonCows, bulls from valleyCows, and cows from forestCows
alert(canyonCows.countCattle("calf") + valleyCows.countCattle("bull") + forestCows.countCattle("cow"));

/* CHALLENGE 5.4 - Add two functions to the Object prototype: noCalvesYet and countForBreeding */
Object.prototype.noCalvesYet = function () {
  /*if the object type is a "cow" and also had no calves, return true */
  if ((this.type == "cow") && (this.hadCalf == null)) {
    return true;
  } else {
    return false;
  }
};

Object.prototype.countForBreeding = function () {
  var numToBreed = 0;

  //Loop through array
  for (var i = 0; i < this.length; i++) {
    //If noCalvesYet returns true for current array item, increment numToBreed
    if (this[i].noCalvesYet()) {
      numToBreed++;
    }
  }

  return numToBreed;
};

/* CHALLENGE 5.5 - Use functions to determine how many cows have not had calves yet */

var numPriorityCows = canyonCows.countForBreeding() +
                      valleyCows.countForBreeding() + forestCows.countForBreeding() + badlandsCows.countForBreeding();

//Alert message with number of cows of top breeding priority
alert("Herd-merger has indicated " + numPriorityCows + " cows of top breeding priority.");
