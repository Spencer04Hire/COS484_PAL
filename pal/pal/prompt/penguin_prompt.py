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


PENGUIN_PROMPT_DIRECT = (
    """
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm. 
We now add a penguin to the table:
James, 12, 90, 12
How many penguins are less than 8 years old?

A:
2


Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
Which is the youngest penguin?

A:
Bernard


Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
What is the name of the second penguin sorted by alphabetic order?

A:
Gwen


Q: %s

A:
""".strip()
    + "\n"
)


# ------------------------------------------COT-------------------------------------------


PENGUIN_PROMPT_COT = (
    """

Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm. 
We now add a penguin to the table:
James, 12, 90, 12
How many penguins are less than 8 years old?

Reasoning:
We examine the age of each penguin:

Louis is 7 years old, which is less than 8.

Bernard is 5 years old, which is less than 8.

Vincent is 9 years old, which is not less than 8.

Gwen is 8 years old, which is not less than 8.

James is 12 years old, which is not less than 8.

Only Louis and Bernard are under 8 years old.

Therefore, the number of penguins less than 8 years old is 2.

A:
2


Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
Which is the youngest penguin?

Reasoning:
We are given the ages of the penguins:

Louis: 7 years

Bernard: 5 years

Vincent: 9 years

Gwen: 8 years

The youngest penguin is the one with the smallest age.
Bernard is 5 years old, which is the youngest among them.

A:
Bernard


Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
What is the name of the second penguin sorted by alphabetic order?

Reasoning:
We need to sort the penguin names in alphabetical order and find the second one in that list.

The names are:

Louis
Bernard
Vincent
Gwen

Alphabetically, they are sorted as:

Bernard
Gwen
Louis
Vincent

A:
Gwen


Q: %s

Reasoning:
""".strip()
    + "\n"
)


# ------------------------------------------Python-------------------------------------------


PENGUIN_PROMPT_PYTHON = (
    '''
"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm. 
We now add a penguin to the table:
James, 12, 90, 12
How many penguins are less than 8 years old?
"""

# Put the penguins into a list.
penguins = []
penguins.append(('Louis', 7, 50, 11))
penguins.append(('Bernard', 5, 80, 13))
penguins.append(('Vincent', 9, 60, 11))
penguins.append(('Gwen', 8, 70, 15))
# Add penguin James.
penguins.append(('James', 12, 90, 12))
# Find penguins under 8 years old.
penguins_under_8_years_old = [penguin for penguin in penguins if penguin[1] < 8]
# Count number of perguins under 8.
num_penguin_under_8 = len(penguins_under_8_years_old)
answer = num_penguin_under_8
print(answer)


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
Which is the youngest penguin?
"""

# Put the penguins into a list.
penguins = []
penguins.append(('Louis', 7, 50, 11))
penguins.append(('Bernard', 5, 80, 13))
penguins.append(('Vincent', 9, 60, 11))
penguins.append(('Gwen', 8, 70, 15))
# Sort the penguins by age.
penguins = sorted(penguins, key=lambda x: x[1])
# Get the youngest penguin's name.
youngest_penguin_name = penguins[0][0]
answer = youngest_penguin_name
print(answer)


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
What is the name of the second penguin sorted by alphabetic order?
"""

# Put the penguins into a list.
penguins = []
penguins.append(('Louis', 7, 50, 11))
penguins.append(('Bernard', 5, 80, 13))
penguins.append(('Vincent', 9, 60, 11))
penguins.append(('Gwen', 8, 70, 15))
# Sort penguins by alphabetic order.
penguins_alphabetic = sorted(penguins, key=lambda x: x[0])
# Get the second penguin sorted by alphabetic order.
second_penguin_name = penguins_alphabetic[1][0]
answer = second_penguin_name
print(answer)


"""
Q: %s
"""
'''.strip()
    + "\n"
)


# ------------------------------------------Java-------------------------------------------


