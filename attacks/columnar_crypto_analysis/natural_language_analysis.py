from nltk.tokenize import word_tokenize
from nltk.corpus import words
from collections import defaultdict

english_words = set(words.words())

MIN_LENGTH = 3
MAX_LENGTH = 15  
BASE = 'abcdefghijklmnopqrstuvwxyz'

ENGLISH_FREQ = {
    'e': 0.127, 't': 0.091, 'a': 0.082, 'o': 0.075, 'i': 0.070,
    'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.060, 'd': 0.043,
    'l': 0.040, 'c': 0.028, 'u': 0.028, 'm': 0.024, 'w': 0.024,
    'f': 0.022, 'g': 0.020, 'y': 0.020, 'p': 0.019, 'b': 0.015,
    'v': 0.0098, 'k': 0.0077, 'j': 0.0015, 'x': 0.0015, 'q': 0.00095,
    'z': 0.00074
}

def normalize_text(text):
    processed_text = ''

    for letter in text.lower():
        if letter in BASE:
            processed_text+=letter
            
    return processed_text


def type_token_ratio(text):
    valid = []
    for l in range(MIN_LENGTH, min(MAX_LENGTH, len(text)) + 1):  # Added +1 to include MAX_LENGTH
        if text[:l] in english_words:
            valid.append(text[:l])
            remaining = text[l:]
            if len(remaining) >= MIN_LENGTH:
                # Recursively get words from remaining text
                valid_words_from_remaining = []
                recursive_result = type_token_ratio(remaining)
                if isinstance(recursive_result, list):  # Handle both return types
                    valid_words_from_remaining = recursive_result
                else:
                    if recursive_result > 0:  # If TTR was returned
                        valid_words_from_remaining = [remaining[:MIN_LENGTH]]  # Fallback
                valid.extend(valid_words_from_remaining)
    
    # Return either the word list or TTR ratio
    if not valid:
        return 0
    else:
        # Return list for recursive calls, TTR for final call
        if len(text) > MAX_LENGTH * 2:  # Arbitrary threshold to switch to TTR
            return len(set(valid)) / len(valid)
        return valid
    

def frequency_score(text):
    if not text:
        return 0.0
    
    total = 0.0
    freq_count = defaultdict(int)
    
    for char in text:
        if char in ENGLISH_FREQ:
            freq_count[char] += 1
    
    for char, count in freq_count.items():
        observed_ratio = count / len(text)
        expected_ratio = ENGLISH_FREQ[char]
        total += max(0, 1.0 - abs(observed_ratio - expected_ratio)/expected_ratio)
    
    return total / len(text)


def word_count(text):
    word_count = 0
    i = 0
    n = len(text)
    
    while i <= n - MIN_LENGTH:
        # Search for longest possible valid word
        found = False
        for l in range(min(MAX_LENGTH, n - i), MIN_LENGTH - 1, -1):
            candidate = text[i:i+l]
            if candidate in english_words:
                word_count += 1
                i += l  # Skip past this word
                found = True
                break
        
        if not found:
            i += 1  # Advance if no word found
    return word_count 