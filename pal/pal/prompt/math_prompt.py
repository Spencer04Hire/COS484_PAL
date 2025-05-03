# Copyright 2022 PAL Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ------------------------------------------Direct-------------------------------------------


MATH_PROMPT_DIRECT = """
# Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A:
8


# Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
A:
33


Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
A:
29


Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

A:
9


Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

A:
8


Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

A:
39


Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

A:
5


Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

A:
6


# Q: %s
""".strip() + '\n'


# ------------------------------------------Python-------------------------------------------


MATH_PROMPT_PYTHON = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

# solution in Python:

"""Olivia has $23. She bought five bagels for $3 each. How much money does she have left?"""
money_initial = 23
bagels = 5
bagel_cost = 3
money_spent = bagels * bagel_cost
money_left = money_initial - money_spent
result = money_left
print(result)





Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

# solution in Python:

"""Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?"""
golf_balls_initial = 58
golf_balls_lost_tuesday = 23
golf_balls_lost_wednesday = 2
golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday
result = golf_balls_left
print(result)





Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

# solution in Python:

"""There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"""
computers_initial = 9
computers_per_day = 5
num_days = 4  # 4 days between monday and thursday
computers_added = computers_per_day * num_days
computers_total = computers_initial + computers_added
result = computers_total
print(result)





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

# solution in Python:

"""Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"""
toys_initial = 5
mom_toys = 2
dad_toys = 2
total_received = mom_toys + dad_toys
total_toys = toys_initial + total_received
result = total_toys
print(result)





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

# solution in Python:

