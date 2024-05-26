#!/usr/bin/env python
# coding: utf-8

# In[5]:


import regex as re
import pandas as pd


# In[4]:


#Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
def characterreplace (text):
    
    pattern = '[ ,.]'
    
    result = re.sub(pattern,':',text)
    
    return result

example = "Hello,this. is, the ,test"
result = characterreplace(example)
print(result)


# In[22]:


#Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.)from the columns except words.

data = {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}

df = pd.DataFrame(data)


def clean_text(text):
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return clean_text

df['SUMMARY'] = df['SUMMARY'].apply(clean_text)

print(df)


# In[25]:


#Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

def findwords(text):
    pattern = re.compile(r'\b\w{4,}\b')
    longwords = pattern.findall(text)
    return longwords

test = "this is the test string"
result  = findwords(test)
print(result)


# In[27]:


#Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

def findwords(text):
    pattern = re.compile(r'\b\w{3,6}\b')
    longwords = pattern.findall(text)
    return longwords

test = "this is the test string to use even bigger wordss"
result  = findwords(test)
print(result)


# In[36]:


#Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.

def remove_parentheses(strings):
    
    pattern = re.compile(r'\s*\(.*?\)\s*')
   
    def remove_parens(text):
        return pattern.sub('', text).strip()
    
    cleaned_strings = [remove_parens(s) for s in strings]
    
    return cleaned_strings


input_list = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
result = remove_parentheses(input_list)
for i in result:
    print(i)


# In[97]:


#Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.


def remove_parenthesis_area_from_file(file_path):
    
    with open(file_path, 'r') as file:
        text = file.read()
    
    
    pattern = re.compile(r'\s*\([^)]*\)')
    
    
    cleaned_text = pattern.sub('', text)
    
    return cleaned_text


file_path = r"E:\DataScience\Internship\removeparenthesis.txt"


cleaned_text = remove_parenthesis_area_from_file(file_path)


print("Expected Output:", cleaned_text)



# In[89]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters

text = "ImportanceOfRegularExpressionsInPython"

pattern = '[A-Z][^A-Z]*'

uppercase_letters = re.findall(pattern,text)

print(uppercase_letters)


# In[49]:


#Question 8- Create a function in python to insert spaces between words starting with numbers.

def insert_spaces(text):
    pattern = re.compile(r'(?<=\D)(?=\d)')
    spaced_text = pattern.sub(' ', text)
    
    return spaced_text

text = 'RegularExpression1IsAn2ImportantTopic3InPython'
result = insert_spaces(text)
print(result)


# In[50]:


#Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.

import re

def insert_spaces(text):

    pattern = re.compile(r'(?<=[A-Z0-9])(?=[A-Z][a-z])|(?<=[a-z])(?=[0-9])')
    spaced_text = pattern.sub(' ', text)
    
    return spaced_text

text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces(text)
print(result)



# In[51]:


#Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
#Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv


import pandas as pd

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"

df = pd.read_csv(url)

df['first_five_letters'] = df['Country'].str[:6]

print(df.head())


# In[53]:


#Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

def match_string(text):
  
    pattern = re.compile(r'^[A-Za-z0-9_]+$')
    
    if pattern.match(text):
        return True
    else:
        return False


test_strings = ["Hello-World!", "Hello_World"]

for text in test_strings:
    result = match_string(text)
    print(f"'{text}' matches: {result}")


# In[55]:


def starts_with_number(text, number):
   
    pattern = re.compile(rf'^{number}\D.*')
    
    if pattern.match(text):
        return True
    else:
        return False

test_strings = ["123abc","123jkl","789mno"]

specific_number = "123"

for text in test_strings:
    result = starts_with_number(text, specific_number)
    print(f"'{text}' starts with {specific_number}: {result}")


# In[56]:


#Question 13- Write a Python program to remove leading zeros from an IP address

def remove_leading_zeros(ip_address):
    
    pattern = re.compile(r'\b0+(\d)')
    cleaned_ip = pattern.sub(r'\1', ip_address)
    return cleaned_ip

test_ips = [
    "192.168.001.001",
    "255.255.000.255",
    "010.000.123.123",
    "001.002.003.004"
]

for ip in test_ips:
    cleaned_ip = remove_leading_zeros(ip)
    print(f"Original: {ip} -> Cleaned: {cleaned_ip}")


# In[58]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.

sample_text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."


with open('sample_text.txt', 'w') as file:
    file.write(sample_text)


