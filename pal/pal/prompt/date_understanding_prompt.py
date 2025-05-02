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


DATE_UNDERSTANDING_PROMPT_DIRECT = '''
"""
# Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
"""

A:
01/06/2015


"""
# Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
"""

A:
01/07/2019

"""
# Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?
"""

A:
05/23/1943

"""
# Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?
"""

A:
04/20/1969

"""
# Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?
"""

A:
03/13/2002

"""
# Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
"""

A:
02/27/2017

"""
# Q: %s
"""
'''.strip() + '\n'


# ------------------------------------------Python-------------------------------------------


DATE_UNDERSTANDING_PROMPT_PYTHON = '''
"""
# Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
"""

# If 2015 is coming in 36 hours, then today is 36 hours before.
today = datetime(2015, 1, 1) - relativedelta(hours=36)
# One week from today,
one_week_from_today = today + relativedelta(weeks=1)
# The answer formatted with %%m/%%d/%%Y is
answer = one_week_from_today.strftime('%%m/%%d/%%Y')
print(answer)

"""
# Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
"""

# If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.
today = datetime(2019, 1, 1) + relativedelta(days=6)
# The answer formatted with %%m/%%d/%%Y is
answer = today.strftime('%%m/%%d/%%Y')
print(answer)

"""
# Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?
"""

# If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.
today = datetime(1943, 6, 1) + relativedelta(days=1)
# 10 days ago,
ten_days_ago = today - relativedelta(days=10)
# The answer formatted with %%m/%%d/%%Y is
answer = ten_days_ago.strftime('%%m/%%d/%%Y')
print(answer)

"""
# Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?
"""

# It is 4/19/1969 today.
today = datetime(1969, 4, 19)
# 24 hours later,
later = today + relativedelta(hours=24)
# The answer formatted with %%m/%%d/%%Y is
answer = later.strftime('%%m/%%d/%%Y')
print(answer)

"""
# Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?
"""

# If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/12/2002.
today = datetime(2002, 3, 12)
# 24 hours later,
later = today + relativedelta(hours=24)
# The answer formatted with %%m/%%d/%%Y is
answer = later.strftime('%%m/%%d/%%Y')
print(answer)

"""
# Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
"""

# If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.
today = datetime(2001, 2, 28) + relativedelta(years=16)
# Yesterday,
yesterday = today - relativedelta(days=1)
# The answer formatted with %%m/%%d/%%Y is
answer = yesterday.strftime('%%m/%%d/%%Y')
print(answer)

"""
# Q: %s
"""
'''.strip() + '\n'


# ------------------------------------------Java-------------------------------------------


DATE_UNDERSTANDING_PROMPT_JAVA = '''
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


// # Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

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
'''.strip() + '\n'


DATE_UNDERSTANDING_PROMPTS = {'Direct': DATE_UNDERSTANDING_PROMPT_DIRECT, 'Python': DATE_UNDERSTANDING_PROMPT_PYTHON, 'Java': DATE_UNDERSTANDING_PROMPT_JAVA}