# frequencies
Rate the quality of word-by-word generated text.

The generated text is evaluated by checking the frequency of words in the corpus and the generated text, subtracting them, and squaring the result to get the mean squared error.  

`raw_corpus` should be all of the text used to train the text generation AI, concatenated into a string, and `raw_text` should be the generated text.
