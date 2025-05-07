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


COLOR_OBJECT_PROMPT_DIRECT = (
    """
Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?

A:
blue


Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball?

A:
brown


Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item?

A:
0


Q: %s
""".strip()
    + "\n"
)


# ------------------------------------------COT-------------------------------------------


COLOR_OBJECT_PROMPT_COT = (
    """
Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?

Reasoning:
The sentence lists the items in this order:

1. Red pencil
2. Purple mug
3. Burgundy keychain
4. Fuchsia teddy bear
5. Black plate
6. Blue stress ball

The stress ball is blue.

A:
blue


Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball?

Reasoning:
The sentence gives the objects in this order:

1. Purple paperclip
2. Pink stress ball
3. Brown keychain
4. Green scrunchiephone charger
5. Mauve fidget spinner
6. Burgundy pen

From the list, the pink stress ball is item number 2.
The object immediately after item 2 is item 3: brown keychain.
The brown keychain is the object directly to the right of the stress ball, so the color of the object is brown.

A:
brown


Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item?

Reasoning:

The items are arranged in the following order:

1. Teal plate
2. Burgundy keychain
3. Yellow scrunchiephone charger
4. Orange mug
5. Pink notebook
6. Grey cup

The teal plate is the first item in the row.
There are no items to the left of the teal plate.

A:
0


Q: %s
""".strip()
    + "\n"
)


# ------------------------------------------Python-------------------------------------------


COLOR_OBJECT_PROMPT_PYTHON = (
    """
# Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?
# Put objects into a dictionary for quick look up
objects = {{}}
objects['pencil'] = 'red'
objects['mug'] = 'purple'
objects['keychain'] = 'burgundy'
objects['teddy bear'] = 'fuchsia'
objects['plate'] = 'black'
objects['stress ball'] = 'blue'

# Look up the color of stress ball
stress_ball_color = objects['stress ball']
answer = stress_ball_color
print(answer)


# Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball?
# Put objects into a list to record ordering
objects = []
objects += [('paperclip', 'purple')] * 1
objects += [('stress ball', 'pink')] * 1
objects += [('keychain', 'brown')] * 1
objects += [('scrunchiephone charger', 'green')] * 1
objects += [('fidget spinner', 'mauve')] * 1
objects += [('pen', 'burgundy')] * 1

# Find the index of the stress ball
stress_ball_idx = None
for i, object in enumerate(objects):
    if object[0] == 'stress ball':
        stress_ball_idx = i
        break

# Find the directly right object
direct_right = objects[i+1]

# Check the directly right object's color
direct_right_color = direct_right[1]
answer = direct_right_color
print(answer)


# Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item?
# Put objects into a list to record ordering
objects = []
objects += [('plate', 'teal')] * 1
objects += [('keychain', 'burgundy')] * 1
objects += [('scrunchiephone charger', 'yellow')] * 1
objects += [('mug', 'orange')] * 1
objects += [('notebook', 'pink')] * 1
objects += [('cup', 'grey')] * 1

# Find the index of the teal item
teal_idx = None
for i, object in enumerate(objects):
    if object[1] == 'teal':
        teal_idx = i
        break

# Find non-orange items to the left of the teal item
non_orange = [object for object in objects[:i] if object[1] != 'orange']

# Count number of non-orange objects
num_non_orange = len(non_orange)
answer = num_non_orange
print(answer)


# Q: %s
""".strip()
    + "\n"
)


# ------------------------------------------Java-------------------------------------------


