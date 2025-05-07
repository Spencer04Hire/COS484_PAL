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


DATE_UNDERSTANDING_PROMPT_DIRECT = (
    """
Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

A:
01/06/2015


Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

A:
01/07/2019


Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

A:
05/23/1943


Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

A:
04/20/1969


Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

A:
03/13/2002


Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

A:
02/27/2017


Q: %s
""".strip()
    + "\n"
)


# ------------------------------------------COT-------------------------------------------

# Prompts adapted from https://arxiv.org/pdf/2201.11903
DATE_UNDERSTANDING_PROMPT_COT = (
    """
Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

Reasoning:
If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today
is 12/30/2014. So one week from today will be 01/05/2015. So the answer is 01/05/2015.

A:
01/06/2015


Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

Reasoning:
If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six
days later. So today is 01/07/2019. So the answer is 01/07/2019.

A:
01/07/2019


Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

Reasoning:
One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943. 10 days before today is 05/23/1943. So the
answer is 05/23/1943.

A:
05/23/1943


Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

Reasoning:
Today is 04/19/1969. 24 hours later is one day after today, which would be 04/20/1969. So the answer is
04/20/1969.

A:
04/20/1969


Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

Reasoning:
Today is 03/12/2002. So the date 24 hours later will be 03/13/2002. So the answer is 03/13/2002

A:
03/13/2002


Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

Reasoning:
The last day of February is the 28th, so Jane was born on 02/28/2001. Today is her 16-year old birthday, so
today is 02/28/2017. So yesterday was 02/27/2017. So the answer is 02/27/2017.

A:
02/27/2017


Q: %s

Reasoning:
""".strip()
    + "\n"
)


# ------------------------------------------Python-------------------------------------------


DATE_UNDERSTANDING_PROMPT_PYTHON = (
    """
# Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

# If 2015 is coming in 36 hours, then today is 36 hours before.
today = datetime(2015, 1, 1) - relativedelta(hours=36)
# One week from today,
one_week_from_today = today + relativedelta(weeks=1)
# The answer formatted with %%m/%%d/%%Y is
answer = one_week_from_today.strftime('%%m/%%d/%%Y')
print(answer)


# Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

# If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
today = datetime(2019, 1, 1) + relativedelta(days=6)
# The answer formatted with %%m/%%d/%%Y is
answer = today.strftime('%%m/%%d/%%Y')
print(answer)


# Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?

# If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
today = datetime(1943, 6, 1) + relativedelta(days=1)
# 10 days ago,
ten_days_ago = today - relativedelta(days=10)
# The answer formatted with %%m/%%d/%%Y is
answer = ten_days_ago.strftime('%%m/%%d/%%Y')
print(answer)


# Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

# It is 4/19/1969 today.
today = datetime(1969, 4, 19)
# 24 hours later,
later = today + relativedelta(hours=24)
# The answer formatted with %%m/%%d/%%Y is
answer = later.strftime('%%m/%%d/%%Y')
print(answer)


# Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

# If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/12/2002.
today = datetime(2002, 3, 12)
# 24 hours later,
later = today + relativedelta(hours=24)
# The answer formatted with %%m/%%d/%%Y is
answer = later.strftime('%%m/%%d/%%Y')
print(answer)


# Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

# If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
today = datetime(2001, 2, 28) + relativedelta(years=16)
# Yesterday,
yesterday = today - relativedelta(days=1)
# The answer formatted with %%m/%%d/%%Y is
answer = yesterday.strftime('%%m/%%d/%%Y')
print(answer)


# Q: %s

""".strip()
    + "\n"
)


# ------------------------------------------Java-------------------------------------------


