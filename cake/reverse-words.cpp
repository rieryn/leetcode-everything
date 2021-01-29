void reverseCharacters(string& str, size_t leftIndex, size_t rightIndex)
{
    // walk towards the middle, from both sides
    while (leftIndex < rightIndex) {

        // swap the left char and right char
        swap(str[leftIndex], str[rightIndex]);
        ++leftIndex;
        --rightIndex;
    }
}

void reverseWords(string& message)
{
    // handle empty message
    if (message.empty()) {
        return;
    }

    // first we reverse all the characters in the entire message
    reverseCharacters(message, 0, message.length() - 1);
    // this gives us the right word order
    // but with each word backward

    // now we'll make the words forward again
    // by reversing each word's characters

    // we hold the index of the *start* of the current word
    // as we look for the *end* of the current word
    size_t currentWordStartIndex = 0;
    for (size_t i = 0; i <= message.length(); ++i) {

        // found the end of the current word!
        if (i == message.length() || message[i] == ' ') {

            // if we haven't exhausted the string our
            // next word's start is one character ahead
            reverseCharacters(message, currentWordStartIndex, i - 1);
            currentWordStartIndex = i + 1;
        }
    }
}