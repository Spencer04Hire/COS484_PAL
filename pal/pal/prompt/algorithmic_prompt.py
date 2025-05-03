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


REPEAT_COPY_PROMPT_DIRECT = '''
Q: say java twice and data once, and then repeat all of this three times.

A:
java java data java java data java java data



Q: ask a group of insects in what family? four times. after the fourth time say The happy family

A:
a group of insects in what family? a group of insects in what family? a group of insects in what family? a group of insects in what family? The happy family



Q: Repeat the word duck four times, but halfway through also say quack

A:
duck duck quack duck duck


Q: Print boolean eleven times, but after the 3rd and 8th also say correct

A:
boolean boolean boolean correct boolean boolean boolean boolean boolean correct boolean boolean boolean


Q: %s

A:
'''.strip() + '\n\n'


# ------------------------------------------Python-------------------------------------------


REPEAT_COPY_PROMPT_PYTHON = '''
Q: say java twice and data once, and then repeat all of this three times.

# solution using Python:

"""Q: say java twice and data once, and then repeat all of this three times."""
result = []
tmp = ["java", "java", "data"]
for i in range(3):
    result.extend(tmp)
print(" ".join(result))



Q: ask a group of insects in what family? four times. after the fourth time say The happy family

# solution using Python:

 """Q: ask a group of insects in what family? four times. after the fourth time say The happy family"""
result = []
tmp = []
for i in range(1, 5):
    tmp.append("a group of insects in what family?")
tmp.append("The happy family")
result.extend(tmp)
print(" ".join(result))



Q: Repeat the word duck four times, but halfway through also say quack

# solution using Python:


"""Q: Repeat the word duck four times, but halfway through also say quack"""
result = []
for i in range(1, 5):
    result.append("duck")
    if i == 2:
        result.append("quack")
print(" ".join(result))



Q: Print boolean eleven times, but after the 3rd and 8th also say correct

# solution using Python:

"""Q: Print boolean eleven times, but after the 3rd and 8th also say correct"""
result = []
for i in range(1, 12):
    result.append("boolean")
    if i == 3 or i == 8:
        result.append("correct")
print(" ".join(result))



Q: %s

# solution using Python:
'''.strip() + '\n\n'


# ------------------------------------------Java-------------------------------------------


REPEAT_COPY_PROMPT_JAVA = '''
Q: say java twice and data once, and then repeat all of this three times.

// solution using Java:

public class Solution {
    public static String solution() {
        // Q: say java twice and data once, and then repeat all of this three times.
        ArrayList<String> result = new ArrayList<>();
        String[] temp = new String[]{"java", "java", "data"};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < temp.length; j++) {
                result.add(temp[j]);
            }
        }

        String answer = String.join(" ", result);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


Q: ask a group of insects in what family? four times. after the fourth time say The happy family

// solution using Java:

public class Solution {
    public static String solution() {
        // Q: ask a group of insects in what family? four times. after the fourth time say The happy family
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            result.add("a group of insects in what family?");
        }
        result.add("The happy family");

        String answer = String.join(" ", result);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


Q: Repeat the word duck four times, but halfway through also say quack

// solution using Java:

public class Solution {
    public static String solution() {
        // Q: Repeat the word duck four times, but halfway through also say quack
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            result.add("duck");
            if (i == 1) {
                result.add("quack");
            }
        }

        String answer = String.join(" ", result);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


Q: Print boolean eleven times, but after the 3rd and 8th also say correct

// solution using Java:

public class Solution {
    public static String solution() {
        // Q: Print boolean eleven times, but after the 3rd and 8th also say correct
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < 11; i++) {
            result.add("boolean");
            if (i == 2 || i == 7) {
                result.add("correct");
            }
        }

        String answer = String.join(" ", result);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}



Q: %s

// solution using Java:
'''.strip() + '\n\n'


# ------------------------------------------C++-------------------------------------------