DATE_UNDERSTANDING_PROMPT_JAVA = (
    """
// Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

public class Solution {
    public static String solution() {
        // If 2015 is coming in 36 hours, then today is 36 hours before.
        LocalDateTime today = LocalDateTime.of(2015, 1, 1, 0, 0).minusHours(36);
        // Add 1 week which is 7 days
        LocalDateTime oneWeekFromToday = today.plusDays(7);
        // Format as MM/DD/YYYY
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        String answer = oneWeekFromToday.format(formatter);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

public class Solution {
    public static String solution() {
        // If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
        LocalDateTime today = LocalDateTime.of(2019, 1, 1, 0, 0).plusDays(6);
        // Format as MM/DD/YYYY
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        String answer = today.format(formatter);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?


public class Solution {
    public static String solution() {
        // If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
        LocalDateTime today = LocalDateTime.of(1943, 6, 1, 0, 0).plusDays(1);
        // 10 days ago
        LocalDateTime tenDaysAgo = today.minusDays(10);
        // Format as MM/DD/YYYY
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        String answer = tenDaysAgo.format(formatter);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?

public class Solution {
    public static String solution() {
        // It is 4/19/1969 today.
        LocalDateTime today = LocalDateTime.of(1969, 4, 19, 0, 0);
        // 24 hours later
        LocalDateTime later = today.plusHours(24);
        // Format as MM/DD/YYYY
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        String answer = later.format(formatter);
        return answer;
    }
    
    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?

public class Solution {
    public static String solution() {
        // If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/12/2002.
        LocalDateTime today = LocalDateTime.of(2002, 3, 12, 0, 0);
        // 24 hours later
        LocalDateTime later = today.plusHours(24);
        // Format as MM/DD/YYYY
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        String answer = later.format(formatter);
        return answer;
    }

    public static void main(String[] args) {
        System.out.print(solution());
    }
}


// Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?

public class Solution {
    public static String solution() {
        // If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
        LocalDateTime today = LocalDateTime.of(2001, 2, 28, 0, 0).plusYears(16);
        // Yesterday
        LocalDateTime yesterday = today.minusDays(1);
        // Format as MM/DD/YYYY
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        String answer = yesterday.format(formatter);
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


DATE_UNDERSTANDING_PROMPT_CPP = (
    """

// Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?


int main() {
    using namespace std::chrono;

    // If 2015 is coming in 36 hours, then today is 36 hours before.
    year_month_day ymd{year{2015}, month{1}, day{1}};
    sys_days base_date{ymd};
    auto today = base_date - hours{36};

    // One week from today,
    auto future_tp = today + weeks{1};

    // The answer formatted with %%m/%%d/%%Y is
    std::time_t answer = system_clock::to_time_t(future_tp);
    std::cout << std::put_time(std::gmtime(&answer), "%%m/%%d/%%Y");

    return 0;
}


// Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?


int main() {
    using namespace std::chrono;

    // If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
    year_month_day ymd{year{2019}, month{1}, day{1}};
    sys_days base_date{ymd};
    auto today = base_date + days{6};

    // The answer formatted with %%m/%%d/%%Y is
    std::time_t answer = system_clock::to_time_t(today);
    std::cout << std::put_time(std::gmtime(&answer), "%%m/%%d/%%Y");

	return 0;
}


// Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?


int main() {
    using namespace std::chrono;

    // If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
    year_month_day ymd{year{1943}, month{6}, day{1}};
    sys_days base_date{ymd};
    auto today = base_date + days{1};

    // 10 days ago,
    auto ten_days_ago = today - days{10};

    // The answer formatted with %%m/%%d/%%Y is
    std::time_t answer = system_clock::to_time_t(ten_days_ago);
    std::cout << std::put_time(std::gmtime(&answer), "%%m/%%d/%%Y");

    return 0;
}


// Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?


int main() {
    using namespace std::chrono;

    // It is 4/19/1969 today.
    year_month_day ymd{year{1969}, month{4}, day{19}};
    sys_days base_date{ymd};
    
    // 24 hours later,
    auto today = base_date + hours{24};

    // The answer formatted with %%m/%%d/%%Y is
    std::time_t answer = system_clock::to_time_t(today);
    std::cout << std::put_time(std::gmtime(&answer), "%%m/%%d/%%Y");

    return 0;
}


// Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?


int main() {
    using namespace std::chrono;

    // If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/12/2002.
    year_month_day ymd{year{2002}, month{3}, day{12}};
    sys_days today{ymd};

    // 24 hours later,
    auto later = today + hours{24};

    // The answer formatted with %%m/%%d/%%Y is
    std::time_t answer = system_clock::to_time_t(later);
    std::cout << std::put_time(std::gmtime(&answer), "%%m/%%d/%%Y");

    return 0;
}


// Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?


int main() {
    using namespace std::chrono;

    // If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
    constexpr year_month_day ymd{year{2001}, month{2}, day{28}};
    year_month_day today = ymd + years{16};

    // Yesterday,
    sys_days today_days = sys_days{today};
    sys_days yesterday = today_days - days{1};

    // The answer formatted with %%m/%%d/%%Y is
    std::time_t answer = system_clock::to_time_t(yesterday);
    std::cout << std::put_time(std::gmtime(&answer), "%%m/%%d/%%Y");

    return 0;
}


// Q: %s

""".strip()
    + "\n"
)


# ------------------------------------------OCaml-------------------------------------------

DATE_UNDERSTANDING_PROMPT_OCAML = (
    """

(* Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY? *)


open Unix;;

(* Manually create the time structure for Jan 1 2015 *)
let base_time = {
    tm_sec = 0;
    tm_min = 0;
    tm_hour = 0;
    tm_mday = 1;
    tm_mon = 0;       (* January is month 0 (0-based) *)
    tm_year = 2015 - 1900;  (* Years since 1900 *)
    tm_wday = 0;        (* Will be set correctly by mktime *)
    tm_yday = 0;        (* Will be set correctly by mktime *)
    tm_isdst = false
} in

(* Convert to timestamp *)
let timestamp_2015 = fst (Unix.mktime base_time) in

let seconds_in_an_hour = 60. *. 60. in

(* Subtract 36 hours in seconds *)
let timestamp_now = timestamp_2015 -. (36. *. seconds_in_an_hour) in

(* Add 1 week (7 days) in seconds *)
let seconds_in_a_day = seconds_in_an_hour *. 24. in
let timestamp_future = timestamp_now +. (7. *. seconds_in_a_day) in

(* Convert back to time structure *)
let future_date = Unix.localtime timestamp_future in

(* Print result in MM/DD/YYYY format *)
Printf.printf "%%02d/%%02d/%%d"
(future_date.tm_mon + 1)
future_date.tm_mday
(future_date.tm_year + 1900)



(* Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY? *)


open Unix;;

(* Manually create the time structure for Jan 1 2019 *)
let base_time = {
    tm_sec = 0;
    tm_min = 0;
    tm_hour = 0;
    tm_mday = 1;
    tm_mon = 0;       (* January is month 0 (0-based) *)
    tm_year = 2019 - 1900;  (* Years since 1900 *)
    tm_wday = 0;        (* Will be set correctly by mktime *)
    tm_yday = 0;        (* Will be set correctly by mktime *)
    tm_isdst = false
} in

(* Convert to timestamp *)
let timestamp_2019 = fst (Unix.mktime base_time) in

let seconds_in_a_day = 60. *. 60. *. 24. in
(* If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later. *)
(* Add 6 days in seconds *)
let timestamp_now = timestamp_2019 +. (6. *. seconds_in_a_day) in

(* Convert back to time structure *)
let today_date = Unix.localtime timestamp_now in

(* Print result in MM/DD/YYYY format *)
Printf.printf "%%02d/%%02d/%%d"
(today_date.tm_mon + 1)
today_date.tm_mday
(today_date.tm_year + 1900)



(* Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY? *)


open Unix;;

(* Manually create the time structure for 06/01/1943 *)
let base_time = {
    tm_sec = 0;
    tm_min = 0;
    tm_hour = 0;
    tm_mday = 1;
    tm_mon = 5;       (* June is month 5 (0-based) *)
    tm_year = 1943 - 1900;  (* Years since 1900 *)
    tm_wday = 0;        (* Will be set correctly by mktime *)
    tm_yday = 0;        (* Will be set correctly by mktime *)
    tm_isdst = false
} in

(* Convert to timestamp *)
let timestamp_concert = fst (Unix.mktime base_time) in

let seconds_in_a_day = 60. *. 60. *. 24. in
(* If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later. *)
(* Add 1 day in seconds *)
let timestamp_now = timestamp_concert +. (1. *. seconds_in_a_day) in

(* Subtract 10 days in seconds *)
let timestamp_before = timestamp_now -. (10. *. seconds_in_a_day) in


(* Convert back to time structure *)
let earlier_date = Unix.localtime timestamp_before in

(* Print result in MM/DD/YYYY format *)
Printf.printf "%%02d/%%02d/%%d"
(earlier_date.tm_mon + 1)
earlier_date.tm_mday
(earlier_date.tm_year + 1900)



(* Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY? *)


open Unix;;

(* Manually create the time structure for 4/19/1969 *)
let base_time = {
    tm_sec = 0;
    tm_min = 0;
    tm_hour = 0;
    tm_mday = 19;
    tm_mon = 3;         (* April is month 3 (0-based) *)
    tm_year = 1969 - 1900;  (* Years since 1900 *)
    tm_wday = 0;        (* Will be set correctly by mktime *)
    tm_yday = 0;        (* Will be set correctly by mktime *)
    tm_isdst = false
} in

(* Convert to timestamp *)
let timestamp_today = fst (Unix.mktime base_time) in

let seconds_in_an_hour = 60. *. 60. in

(* Add 24 hours in seconds *)
let timestamp_future = timestamp_today +. (24. *. seconds_in_an_hour) in

(* Convert back to time structure *)
let future_date = Unix.localtime timestamp_future in

(* Print result in MM/DD/YYYY format *)
Printf.printf "%%02d/%%02d/%%d"
(future_date.tm_mon + 1)
future_date.tm_mday
(future_date.tm_year + 1900)



(* Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY? *)


open Unix;;

(* Manually create the time structure for Mar 12 2022*)
let base_time = {
    tm_sec = 0;
    tm_min = 0;
    tm_hour = 0;
    tm_mday = 12;
    tm_mon = 2;         (* March is month 2 (0-based) *)
    tm_year = 2002 - 1900;  (* Years since 1900 *)
    tm_wday = 0;        (* Will be set correctly by mktime *)
    tm_yday = 0;        (* Will be set correctly by mktime *)
    tm_isdst = false
} in

(* Convert to timestamp *)
let timestamp_today = fst (Unix.mktime base_time) in

let seconds_in_an_hour = 60. *. 60. in

(* Add 24 hours in seconds *)
let timestamp_future = timestamp_today +. (24. *. seconds_in_an_hour) in

(* Convert back to time structure *)
let future_date = Unix.localtime timestamp_future in

(* Print result in MM/DD/YYYY format *)
Printf.printf "%%02d/%%02d/%%d"
(future_date.tm_mon + 1)
future_date.tm_mday
(future_date.tm_year + 1900)



(* Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY? *)


open Unix;;

(* Manually create the time structure for Feb 28 2001 + 16 years *)
let base_time = {
    tm_sec = 0;
    tm_min = 0;
    tm_hour = 0;
    tm_mday = 28;
    tm_mon = 1;         (* February is month 1 (0-based) *)
    tm_year = 2001 - 1900 + 16;  (* Years since 1900 *)
    tm_wday = 0;        (* Will be set correctly by mktime *)
    tm_yday = 0;        (* Will be set correctly by mktime *)
    tm_isdst = false
} in

(* Convert to timestamp *)
let timestamp_today = fst (Unix.mktime base_time) in

let seconds_in_a_day = 60. *. 60. *. 24. in

(* Add 24 hours in seconds *)
let timestamp_yesterday = timestamp_today -. (1. *. seconds_in_a_day) in

(* Convert back to time structure *)
let yesterday_date = Unix.localtime timestamp_yesterday in

(* Print result in MM/DD/YYYY format *)
Printf.printf "%%02d/%%02d/%%d"
(yesterday_date.tm_mon + 1)
yesterday_date.tm_mday
(yesterday_date.tm_year + 1900)



(* Q: %s *)

""".strip()
    + "\n"
)


DATE_UNDERSTANDING_PROMPTS = {
    "Direct": DATE_UNDERSTANDING_PROMPT_DIRECT,
    "COT": DATE_UNDERSTANDING_PROMPT_COT,
    "Python": DATE_UNDERSTANDING_PROMPT_PYTHON,
    "Java": DATE_UNDERSTANDING_PROMPT_JAVA,
    "Cpp": DATE_UNDERSTANDING_PROMPT_CPP,
    "Ocaml": DATE_UNDERSTANDING_PROMPT_OCAML,
}
