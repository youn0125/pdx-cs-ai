
#features : Emit comma-separated line with paragraph identifier
CS 441/541 Fall 2020 class

Mi Yon Kim / HW #3 - Author Identification by Machine Learning

This program emits comma-separated line with paragraph identifier

What decisions you made in constructing your instances?
 * First, I construct each instance with paragraph.
 * Second, each instance have class(1 = shelly, 0 = Austen), paragraph identifier, 
   and a set of all unique words present in the paragraph.
 * Third, I strip away leading and trailing punctuation.

What machine learner(s) you tried?
 * I tried nbayes and id3 learners.

How the learners performed?
 * Nbayes: The naive bayes learner performed approximately 72%(median of 10) of accuracy.
 * Id3: The id3 learner performed approximately 82%(median of 10) of accuracy
 * Basically the learners found the accuracy through n-way cross-validation.