REPEAT_COPY_PROMPT_CPP = '''
Q: say java twice and data once, and then repeat all of this three times.

// solution using C++:

int main() {
    // Q: say java twice and data once, and then repeat all of this three times.
    std::vector<std::string> result;
    std::vector<std::string> temp = {"java", "java", "data"};
    
    for (int i = 0; i < 3; i++) {
        for (const auto& word : temp) {
            result.push_back(word);
        }
    }
    
    for (size_t i = 0; i < result.size(); i++) {
        std::cout << result[i];
        if (i < result.size() - 1) {
            std::cout << " ";
        }
    }

    return 0;
}



Q: ask a group of insects in what family? four times. after the fourth time say The happy family

// solution using C++:

int main() {
    // Q: ask a group of insects in what family? four times. after the fourth time say The happy family
    std::vector<std::string> result;
    
    for (int i = 0; i < 5; i++) {
        result.push_back("a group of insects in what family?");
    }

    result.push_back("The happy family");
    
    for (size_t i = 0; i < result.size(); i++) {
        std::cout << result[i];
        if (i < result.size() - 1) {
            std::cout << " ";
        }
    }

    return 0;
}



Q: Repeat the word duck four times, but halfway through also say quack

// solution using C++:

int main() {
    // Q: Repeat the word duck four times, but halfway through also say quack
    std::vector<std::string> result;
    
    for (int i = 0; i < 4; i++) {
        result.push_back("duck");
        if (i == 1) {
            result.push_back("quack");
        }
    }

    for (size_t i = 0; i < result.size(); i++) {
        std::cout << result[i];
        if (i < result.size() - 1) {
            std::cout << " ";
        }
    }

    return 0;
}



Q: Print boolean eleven times, but after the 3rd and 8th also say correct

// solution using C++:

int main() {
    // Q: Print boolean eleven times, but after the 3rd and 8th also say correct
    std::vector<std::string> result;
    
    for (int i = 0; i < 11; i++) {
        result.push_back("boolean");
        if (i == 2 || i == 7) {
            result.push_back("correct");
        }
    }

    for (size_t i = 0; i < result.size(); i++) {
        std::cout << result[i];
        if (i < result.size() - 1) {
            std::cout << " ";
        }
    }

    return 0;
}



Q: %s

// solution using C++:
'''.strip() + '\n\n'


# ------------------------------------------OCaml-------------------------------------------


REPEAT_COPY_PROMPT_OCAML = '''
Q: say java twice and data once, and then repeat all of this three times.

(* solution using OCaml: *)

(* Q: say java twice and data once, and then repeat all of this three times. *)
let tmp = ["java"; "java"; "data"] in
let result = Buffer.create 100 in
for _ = 1 to 3 do
  List.iter (fun s -> Buffer.add_string result s; Buffer.add_string result " ") tmp;
done;
print_string (Buffer.contents result)


Q: ask a group of insects in what family? four times. after the fourth time say The happy family

(* solution using OCaml: *)

(* Q: ask a group of insects in what family? four times. after the fourth time say The happy family *)
let result = Buffer.create 100 in
for _ = 1 to 4 do
  Buffer.add_string result "a group of insects in what family? "
done;
Buffer.add_string result "The happy family";
print_string (Buffer.contents result)


Q: Repeat the word duck four times, but halfway through also say quack

(* solution using OCaml: *)

(* Q: Repeat the word duck four times, but halfway through also say quack *)
let result = Buffer.create 100 in
for i = 1 to 4 do
  Buffer.add_string result "duck ";
  if i = 2 then Buffer.add_string result "quack ";
done;
print_string (Buffer.contents result)



Q: Print boolean eleven times, but after the 3rd and 8th also say correct

(* solution using OCaml: *)

(* Q: Print boolean eleven times, but after the 3rd and 8th also say correct *)
let result = Buffer.create 100 in
for i = 1 to 11 do
  Buffer.add_string result "boolean ";
  if i = 3 || i = 8 then Buffer.add_string result "correct "
done;
print_string (Buffer.contents result)



Q: %s
(* solution using OCaml: *)
'''.strip() + '\n\n'


REPEAT_COPY_PROMPTS = {'Direct': REPEAT_COPY_PROMPT_DIRECT, 'Python': REPEAT_COPY_PROMPT_PYTHON,
					   'Java': REPEAT_COPY_PROMPT_JAVA, "Cpp": REPEAT_COPY_PROMPT_CPP,
                       "Ocaml": REPEAT_COPY_PROMPT_OCAML }

# ------------------------------------------Direct-------------------------------------------

OBJECT_COUNTING_PROMPT_DIRECT = '''
Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?

A:
11


Q: I have a chair, two ovens, and three tables. How many objects do I have?

A:
6



Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?

A:
7



Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?

A:
12
    


Q: %s

A:
'''.strip() + '\n\n'


# ------------------------------------------Python-------------------------------------------