"""Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
jason_lollipops_initial = 20
jason_lollipops_after = 12
denny_lollipops = jason_lollipops_initial - jason_lollipops_after
result = denny_lollipops
print(result)





Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

# solution in Python:

"""Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?"""
leah_chocolates = 32
sister_chocolates = 42
total_chocolates = leah_chocolates + sister_chocolates
chocolates_eaten = 35
chocolates_left = total_chocolates - chocolates_eaten
result = chocolates_left
print(result)





Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

# solution in Python:

"""If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?"""
cars_initial = 3
cars_arrived = 2
total_cars = cars_initial + cars_arrived
result = total_cars
print(result)





Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

# solution in Python:

"""There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?"""
trees_initial = 15
trees_after = 21
trees_added = trees_after - trees_initial
result = trees_added
print(result)
 




Q: %s

# solution in Python:
'''.strip() + '\n\n\n'


# ------------------------------------------Java-------------------------------------------


MATH_PROMPT_JAVA = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

// solution in Java:


public class Solution {
    public static int solution() {
        // Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
        int moneyInitial = 23;
		int bagels = 5;
		int bagelCost = 3;
		int moneySpent = bagels * bagelCost;
        int moneyLeft = moneyInitial - moneySpent;
        int result = moneyLeft;
        
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}





Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

// solution in Java:


public class Solution {
    public static int solution() {
        // Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
        int golfBallsInitial = 58;
		int golfBallsLostTuesday = 23;
		int golfBallsLostWednesday = 2;
		int golfBallsLeft = golfBallsInitial - golfBallsLostTuesday - golfBallsLostWednesday;
        int result = golfBallsLeft;
        
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}




Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

// solution in Java:


public class Solution {
    public static int solution() {
        // Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
        int computersInitial = 9;
		int computerPerDay = 5;
        int numDays = 4;
        int computersAdded = computerPerDay * numDays;
        int computersTotal = computersInitial + computersAdded;
        int result = computersTotal;
        
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

// solution in Java:


public class Solution {
    public static int solution() {
        // Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
        int toysInitial = 5;
		int momToys = 2;
        int dadToys = 2;
        int totalReceived = momToys + dadToys;
        int totalToys = toysInitial + totalReceived;
        int result = totalToys;
        
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

# solution in Java:


public class Solution {
    public static int solution() {
        // Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
        int jasonLollipopsInitial = 20;
        int jasonLollipopsAfter = 12;
        int dennyLollipops = jasonLollipopsInitial - jasonLollipopsAfter;
        int result = dennyLollipops;
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}



Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

# solution in Java:


public class Solution {
    public static int solution() {
        // Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
        int leahChocolates = 32;
        int sisterChocolates = 42;
        int totalChocolates = leahChocolates + sisterChocolates;
        int chocolatesEaten = 35;
        int chocolatesLeft = totalChocolates - chocolatesEaten;
        int result = chocolatesLeft;
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}




Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

# solution in Java:


public class Solution {
    public static int solution() {
        // Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
        int carsInitial = 3;
		int carsArrived = 2;
        int totalCars = carsInitial + carsArrived;
		int result = totalCars;
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}




Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

# solution in Java:


public class Solution {
    public static int solution() {
        // Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
        int treesInitial = 15;
		int treesAfter = 21;
        int treesAdded = treesAfter - treesInitial;
		int result = treesAdded;
        return result;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


Q: %s

# solution in Java:
'''.strip() + '\n\n\n'


# ------------------------------------------C++-------------------------------------------


MATH_PROMPT_CPP = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

// solution in C++:

int main() {
    // Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
    int money_initial = 23
    int bagels = 5;
    int bagel_cost = 3;
    int money_spent = bagels * bagel_cost;
    int money_left = money_initial - money_spent;

    int result = money_left;

    std::cout << result;

    return 0;
}


Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

// solution in C++:

int main() {
    // Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
    int golf_balls_initial = 58;
    int golf_balls_lost_tuesday = 23;
    int golf_balls_lost_wednesday = 2;
    int golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday;

    int result = golf_balls_left;

    std::cout << result;

    return 0;
}





Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

// solution in C++:

int main() {
    // There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
    int computers_initial = 9;
    int computers_per_day = 5;
    int num_days = 4;
    int computers_added = computers_per_day * num_days;
    int computers_total = computers_initial + computers_added;

    int result = computers_total;

    std::cout << result;

    return 0;
}





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

// solution in C++:

int main() {
    // Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
    int toys_initial = 5;
    int mom_toys = 2;
    int dad_toys = 2;
    int total_received = mom_toys + dad_toys;
    int total_toys = toys_initial + total_received;

    int result = total_toys;

    std::cout << result;

    return 0;
}





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

// solution in C++:

int main() {
    // Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
    int jason_lollipops_initial = 20;
    int jason_lollipops_after = 12;
    int denny_lollipops = jason_lollipops_initial - jason_lollipops_after;

    int result = denny_lollipops;

    std::cout << result;

    return 0;
}





Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

// solution in C++:

int main() {
    // Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
    int leah_chocolates = 32;
    int sister_chocolates = 42;
    int total_chocolates = leah_chocolates + sister_chocolates;

    int chocolates_eaten = 35;
    int chocolates_left = total_chocolates - chocolates_eaten;

    int result = chocolates_left;

    std::cout << result;

    return 0;
}





Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

// solution in C++:

int main() {
    // If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
    int cars_initial = 3;
    int cars_arrived = 2;
    int total_cars = cars_initial + cars_arrived;

    int result = total_cars;

    std::cout << result;

    return 0;
}





Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

// solution in C++:

int main() {
    // There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
    int trees_initial = 15;
    int trees_after = 21;
    int trees_added = trees_after - trees_initial;

    int result = trees_added;

    std::cout << result;

    return 0;
}





Q: %s

// solution in C++:
'''.strip() + '\n\n\n'


# ------------------------------------------OCaml-------------------------------------------

MATH_PROMPT_OCAML = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

(* solution in OCaml: *)

(* Olivia has $23. She bought five bagels for $3 each. How much money does she have left? *)
let money_initial = 23 in
let bagels = 5 in
let bagel_cost = 3 in
let money_spent = bagels * bagel_cost in
let money_left = money_initial - money_spent in
let result = money_left in
print_int result




Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

(* solution in OCaml: *)

(* Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday? *)
let golf_balls_initial = 58 in
let golf_balls_lost_tuesday = 23 in
let golf_balls_lost_wednesday = 2 in
let golf_balls_left = golf_balls_initial - golf_balls_lost_tuesday - golf_balls_lost_wednesday in
let result = golf_balls_left in
print_int result





Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

(* solution in OCaml: *)

(* There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room? *)
let computers_initial = 9 in
let computers_per_day = 5 in
(* 4 days between monday and thursday *)
let num_days = 4 in  
let computers_added = computers_per_day * num_days in
let computers_total = computers_initial + computers_added in
let result = computers_total in
print_int result





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

(* solution in OCaml: *)

(* Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now? *)
let toys_initial = 5 in
let mom_toys = 2 in
let dad_toys = 2 in
let total_received = mom_toys + dad_toys in
let total_toys = toys_initial + total_received in
let result = total_toys in
print_int result





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

(* solution in OCaml: *)

(* Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny? *)
let jason_lollipops_initial = 20 in
let jason_lollipops_after = 12 in
let denny_lollipops = jason_lollipops_initial - jason_lollipops_after in
let result = denny_lollipops in
print_int result




Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

(* solution in OCaml: *)

(* Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total? *)
let leah_chocolates = 32 in
let sister_chocolates = 42 in
let total_chocolates = leah_chocolates + sister_chocolates in
let chocolates_eaten = 35 in
let chocolates_left = total_chocolates - chocolates_eaten in
let result = chocolates_left in
print_int result




Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

(* solution in OCaml: *)

(* If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot? *)
let cars_initial = 3 in
let cars_arrived = 2 in
let total_cars = cars_initial + cars_arrived in
let result = total_cars in
print_int result





Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

(* solution in OCaml: *)

(* There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today? *)
let trees_initial = 15 in
let trees_after = 21 in
let trees_added = trees_after - trees_initial in
let result = trees_added in
print_int result
 




Q: %s

(* solution in OCaml: *)
'''.strip() + '\n\n\n'


MATH_PROMPTS = {"Direct": MATH_PROMPT_DIRECT, "Python": MATH_PROMPT_PYTHON,
				"Java": MATH_PROMPT_JAVA, "Cpp": MATH_PROMPT_CPP,
				"Ocaml": MATH_PROMPT_OCAML}