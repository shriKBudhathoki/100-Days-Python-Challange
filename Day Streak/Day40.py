'''
Day 39 KBC Only


Write a python program to translate a message into secret code language.
use the rules below to translate normal english into secret code language.

coding:
if the word contains atleast 3 characters, removes the first letter
and append it at the end now append three random characters at the starting and the end

else 
simply reverse the string

Decoding

if the word contain less than 3 characters reverse it

else 
remove 3 random characters from start and end. Now remove the last letter and append it to tthe beginner

your program should ask whether you want to code or decode

'''
import random
import string

def generate_random_chars(length=3):
    """Generate random characters for encoding"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def encode_word(word):
    """Encode a single word using the secret code rules"""
    if len(word) >= 3:
        # Remove first letter and append it at the end
        modified_word = word[1:] + word[0]
        # Add 3 random characters at start and end
        random_start = generate_random_chars(3)
        random_end = generate_random_chars(3)
        return random_start + modified_word + random_end
    else:
        # Simply reverse the string
        return word[::-1]

def decode_word(word):
    """Decode a single word using the secret code rules"""
    if len(word) < 3:
        # Reverse it
        return word[::-1]
    else:
        # Remove 3 characters from start and end
        core_word = word[3:-3]
        if len(core_word) == 0:
            return ""
        # Remove last letter and append it to the beginning
        return core_word[-1] + core_word[:-1]

def encode_message(message):
    """Encode an entire message"""
    words = message.split() # String method that breaks text into a list using whitespace as separator
    encoded_words = []
    
    for word in words:
        # Separate punctuation from the word
        punctuation = ""
        clean_word = word
        
        # Extract trailing punctuation
        while clean_word and clean_word[-1] in string.punctuation:
            punctuation = clean_word[-1] + punctuation
            clean_word = clean_word[:-1]
        
        # Extract leading punctuation
        leading_punct = ""
        while clean_word and clean_word[0] in string.punctuation:
            leading_punct += clean_word[0]
            clean_word = clean_word[1:]
        
        if clean_word:
            encoded_word = encode_word(clean_word.lower())
            encoded_words.append(leading_punct + encoded_word + punctuation)
        else:
            encoded_words.append(word)  # Only punctuation
    
    return " ".join(encoded_words)

def decode_message(message):
    """Decode an entire message"""
    words = message.split()
    decoded_words = []
    
    for word in words:
        # Separate punctuation from the word
        punctuation = ""
        clean_word = word
        
        # Extract trailing punctuation
        while clean_word and clean_word[-1] in string.punctuation:
            punctuation = clean_word[-1] + punctuation
            clean_word = clean_word[:-1]
        
        # Extract leading punctuation
        leading_punct = ""
        while clean_word and clean_word[0] in string.punctuation:
            leading_punct += clean_word[0]
            clean_word = clean_word[1:]
        
        if clean_word:
            decoded_word = decode_word(clean_word)
            decoded_words.append(leading_punct + decoded_word + punctuation)
        else:
            decoded_words.append(word)  # Only punctuation
    
    return " ".join(decoded_words)

def main():
    """Main program function"""
    print("=== Secret Code Language Translator ===")
    print("\nCoding Rules:")
    print("- Words with 3+ characters: Remove first letter, append to end, add 3 random chars at start and end")
    print("- Words with <3 characters: Simply reverse")
    print("\nDecoding Rules:")
    print("- Words with <3 characters: Reverse")
    print("- Words with 3+ characters: Remove 3 chars from start/end, move last letter to beginning")
    
    while True:
        print("\n" + "="*50)
        choice = input("\nWhat would you like to do?\n1. Encode a message\n2. Decode a message\n3. Exit\nEnter your choice (1/2/3): ").strip()
        
        if choice == '1':
            message = input("\nEnter the message to encode: ")
            encoded = encode_message(message)
            print(f"\nOriginal message: {message}")
            print(f"Encoded message: {encoded}")
            
        elif choice == '2':
            message = input("\nEnter the message to decode: ")
            decoded = decode_message(message)
            print(f"\nEncoded message: {message}")
            print(f"Decoded message: {decoded}")
            
        elif choice == '3':
            print("\nGoodbye!")
            break
            
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()