OBJECT_COUNTING_PROMPT_PYTHON = '''
Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?

# solution using Python:

"""Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?"""
musical_instruments_to_count = {{
    'drum': 1,
    'flute': 1,
    'clarinet': 1,
    'violin': 1,
    'accordion': 4,
    'piano': 1,
    'trombone': 1,
    'trumpet': 1
}
num_musical_instruments = sum(musical_instruments_to_count.values())
print(num_instruments)



Q: I have a chair, two ovens, and three tables. How many objects do I have?

# solution using Python:

"""Q: I have a chair, two ovens, and three tables. How many objects do I have?"""
objects_to_count = {
    'chair': 1,
    'oven': 2,
    'table': 3
}
num_objects = sum(objects_to_count.values())
print(num_objects)



Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?

# solution using Python:

"""Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?"""
# note: I'm not counting the chair, tables, or fridges as vegetables
vegetables_to_count = {
    'potato': 2,
    'cauliflower': 1,
    'lettuce head': 1,
    'cabbage': 1,
    'onion': 2
}
num_vegetables = sum(vegetables_to_count.values())
print(num_vegetables)



Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?

# solution using Python:

"""Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?"""
# note: I'm not counting the raspberry as an animal
animals_to_count = {
    'cat': 1,
    'rabbit': 1,
    'mouse': 1,
    'pig': 1,
    'snail': 2,
    'fish': 1,
    'cow': 2,
    'snake': 1,
    'goat': 1,
    'duck': 1
}
num_animals = sum(animals_to_count.values())
print(num_animals)
    


Q: %s

# solution using Python:
'''.strip() + '\n\n'


# ------------------------------------------Java-------------------------------------------

OBJECT_COUNTING_PROMPT_JAVA = '''
Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?

// solution using Java:

public class Solution {
    public static int solution() {
        // Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?
        HashMap<String, Integer> musicalInstrumentsToCount = new HashMap<>();
        musicalInstrumentsToCount.put("drum", 1);
        musicalInstrumentsToCount.put("flute", 1);
        musicalInstrumentsToCount.put("clarinet", 1);
        musicalInstrumentsToCount.put("violin", 1);
        musicalInstrumentsToCount.put("accordion", 4);
        musicalInstrumentsToCount.put("piano", 1);
        musicalInstrumentsToCount.put("trombone", 1);
        musicalInstrumentsToCount.put("trumpet", 1);

        int numMusicalInstruments = 0;
        for (int count : musicalInstrumentsToCount.values()) {
            numMusicalInstruments += count;
        }

        return numMusicalInstruments;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}



Q: I have a chair, two ovens, and three tables. How many objects do I have?

// solution using Java:

public class Solution {
    public static int solution() {
        // Q: I have a chair, two ovens, and three tables. How many objects do I have?
        HashMap<String, Integer> objectsToCount = new HashMap<>();
        objectsToCount.put("chair", 1);
        objectsToCount.put("oven", 2);
        objectsToCount.put("table", 3);

        int numObjects = 0;
        for (int count : objectsToCount.values()) {
            numObjects += count;
        }

        return numObjects;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}



Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?

// solution using Java:

public class Solution {
    public static int solution() {
        // Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?
        // note: I'm not counting the chair, tables, or fridges as vegetables
        HashMap<String, Integer> vegetablesToCount = new HashMap<>();
        vegetablesToCount.put("chair", 1);
        vegetablesToCount.put("oven", 2);
        vegetablesToCount.put("table", 3);

        int numVegetables = 0;
        for (int count : vegetablesToCount.values()) {
            numVegetables += count;
        }

        return numVegetables;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}



Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?

// solution using Java:

public class Solution {
    public static int solution() {
        // Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?
        // note: I'm not counting the raspberry as an animal
        HashMap<String, Integer> animalsToCount = new HashMap<>();
        animalsToCount.put("cat", 1);
        animalsToCount.put("rabbit", 1);
        animalsToCount.put("mouse", 1);
        animalsToCount.put("pig", 1);
        animalsToCount.put("snail", 2);
        animalsToCount.put("fish", 1);
        animalsToCount.put("cow", 2);
        animalsToCount.put("snake", 1);
        animalsToCount.put("goat", 1);
        animalsToCount.put("duck", 1);

        int numAnimals = 0;
        for (int count : animalsToCount.values()) {
            numAnimals += count;
        }

        return numAnimals;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}



Q: %s

# solution using Java:
'''.strip() + '\n\n'

# ------------------------------------------C++-------------------------------------------