PENGUIN_PROMPT_JAVA = (
    '''
"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm. 
We now add a penguin to the table:
James, 12, 90, 12
How many penguins are less than 8 years old?
"""

public class Solution {
    public static int solution() {
        // Put the penguins into a list.
        ArrayList<String[]> penguins = new ArrayList<>();
        penguins.add(new String[]{"Louis", "7", "50", "11"});
        penguins.add(new String[]{"Bernard", "5", "80", "13"});
        penguins.add(new String[]{"Vincent", "9", "60", "11"});
        penguins.add(new String[]{"Gwen", "8", "70", "15"});

        // Add penguin James.
        penguins.add(new String[]{"James", "12", "90", "12"});
        
        // Find penguins under 8 years old.
        ArrayList<String[]> penguinsUnder8YearsOld = new ArrayList<>();
        for (String[] penguin : penguins) {
            if (Integer.parseInt(penguin[1]) < 8) {
                penguinsUnder8YearsOld.add(penguin);
            }
        }

        // Count number of perguins under 8.
        int numPenguinsUnder8 = penguinsUnder8YearsOld.length;
        int answer = numPenguinsUnder8;
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
Which is the youngest penguin?
"""

public class Solution {
    public static String solution() {
        // Put the penguins into a list.
        ArrayList<String[]> penguins = new ArrayList<>();
        penguins.add(new String[]{"Louis", "7", "50", "11"});
        penguins.add(new String[]{"Bernard", "5", "80", "13"});
        penguins.add(new String[]{"Vincent", "9", "60", "11"});
        penguins.add(new String[]{"Gwen", "8", "70", "15"});

        // Sort the penguins by age.
        penguins.sort(Comparator.comparing(x -> x[1]));

        // Get the youngest penguin's name.
        String youngestPenguinName = penguins.get(0)[0];
        String answer = youngestPenguinName;
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
What is the name of the second penguin sorted by alphabetic order?
"""

public class Solution {
    public static String solution() {
        // Put the penguins into a list.
        ArrayList<String[]> penguins = new ArrayList<>();
        penguins.add(new String[]{"Louis", "7", "50", "11"});
        penguins.add(new String[]{"Bernard", "5", "80", "13"});
        penguins.add(new String[]{"Vincent", "9", "60", "11"});
        penguins.add(new String[]{"Gwen", "8", "70", "15"});

        // Sort penguins by alphabetic order.
        penguins.sort(Comparator.comparing(p -> p[0]));
        // Get the second penguin sorted by alphabetic order.
        String secondPenguinName = penguins.get(1)[0];
        String answer = secondPenguinName;
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


"""
Q: %s
"""
'''.strip()
    + "\n"
)


# ------------------------------------------C++-------------------------------------------


PENGUIN_PROMPT_CPP = (
    '''
"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm. 
We now add a penguin to the table:
James, 12, 90, 12
How many penguins are less than 8 years old?
"""

int main() {
   // Put the penguins into a list
   std::vector<std::tuple<std::string, int, int, int>> penguins;
   penguins.push_back(std::make_tuple("Louis", 7, 50, 11));
   penguins.push_back(std::make_tuple("Bernard", 5, 80, 13));
   penguins.push_back(std::make_tuple("Vincent", 9, 60, 11));
   penguins.push_back(std::make_tuple("Gwen", 8, 70, 15));

   // Add penguin James
   penguins.push_back(std::make_tuple("James", 12, 90, 12));
   
   // Find penguins under 8 years old
   std::vector<std::tuple<std::string, int, int, int>> penguins_under_8_years_old;
   for (const auto& penguin : penguins) {
       if (std::get<1>(penguin) < 8) {
           penguins_under_8_years_old.push_back(penguin);
       }
   }
   
   // Count number of penguins under 8
   int num_penguin_under_8 = penguins_under_8_years_old.size();
   int answer = num_penguin_under_8;
   
   std::cout << answer;
   
   return 0;
}


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
Which is the youngest penguin?
"""

int main() {
    // Put the penguins into a list
    std::vector<std::tuple<std::string, int, int, int>> penguins;
    penguins.push_back(std::make_tuple("Louis", 7, 50, 11));
    penguins.push_back(std::make_tuple("Bernard", 5, 80, 13));
    penguins.push_back(std::make_tuple("Vincent", 9, 60, 11));
    penguins.push_back(std::make_tuple("Gwen", 8, 70, 15));
    
    // Sort the penguins by age.
    std::sort(penguins.begin(), penguins.end(),
    [] (const auto& a, const auto& b) {
        return std::get<1>(a) < std::get<1>(b);
    });
   
    // Get the youngest penguin's name.
    std::string youngest_penguin_name = std::get<0>(penguins[0]);
    std::string answer = youngest_penguin_name;
    
    std::cout << answer;
    
    return 0;
}


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
What is the name of the second penguin sorted by alphabetic order?
"""

int main() {
    // Put the penguins into a list
    std::vector<std::tuple<std::string, int, int, int>> penguins;
    penguins.push_back(std::make_tuple("Louis", 7, 50, 11));
    penguins.push_back(std::make_tuple("Bernard", 5, 80, 13));
    penguins.push_back(std::make_tuple("Vincent", 9, 60, 11));
    penguins.push_back(std::make_tuple("Gwen", 8, 70, 15));
    
    // Sort penguins by alphabetic order
    std::vector<std::tuple<std::string, int, int, int>> penguins_alphabetic = penguins;
    std::sort(penguins_alphabetic.begin(), penguins_alphabetic.end(), 
        [](const auto& a, const auto& b) {
            return std::get<0>(a) < std::get<0>(b);
       });
   
    // Get the second penguin sorted by alphabetic order
    std::string second_penguin_name = std::get<0>(penguins_alphabetic[1]);
    std::string answer = second_penguin_name;
    
    std::cout << answer;
    
    return 0;
}

"""
Q: %s
"""
'''.strip()
    + "\n"
)