COLOR_OBJECT_PROMPT_JAVA = (
    """
// Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?

public class Solution {
    public static String solution() {
        // Put objects into a dictionary for quick look up
        HashMap<String, String> objects = new HashMap<>();
        objects.put("pencil", "red");
        objects.put("mug", "purple");
        objects.put("keychain", "burgundy");
        objects.put("teddy bear", "fuchsia");
        objects.put("plate", "black");
        objects.put("stress ball", "blue");

        // Look up the color of stress ball
        String stressBallColor = objects.get("stress ball");
        String answer = stressBallColor;
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball?

public class Solution {
    public static String solution() {
        // Put objects into a list to record ordering
        ArrayList<String[]> objects = new ArrayList<>();
        for (int i = 0; i < 1; i++) objects.add(new String[]{"paperclip", "purple"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"stress ball", "pink"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"keychain", "brown"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"scrunchiephone charger", "green"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"fidget spinner", "mauve"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"pen", "burgundy"});

        // Find the index of the stress ball
        int stressBallIndex = -1;
        for (int i = 0; i < objects.size(); i++) {
            String[] object = objects.get(i);
            if (object[0].equals("stress ball")) {
                stressBallIndex = i;
                break;
            }
        }

        // Find the directly right object
        String[] directRight = objects.get(stressBallIndex + 1);

        // Get the directly right object's color
        String directRightColor = directRight[1];
        String answer = directRightColor;
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item?

public class Solution {
    public static int solution() {
        // Put objects into a list to record ordering
        ArrayList<String[]> objects = new ArrayList<>();
        for (int i = 0; i < 1; i++) objects.add(new String[]{"plate", "teal"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"keychain", "burgundy"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"scrunchiephone charger", "yellow"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"mug", "orange"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"notebook", "pink"});
        for (int i = 0; i < 1; i++) objects.add(new String[]{"cup", "grey"});

        // Find the index of the teal item
        int tealIndex = -1;

        for (int i = 0; i < objects.size(); i++) {
            String[] object = objects.get(i);
            if (object[1].equals("teal")) {
                tealIndex = i;
                break;
            }
        }

        // Count number of non-orange objects to the left of the teal item
        int numNonOrange = 0;
        for (int i = 0; i < tealIndex; i++) {
            String[] object = objects.get(i);
            if (!object[1].equals("orange")) {
                numNonOrange++;
            }
        }
        int answer = numNonOrange;
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: %s
""".strip()
    + "\n"
)


# ------------------------------------------C++-------------------------------------------


COLOR_OBJECT_PROMPT_CPP = (
    """
// Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball?
int main() {

    // Put objects into a dictionary for quick look up
    std::map<std::string, std::string> objects;
    objects["pencil"] = "red";
    objects["mug"] = "purple";
    objects["keychain"] = "burgundy";
    objects["teddy bear"] = "fuchsia";
    objects["plate"] = "black";
    objects["stress ball"] = "blue";
    
    // Look up the color of stress ball
    std::string stress_ball_color = objects["stress ball"];
    std::string answer = stress_ball_color;
    
    std::cout << answer;
        
    return 0;
}


// Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball?
int main() {

    // Put objects into a list to record ordering
    std::vector<std::tuple<std::string, std::string>> objects;
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("paperclip", "purple"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("stress ball", "pink"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("keychain", "brown"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("scrunchiephone charger", "green"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("fidget spinner", "mauve"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("pen", "burgundy"));
    
    // Find the index of the stress ball
    int stress_ball_idx = -1;
    for (int i = 0; i < objects.size(); i++) {
        if (std::get<0>(objects[i]) == "stress ball") {
            stress_ball_idx = i;
            break;
        }
    }

    // Find the directly right object
    std::tuple<std::string, std::string> direct_right = objects[stress_ball_idx + 1];
    
    // Check the directly right object's color
    std::string direct_right_color = std::get<1>(direct_right);
    std::string answer = direct_right_color;
    
    std::cout << answer;
    return 0;
}


// Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item?
int main() {

    // Put objects into a list to record ordering
    std::vector<std::tuple<std::string, std::string>> objects;
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("plate", "teal"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("keychain", "burgundy"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("scrunchiephone charger", "yellow"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("mug", "orange"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("notebook", "pink"));
    for (int i = 0; i < 1; i++) objects.push_back(std::make_tuple("cup", "grey"));

    // Find the index of the teal item
    int teal_idx = -1;
    for (int i = 0; i < objects.size(); i++) {
        if (std::get<1>(objects[i]) == "teal") {
            teal_idx = i;
            break;
        }
    }

    // Find non-orange items to the left of the teal item
    std::vector<std::tuple<std::string, std::string>> non_orange;
    for (int i = 0; i < teal_idx; i++) {
        if (std::get<1>(objects[i]) != "orange") {
            non_orange.push_back(objects[i]);
        }
    }
    
    // Count number of non-orange objects
    int num_non_orange = non_orange.size();
    int answer = num_non_orange;
    
    std::cout << answer;
    return 0;
}


// Q: %s
""".strip()
    + "\n"
)


