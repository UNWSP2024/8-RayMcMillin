#Ray McMillin, Word Separator Code, 3/21/25
def word_separator(sentence):

    new_sentence = ""
    for i in range(len(sentence)):
        if sentence[i].isupper() and i > 0:
            new_sentence += " "
        new_sentence += sentence[i].lower()

    new_sentence = new_sentence.capitalize()

    new_sentence += "."
    
    return new_sentence.strip()



sentence = input("Please enter a sentence with continuous words. Ex. (StopAndSmellTheRoses)")

new_sentence = word_separator(sentence)

print(new_sentence)