def extract_date(file_path):
   
    pattern = re.compile(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(st|nd|rd|th)?\s+\d{4}\b')
    
    
    with open(file_path, 'r') as file:
        text = file.read()
        
       
        match = pattern.search(text)
        
        
        if match:
            return match.group()
        else:
            return None


date_string = extract_date('sample_text.txt')
print(f"Extracted date string: {date_string}")


# In[63]:


#Question 15- Write a Python program to search some literals strings in a string. 

def search_literals(text, words):

    pattern = re.compile(r'\b(' + '|'.join(words) + r')\b')
    
    matches = pattern.findall(text)
    
    return matches


text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']


found_words = search_literals(text, searched_words)


print(f"Searched words: {searched_words}")
print(f"Found words: {found_words}")



# In[64]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs

def search_literal_with_location(text, word):
   
    pattern = re.compile(r'\b' + re.escape(word) + r'\b')
    
    
    matches = [(match.start(), match.end()) for match in pattern.finditer(text)]
    
    return matches


sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

locations = search_literal_with_location(sample_text, searched_word)


print(f"Searched word: '{searched_word}'")
print(f"Locations: {locations}")


for start, end in locations:
    found_word = sample_text[start:end]
    print(f"Found word: '{found_word}' at position: {start}-{end}")


# In[67]:


#Question 17- Write a Python program to find the substrings within a string.


def find_substrings(text, pattern):
    
    regex = re.compile(re.escape(pattern))
    
   
    matches = [(match.start(), match.end()) for match in regex.finditer(text)]
    
    return matches


sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'


locations = find_substrings(sample_text, pattern)


print(f"Searched pattern: '{pattern}'")
print(f"Locations: {locations}")



# In[66]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

def find_occurrences(text, pattern):

    regex = re.compile(re.escape(pattern))
    
    
    matches = [(match.start(), match.end()) for match in regex.finditer(text)]
    
    return matches


sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'


locations = find_occurrences(sample_text, pattern)


print(f"Searched pattern: '{pattern}'")
print(f"Occurrences and positions: {locations}")


for start, end in locations:
    found_substring = sample_text[start:end]
    print(f"Found substring: '{found_substring}' at position: {start}-{end}")


# In[68]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

def convert_date_format(date_str):
    
    pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
    
    new_date_str = pattern.sub(r'\3-\2-\1', date_str)
    
    return new_date_str

input_date = '2024-05-26'
converted_date = convert_date_format(input_date)
print(f"Original date: {input_date}")
print(f"Converted date: {converted_date}")



# In[69]:


#Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.

def find_decimal_numbers(text):
    
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    
    decimal_numbers = pattern.findall(text)
    
    return decimal_numbers

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

result = find_decimal_numbers(sample_text)

print("Decimal numbers with precision of 1 or 2:", result)


# In[70]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.

def print_numbers_with_positions(text):
    
    pattern = re.compile(r'\d+')
    
    
    for match in pattern.finditer(text):
        number = match.group()  
        start = match.start()   
        end = match.end()      
        
        
        print(f"Number: {number}, Position: {start}-{end}")


sample_text = "The price of the item is $20.50 and the quantity is 3."

print_numbers_with_positions(sample_text)


# In[72]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.

import re

def extract_maximum_numeric_value(text):
    
    pattern = re.compile(r'\b\d+\b')
    
    
    numeric_values = pattern.findall(text)
    
   
    numeric_values = [int(value) for value in numeric_values]
    
   
    max_value = max(numeric_values)
    
    return max_value


sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'


max_numeric_value = extract_maximum_numeric_value(sample_text)

print("Maximum marks:", max_numeric_value)



# In[74]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters.

def insert_spaces(text):
   
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    
    result = result.capitalize()
    return result


sample_text = "RegularExpressionIsAnImportantTopicInPython"


output_text = insert_spaces(sample_text)


print(output_text)


# In[76]:


#Question 24- Python regex to find sequences of one upper case letter followed by lower case letters
    
def find_sequences(text):
   
    sequences = re.findall(r'[A-Z][a-z]+', text)
    return sequences


sample_text = "RegularExpressionIsAnImportantTopicInPython"


result = find_sequences(sample_text)

print(result)


# In[78]:


#Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.

def remove_continuous_duplicates(sentence):
    
    cleaned_sentence = re.sub(r'\b(\w+)( \1\b)+', r'\1', sentence)
    return cleaned_sentence


sample_text = "Hello hello world world"


cleaned_text = remove_continuous_duplicates(sample_text)


print(cleaned_text)


# In[80]:


#Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

def accept_ending_with_alphanumeric(text):
    
    pattern = re.compile(r'.*[a-zA-Z0-9]$')
 
    match = pattern.match(text)
    
    return bool(match)

test_strings = ["Hello123", "xyz!",]

for test_string in test_strings:
    result = accept_ending_with_alphanumeric(test_string)
    print(f"String '{test_string}': {'Accepted' if result else 'Rejected'}")


# In[82]:


#Question 27-Write a python program using RegEx to extract the hashtags.

import re

def extract_hashtags(text):

    pattern = re.compile(r'#\w+')
    
    hashtags = pattern.findall(text)
    
    return hashtags


sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

result = extract_hashtags(sample_text)

print(result)


# In[83]:


#Question 28- Write a python program using RegEx to remove <U+..> like symbols

import re

def remove_unicode_symbols(text):
    
    pattern = re.compile(r'\<U\+[0-9A-F]{4}\>')
    
    cleaned_text = pattern.sub('', text)
    
    return cleaned_text

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

result = remove_unicode_symbols(sample_text)


print(result)


# In[94]:


#Question 29- Write a python program to extract dates from the text stored in the text file.

def extract_dates_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    
    pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')
    
    
    dates = pattern.findall(text)
    
    return dates


file_path = "E:\DataScience\Internship\dates.txt"


extracted_dates = extract_dates_from_file(file_path)

print("Extracted Dates:", extracted_dates)


# In[87]:


#Question 30- Create a function in python to remove all words from a string of length between 2 and 4.

def remove_words_of_length_2_to_4(text):
    
    pattern = re.compile(r'\b\w{2,4}\b')
    
    
    cleaned_text = pattern.sub('', text)
    
    return cleaned_text


sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."


result = remove_words_of_length_2_to_4(sample_text)


print( result)


# In[ ]:




