/* CHALLENGE 1 - MINIMUM: Write a function min that takes two arguments and returns their minimum */
function min(a, b) {
  if (a == b) {
    return a;
  } else if (a < b) {
    return a;
  } else {
    return b;
  }
}

/* CHALLENGE 2 - RECURSION: Define a recursive function isEven corresponding to the following description...
  - Zero is even.
  - One is odd.
  - For any other number N, it's evenness is the same as N-2.
... The funciton should accept a number parameter and return a boolean. */
function isEven(n) {
  if (n > 1) {
    return isEven(n - 2);
  } else if (n === 1) {
    return false;
  } else if (n === 0) {
    return true;
  } else {
    return null;
  }
}

/* CHALLENGE 3 - BEAN COUNTING: Write a funciton countBs that takes a string as its only argument and returns a number that indicates how many uppercase "B" characters are in the string.

Next, write a function called countChar that behances like countBs, except it takes a second argument that indicates the character thatis to be counted. */

function countBs(phrase) {
  var numBs = 0;
  for (var i = 0; i < phrase.length; i++) {
    if (phrase.charAt(i) === "B") {
      numBs++;
    }
  }

  return numBs;
}

function countChar(phrase, char) {
  var numChar = 0;
  for (var i = 0; i < phrase.length; i++) {
    if (phrase.charAt(i) === char) {
      numChar++;
    }
  }

  return numChar;
}

//Refactor countBs to use countChar
function countBs(phrase) {
  return countChar(phrase, "B");
}
