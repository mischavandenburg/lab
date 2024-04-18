// See https://aka.ms/new-console-template for more information

/* Here are the FizzBuzz rules that you need to implement in your code project: */
/**/
/* Output values from 1 to 100, one number per line, inside the code block of an iteration statement. */
/* When the current value is divisible by 3, print the term Fizz next to the number. */
/* When the current value is divisible by 5, print the term Buzz next to the number. */
/* When the current value is divisible by both 3 and 5, print the term FizzBuzz next to the number. */

for (int i = 1; i <= 100; i++)
{
  if (i % 3 == 0)
  {
    Console.WriteLine(i + " Fizz");
  }
  else if (i % 5 == 0)
  {
    Console.WriteLine(i + " Buzz");
  }
  else if (i % 5 == 0 && i % 3 == 0)
  {
    Console.WriteLine(i + " FizzBuzz");
  }
  else
  {
    Console.WriteLine(i);
  }
}
