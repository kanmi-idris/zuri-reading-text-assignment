# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
def read_file_content(filename):
    # [assignment] Add your code here
    with open("C://Users/HP/Downloads/Reading-Text-Files/story.txt") as f:
        file = f.read()
    return file

outcome = read_file_content(
    "C://Users/HP/Downloads/Reading-Text-Files/story.txt")
print(outcome)


def count_words(str):
    outcome = read_file_content(
        "C://Users/HP/Downloads/Reading-Text-Files/story.txt")
    # Create an empty dictionary
    counts = dict()
    words = str.split()

    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(outcome))
