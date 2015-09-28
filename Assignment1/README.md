# Class 13 (Wednesday, Sept. 23, 2015)

We'll continue going over the [data-cleaning script](https://github.com/cjdd3b/advanced-data-journalism/blob/master/week5/class12/cleaner.py), talk about some [basic string methods](http://www.thehelloworldprogram.com/python/python-string-methods/) and some [not-so-basic ones](http://www.tutorialspoint.com/python/string_zfill.htm), and then move on to your assignment, which will be due next Monday.

Your task is to write a script that will take [this file](https://github.com/cjdd3b/advanced-data-journalism/blob/master/week5/class13/data/cleanme.csv), perform several cleanup operations on it, and then output a selection of it as a clean CSV. You should be able to acheive all of this using the skills we've learned in class, plus the string methods outlined above. Specifically, you should:

  - Be sure all text fields are represented in uppercase
  - Add leading zeroes to any ZIP codes that are less than 5 digits long (for instance, "2169" should become "02169")
  - Delete any non-breaking spaces (represented as the HTML character "&nbsp;")
  - Save only contributions of $1,000 or more to the output CSV

Once you're done, you should check the results into your Github account, using either a new repository or a single repository dedicated to all of your assignments. The assignment will be due next Monday, Sept. 28.