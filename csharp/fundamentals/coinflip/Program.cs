// Throw a coin with a 50% chance

Random coin = new Random();
int throwCoin = coin.Next(0, 100);
Console.WriteLine(throwCoin >= 50 ? "head" : "tails");



