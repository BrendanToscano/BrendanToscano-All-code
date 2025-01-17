/* .h file that takes the functions from the .c file so they can be used in other
 programs by using #include "myMath.h"
 */
// Include guards
#ifndef MYMATH_H
#define MYMATH_H

int add(int num1, int num2);
int subtract(int num1, int num2);
int multiply(int num1, int num2);
double divide(int num1, int num2);

// End of include guards
#endif