# ------------------------------------------OCaml-------------------------------------------


COLOR_OBJECT_PROMPT_OCAML = (
    """
(* Q: On the nightstand, there is a red pencil, a purple mug, a burgundy keychain, a fuchsia teddy bear, a black plate, and a blue stress ball. What color is the stress ball? *)

(* solution using OCaml: *)

(* Put objects into a dictionary for quick look up *)
let objects = Hashtbl.create 6 in
Hashtbl.add objects "pencil" "red";
Hashtbl.add objects "mug" "purple";
Hashtbl.add objects "keychain" "burgundy";
Hashtbl.add objects "teddy bear" "fuchsia";
Hashtbl.add objects "plate" "black";
Hashtbl.add objects "stress ball" "blue";
let stress_ball_color = Hashtbl.find objects "stress ball" in
print_string stress_ball_color



(* Q: On the table, you see a bunch of objects arranged in a row: a purple paperclip, a pink stress ball, a brown keychain, a green scrunchiephone charger, a mauve fidget spinner, and a burgundy pen. What is the color of the object directly to the right of the stress ball? *)

(* solution using OCaml: *)

(* Put objects into a list to record ordering *)
let objects = [
  ("purple", "paperclip");
  ("pink", "stress ball");
  ("brown", "keychain");
  ("green", "scrunchiephone charger");
  ("mauve", "fidget spinner");
  ("burgundy", "pen")
] in
let find_color_right_of target =
  let rec aux = function
    | [] | [_] -> ""
    | (_, obj) :: (color, _) :: _ when obj = target -> color
    | _ :: rest -> aux rest
  in
  aux objects
in
let result = find_color_right_of "stress ball" in
print_string result


(* Q: On the nightstand, you see the following items arranged in a row: a teal plate, a burgundy keychain, a yellow scrunchiephone charger, an orange mug, a pink notebook, and a grey cup. How many non-orange items do you see to the left of the teal item? *)

(* solution using OCaml: *)

(* Put objects into a list to record ordering *)
let objects = [
  ("teal", "plate"); 
  ("burgundy", "keychain"); 
  ("yellow", "scrunchiephone charger"); 
  ("orange", "mug"); 
  ("pink", "notebook"); 
  ("grey", "cup")
] in
(* Find non-orange items to the left of the teal item *)
let count_non_orange_before target_color lst =
  let rec aux count = function
    | [] -> 0
    | (color, _) :: _ when color = target_color -> count
    | (color, _) :: rest ->
        let new_count = if color <> "orange" then count + 1 else count in
        aux new_count rest
  in
  aux 0 lst
in
let result = count_non_orange_before "teal" objects in
print_int result


(* Q: %s *)
""".strip()
    + "\n"
)


COLOR_OBJECT_PROMPTS = {
    "Direct": COLOR_OBJECT_PROMPT_DIRECT,
    "COT": COLOR_OBJECT_PROMPT_COT,
    "Python": COLOR_OBJECT_PROMPT_PYTHON,
    "Java": COLOR_OBJECT_PROMPT_JAVA,
    "Cpp": COLOR_OBJECT_PROMPT_CPP,
    "Ocaml": COLOR_OBJECT_PROMPT_OCAML,
}