OBJECT_COUNTING_PROMPT_CPP = '''
Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?

// solution using C++:

int main() {
    // Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?
    std::map<std::string, int> musical_instruments_to_count = {
        {"drum", 1},
        {"flute", 1},
        {"clarinet", 1},
        {"violin", 1},
        {"accordion", 4},
        {"piano", 1},
        {"trombone", 1},
        {"trumpet", 1}
    };
    
    int num_musical_instruments = 0;
    for (const auto& pair : musical_instruments_to_count) {
        num_musical_instruments += pair.second;
    }
    
    std::cout << num_musical_instruments;
    
    return 0;
}



Q: I have a chair, two ovens, and three tables. How many objects do I have?

// solution using C++:

int main() {
    // Q: I have a chair, two ovens, and three tables. How many objects do I have?
    std::map<std::string, int> objects_to_count = {
        {"chair", 1},
        {"oven", 2},
        {"table", 3},
    };
    
    int num_objects = 0;
    for (const auto& pair : objects_to_count) {
        num_objects += pair.second;
    }
    
    std::cout << num_objects;
    
    return 0;
}



Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?

// solution using C++:

int main() {
    // Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?
    // note: I'm not counting the chair, tables, or fridges as vegetables
    std::map<std::string, int> vegetables_to_count = {
        {"potato", 2},
        {"cauliflower", 1},
        {"lettuce head", 1},
        {"cabbage", 1},
        {"onion", 2},
    };
    
    int num_vegetables = 0;
    for (const auto& pair : vegetables_to_count) {
        num_vegetables += pair.second;
    }
    
    std::cout << num_vegetables;
    
    return 0;
}



Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?

// solution using C++:

int main() {
    // Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?
    // note: I'm not counting the raspberry as an animal
    std::map<std::string, int> animals_to_count = {
        {"cat", 1},
        {"rabbit", 1},
        {"mouse", 1},
        {"pig", 1},
        {"snail", 2},
        {"fish", 1},
        {"cow", 2},
        {"snake", 1},
        {"goat", 1},
        {"duck", 1},
    };
    
    int num_animals = 0;
    for (const auto& pair : animals_to_count) {
        num_animals += pair.second;
    }
    
    std::cout << num_animals;
    
    return 0;
}
    


Q: %s

// solution using C++:
'''.strip() + '\n\n'


# ------------------------------------------OCaml-------------------------------------------

OBJECT_COUNTING_PROMPT_OCAML = '''
Q: I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have?

(* solution using OCaml: *)

(* I have a drum, a flute, a clarinet, a violin, four accordions, a piano, a trombone, and a trumpet. How many musical instruments do I have? *)
let instruments = Hashtbl.create 8 in
Hashtbl.add instruments "drum" 1;
Hashtbl.add instruments "flute" 1;
Hashtbl.add instruments "clarinet" 1;
Hashtbl.add instruments "violin" 1;
Hashtbl.add instruments "accordion" 4;
Hashtbl.add instruments "piano" 1;
Hashtbl.add instruments "trombone" 1;
Hashtbl.add instruments "trumpet" 1;
let num_instruments = Hashtbl.fold (fun _ count total -> total + count) instruments 0 in
print_int num_instruments



Q: I have a chair, two ovens, and three tables. How many objects do I have?

(* solution using OCaml: *)

(* Q: I have a chair, two ovens, and three tables. How many objects do I have? *)
let objects = Hashtbl.create 3 in
Hashtbl.add objects "chair" 1;
Hashtbl.add objects "oven" 2;
Hashtbl.add objects "table" 3;
let num_objects = Hashtbl.fold (fun _ count total -> total + count) objects 0 in
print_int num_objects



Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have?

(* solution using OCaml: *)

(* Q: I have a chair, two potatoes, a cauliflower, a lettuce head, two tables, a cabbage, two onions, and three fridges. How many vegetables do I have? *)
(* note: I'm not counting the chair, tables, or fridges as vegetables *)
let vegetables = Hashtbl.create 5 in
Hashtbl.add vegetables "potato" 2;
Hashtbl.add vegetables "cauliflower" 1;
Hashtbl.add vegetables "lettuce head" 1;
Hashtbl.add vegetables "cabbage" 1;
Hashtbl.add vegetables "onion" 2;
let num_vegetables = Hashtbl.fold (fun _ count total -> total + count) vegetables 0 in
print_int num_vegetables



Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have?

(* solution using OCaml: *)

(* Q: I have a raspberry, a cat, a rabbit, a mouse, a pig, two snails, a fish, two cows, a snake, a goat, and a duck. How many animals do I have? *)
(* note: I'm not counting the raspberry as an animal *)
let animals = Hashtbl.create 10 in
Hashtbl.add animals "cat" 1;
Hashtbl.add animals "rabbit" 1;
Hashtbl.add animals "mouse" 1;
Hashtbl.add animals "pig" 1;
Hashtbl.add animals "snail" 2;
Hashtbl.add animals "fish" 1;
Hashtbl.add animals "cow" 2;
Hashtbl.add animals "snake" 1;
Hashtbl.add animals "goat" 1;
Hashtbl.add animals "duck" 1;
let num_animals = Hashtbl.fold (fun _ count total -> total + count) animals 0 in
print_int num_animals



Q: %s

(* solution using OCaml: *)
'''.strip() + '\n\n'


OBJECT_COUNTING_PROMPTS = {"Direct": OBJECT_COUNTING_PROMPT_DIRECT, "Python": OBJECT_COUNTING_PROMPT_PYTHON,
						   "Java": OBJECT_COUNTING_PROMPT_JAVA, "Cpp": OBJECT_COUNTING_PROMPT_CPP,
						   "Ocaml": OBJECT_COUNTING_PROMPT_OCAML}
