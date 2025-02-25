# Fuzzy matching, also known as approximate string matching, is a technique used to 
# find strings that are similar to a given pattern, even if they are not exactly the same.

#FuzzyWuzzy is a library of Python which is used for string matching.
def fuzzywuzzy(string1, string2):
    from fuzzywuzzy import fuzz
    # Simple ratio
    print(fuzz.ratio(string1, string2))

    # Partial ratio
    print(fuzz.partial_ratio(string1, string2))

    # Token sort ratio
    print(fuzz.token_sort_ratio(string1, string2))

    # Token set ratio
    print(fuzz.token_set_ratio(string1, string2))

def rapidfuzz(string1, string2):
    from rapidfuzz import fuzz
    # Simple ratio
    print(fuzz.ratio(string1, string2))

    # Partial ratio
    print(fuzz.partial_ratio(string1, string2))

    # Token sort ratio
    print(fuzz.token_sort_ratio(string1, string2))

    # Token set ratio
    print(fuzz.token_set_ratio(string1, string2))

def difflib(string1, string2):
    import difflib
    print(difflib.SequenceMatcher(None, string1, string2).ratio())



string1 = "apple inc"
string2 = "apple incorporated"
# fuzzywuzzy(string1, string2)
# rapidfuzz(string1, string2)
difflib(string1, string2)