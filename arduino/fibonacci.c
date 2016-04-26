//A script that returns a fibonacci sequence to a specified number of iterations
/* Write a program in C that computes and prints out the first six digits in the Fibonacci sequence. You will need to look up the definition of the Fibonacci sequence if you don't know it. The first two numbers in the sequence are 0 and 1, but your program should compute the next four digits. Turn in your C program. Your C program must compile in order for it to be tested. */
#include <stdio.h>

void fibonacci(int startingNumber, int iterations) {
  //place holder variables for fibonacci sequence
  int n, n1, n2;
  for (int i = 0; i < iterations; i++) {
    switch(i) {
      //print the first fibanocci number
      case 0:
        n = startingNumber;
        printf("%d", n);
        printf("%s", ", ");
        n1 = n;
        break;
      //print the second fibanocci number
      case 1:
        n = n1 + 1;
        printf("%d", n);
        printf("%s", ", ");
        n2 = n1;
        n1 = n;
        break;
      //print the rest of the fibanocci numbers
      default:
        n = n1 + n2;
        printf("%d", n);
        printf("%s", ", ");
        n2 = n1;
        n1 = n;
    }
  }
}

int main() {
  //call fibonacci() starting from 0 and calculating 6 numbers in the sequence
  fibonacci(0,6);
}
