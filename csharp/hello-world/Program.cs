Console.WriteLine("Hello, World!");


string firstFriend = " Maria  ";
string secondFriend = "Scott  ";

firstFriend = firstFriend.TrimStart();

Console.WriteLine($"My friends are {firstFriend.TrimEnd()} and {secondFriend.TrimEnd()}");
string friends= $"My friends are {firstFriend.TrimEnd()} and {secondFriend.TrimEnd()}";

Console.WriteLine(friends.Replace("Scott", "John"));

