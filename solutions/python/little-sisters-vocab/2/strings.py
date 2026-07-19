"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    Parameters:
        word (str): The root word.

    Returns:
        str: Root word prepended with 'un'.
    """

    return "un" + word



def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    Parameters:
        vocab_words (list[str]): Vocabulary words with prefix at first index.

    Returns:
        str: Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '.

    Examples:
        >>> list('en', 'close', 'joy', 'lighten')
        'en :: enclose :: enjoy :: enlighten'.

    """
    separator = " :: " + vocab_words[0]
    return separator.join(vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """

    # BUG: str.replace("i", "y") replaces EVERY "i" in the whole word, not just
    # one that's part of the "iness" -> "y" spelling swap (e.g. heaviness -> heavy).
    # For a word like "lightness" there's no "i" before "ness" at all, but the
    # leftover "light" still contains an "i" (l-i-g-h-t), so it gets mangled
    # into "lyght".
    #
    # FIX: only swap i->y when the suffix is actually "iness". Use str.endswith()
    # to check for that specific case, then str slicing (word[:-len(suffix)]) to
    # strip the right number of characters instead of str.replace() acting globally:
    #
    #   if word.endswith("iness"):
    #       return word[:-len("iness")] + "y"
    #   return word[:-len("ness")]
    
    if word.endswith("iness"):
        return word[:-len("iness")] + "y"
    return word[:-len("ness")]


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """

    # BUG: sentence.split() only splits on whitespace, so trailing punctuation
    # stays glued to the word. For "His expression went dark." at index -1,
    # the extracted word is "dark." (with the period), so appending "en" gives
    # "dark.en" instead of "darken".
    #
    # FIX: strip trailing punctuation off the extracted word before appending
    # "en". str.strip() with a set of punctuation characters removes any of
    # them from both ends without touching letters in the middle:
    #
    #   word = sentence.split()[index].strip(".,!?;:")
    #   return word + "en"
    word = sentence.split()[index].strip(".")
    return word + "en"
