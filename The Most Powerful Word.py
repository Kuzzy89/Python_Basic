the_most_powerful_word_text = ""
the_most_powerful_word_counter = 0

while True:
    word = input()

    if word == "End of words":
        break

    current_word_counter = 0
    for ch in word:
        current_word_counter += ord(ch)

    if word[0].lower() in "aeiouy":
        current_word_counter *= len(word)
    else:
        current_word_counter = int(current_word_counter / len(word))

    if the_most_powerful_word_counter < current_word_counter:
        the_most_powerful_word_counter = current_word_counter
        the_most_powerful_word_text = word

print(f"The most powerful word is {the_most_powerful_word_text} - {the_most_powerful_word_counter}")
