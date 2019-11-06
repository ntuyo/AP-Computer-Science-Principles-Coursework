example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard " \
                    "to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for " \
                    "a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to " \
                    "prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana " \
                    "Grande decides to go to Times Square instead. What a beautiful day in New York."

def find_max_value():
    words = {'a': 6, 'to': 4, 'grande': 4, 'ariana': 4, 'york': 3, 'was': 3,
             'of': 3, 'new': 3, 'in': 3, 'the': 2, 'reade': 2, 'instead': 2,
             'from': 2, 'duane': 2, 'day': 2, 'beautiful': 2}
    v = list(words.values())
    k = list(words.keys())
    return k[v.index(max(v))], "is the highest value"


hi = print("Max Value")
print(find_max_value())
example_paragraph_lower = example_paragraph.lower()
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")
example_word_list = example_paragraph_lower_no_punctuation.split(" ")

# My dad helped me to create a dictionary and incorporate it into my code
