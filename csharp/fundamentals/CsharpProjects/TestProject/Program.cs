Random dice = new Random();
int roll = dice.Next(1, 7);
Console.WriteLine(roll);

dice.Next();

int firstValue = 500;
int secondValue = 600;
int largerValue = Math.Max(firstValue, secondValue);

Console.WriteLine($"The larger value is {largerValue}");

string[] numbers = {
"B123",
"C234",
"A345",
"C15",
"B177",
"G3003",
"C235",
"B179",
};


foreach (var i in numbers)
{
  if (i.StartsWith("B"))
  {
    Console.WriteLine(i);
  }
}