# ------------------------------------------OCaml-------------------------------------------

PENGUIN_PROMPT_OCAML = (
    '''
"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm. 
We now add a penguin to the table:
James, 12, 90, 12
How many penguins are less than 8 years old?
"""

(* Put the penguins into a list. *)
let penguins = [
    ("Louis", 7, 50, 11);
    ("Bernard", 5, 80, 13);
    ("Vincent", 9, 60, 11);
    ("Gwen", 8, 70, 15);
] in
(* Add penguin James. *)
let penguins = ("James", 12, 90, 12) :: penguins in
(* Count number of perguins under 8. *)
let check_under_eight count (_,age,_,_) = if age < 8 then count + 1 else count in
let count_under_eight = List.fold_left check_under_eight 0 penguins in
print_int count_under_eight


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
Which is the youngest penguin?
"""

(* Put the penguins into a list. *)
let penguins = [
    ("Louis", 7, 50, 11);
    ("Bernard", 5, 80, 13);
    ("Vincent", 9, 60, 11);
    ("Gwen", 8, 70, 15);
] in
(* Find youngest penguin. *)
let check_if_younger youngest penguin = 
    let (_,age1,_,_) = youngest in
    let (_,age2,_,_) = penguin in
    if age2 < age1 then penguin else youngest
in
let youngest_penguin = List.fold_left check_if_younger (List.hd penguins) penguins in
(* Get the youngest penguin's name. *)
let (name,_,_,_) = youngest_penguin in
print_string name


"""
Q: Here is a table where the first line is a header and each subsequent line is a penguin:
name, age, height (cm), weight (kg) 
Louis, 7, 50, 11
Bernard, 5, 80, 13
Vincent, 9, 60, 11
Gwen, 8, 70, 15
For example: the age of Louis is 7, the weight of Gwen is 15 kg, the height of Bernard is 80 cm.
What is the name of the second penguin sorted by alphabetic order?
"""

(* Put the penguins into a list. *)
let penguins = [
    ("Louis", 7, 50, 11);
    ("Bernard", 5, 80, 13);
    ("Vincent", 9, 60, 11);
    ("Gwen", 8, 70, 15);
] in
(* Sort penguins by alphabetic order. *)
let compare_name penguin1 penguin2 =
    let (name1,_,_,_) = penguin1 in
    let (name2,_,_,_) = penguin2 in
    String.compare name1 name2
in
let sorted_by_name = List.sort compare_name penguins in
(* Get the second penguin sorted by alphabetic order. *)
let second_penguin = List.nth sorted_by_name 1 in
let (name, _, _, _) = second_penguin in
print_string name


"""
Q: %s
"""
'''.strip()
    + "\n"
)


PENGUIN_PROMPTS = {
    "Direct": PENGUIN_PROMPT_DIRECT,
    "COT": PENGUIN_PROMPT_COT,
    "Python": PENGUIN_PROMPT_PYTHON,
    "Java": PENGUIN_PROMPT_JAVA,
    "Cpp": PENGUIN_PROMPT_CPP,
    "Ocaml": PENGUIN_PROMPT_OCAML,
}
