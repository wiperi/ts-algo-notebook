# Python String Manipulation Techniques for Algorithm Problems

# 1. Basic String Operations
def basic_operations():
    s = "algorithm"
    # Length
    length = len(s)  # 9
    
    # Indexing and Slicing
    first_char = s[0]  # 'a'
    last_char = s[-1]  # 'm'
    substring = s[1:5]  # 'lgor'
    reversed_str = s[::-1]  # 'mhtirogla'
    
    # Checking content
    contains_algo = "algo" in s  # True
    starts_with = s.startswith("alg")  # True
    ends_with = s.endswith("thm")  # True
    
    # Case conversion
    upper_case = s.upper()  # 'ALGORITHM'
    lower_case = s.lower()  # 'algorithm'
    
    # Character counting
    count_a = s.count('a')  # 1
    
    # Finding positions
    first_a = s.find('a')  # 0 (returns -1 if not found)
    last_a = s.rfind('a')  # 0
    
    # Replace
    replaced = s.replace('a', 'A')  # 'Algorithm'


# 2. String Splitting and Joining
def split_join_examples():
    # Splitting
    sentence = "leetcode is a coding platform"
    words = sentence.split()  # ['leetcode', 'is', 'a', 'coding', 'platform']
    
    csv_data = "1,2,3,4,5"
    numbers = csv_data.split(',')  # ['1', '2', '3', '4', '5']
    
    # Joining
    joined_words = ' '.join(words)  # 'leetcode is a coding platform'
    joined_nums = ','.join(['1', '2', '3'])  # '1,2,3'
    
    # Split with limit
    limited_split = sentence.split(' ', 2)  # ['leetcode', 'is', 'a coding platform']


# 3. String Checking and Validation
def string_validation():
    # Character type checking
    s1 = "abc123"
    is_alnum = s1.isalnum()  # True (alphanumeric)
    
    s2 = "abc"
    is_alpha = s2.isalpha()  # True (alphabetic)
    
    s3 = "123"
    is_digit = s3.isdigit()  # True (digits)
    
    s4 = "   "
    is_space = s4.isspace()  # True (whitespace)
    
    # Stripping whitespace
    text = "  hello world  "
    stripped = text.strip()  # 'hello world'
    left_stripped = text.lstrip()  # 'hello world  '
    right_stripped = text.rstrip()  # '  hello world'


# 4. String Formatting and Conversion
def string_formatting():
    # f-strings (Python 3.6+)
    name = "Alice"
    age = 30
    formatted = f"{name} is {age} years old"  # 'Alice is 30 years old'
    
    # format() method
    formatted2 = "{} is {} years old".format(name, age)
    
    # Converting between strings and other types
    num_str = str(42)  # '42'
    num_int = int("42")  # 42
    num_float = float("3.14")  # 3.14
    
    # Padding and alignment
    left_aligned = f"{name:<10}"  # 'Alice     '
    right_aligned = f"{name:>10}"  # '     Alice'
    center_aligned = f"{name:^10}"  # '  Alice   '
    zero_padded = f"{42:05d}"  # '00042'


# 5. Advanced String Techniques for Algorithms
def advanced_techniques():
    # Character frequency counting
    from collections import Counter
    s = "leetcode"
    char_count = Counter(s)  # Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    
    # Check if strings are anagrams
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    
    # Check if string is palindrome
    def is_palindrome(s: str):
        # Remove non-alphanumeric and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
    
    # String comparison for lexicographical sorting
    words = ["apple", "banana", "cherry"]
    sorted_words = sorted(words)  # ['apple', 'banana', 'cherry']
    
    # Custom sorting
    sorted_by_length = sorted(words, key=len)  # ['apple', 'cherry', 'banana']
    
    # String building (more efficient than concatenation in loops)
    def build_string(n):
        result = []
        for i in range(n):
            result.append(str(i))
        return ''.join(result)


# 6. Regular Expressions for Pattern Matching
def regex_examples():
    import re
    
    text = "Email me at example@email.com or call at 123-456-7890"
    
    # Find all email addresses
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    # ['example@email.com']
    
    # Find all phone numbers
    phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
    # ['123-456-7890']
    
    # Replace pattern
    censored = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
    # 'Email me at example@email.com or call at XXX-XXX-XXXX'
    
    # Match at beginning
    starts_with_email = re.match(r'Email', text) is not None  # True


# 7. String Algorithms
def string_algorithms():
    # Longest Common Prefix
    def longest_common_prefix(strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
    # String hashing (for pattern matching)
    def rabin_karp(text, pattern):
        n, m = len(text), len(pattern)
        if m > n:
            return -1
        
        # Simple hash function (can be improved)
        def hash_str(s):
            return sum(ord(c) for c in s)
        
        pattern_hash = hash_str(pattern)
        for i in range(n - m + 1):
            if hash_str(text[i:i+m]) == pattern_hash:
                if text[i:i+m] == pattern:  # Verify to avoid collisions
                    return i
        return -1


# 8. Working with Unicode and Special Characters
def unicode_examples():
    # Unicode characters
    unicode_str = "Hello, 世界!"
    
    # Encoding/decoding
    encoded = unicode_str.encode('utf-8')  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c!'
    decoded = encoded.decode('utf-8')  # 'Hello, 世界!'
    
    # Escape sequences
    escaped = "Line1\nLine2\tTabbed"
    
    # Raw strings (useful for regex)
    raw_str = r"This\nIs\tNot\Escaped"
    
    # Get character code (Unicode code point)
    char_code = ord('A')  # 65
    char_code_unicode = ord('世')  # 19990
    
    # Convert code to character
    char_from_code = chr(65)  # 'A'
    char_from_unicode = chr(19990)  # '世'
    
    # Iterate through string and get character codes
    for char in "Hello":
        print(f"Character: {char}, Code: {ord(char)}")


# Example usage
if __name__ == "__main__":
    print("String manipulation examples for algorithm problems")
    basic_operations()
    split_join_examples()
    string_validation()
    string_formatting()
    advanced_techniques()
    regex_examples()
    string_algorithms()
    unicode_examples()
