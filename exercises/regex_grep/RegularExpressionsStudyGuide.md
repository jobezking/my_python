# Study guide: Regular expressions

A regular expression—sometimes called regex—is a string of characters that specifies a pattern to match against some text. In addition to matching patterns, they can search to extract specific parts of text, validate input data, and are supported by code editors and integrated development environments (IDEs). In this reading, you will look at some examples of common regexes used in coding. 

## **Regex examples**

**r”\\d{3}-\\d{3}-\\d{4}”**  This line of code matches U.S. phone numbers in the format 111-222-3333.

**r”^-?\\d\*(\\.\\d+)?$”**  This line of code matches any positive or negative number, with or without decimal places.

**r”^/(.+)/(\[^/\]+)/$”** This line of code is often used to extract specific parts of URLs or file paths, such as the directory names or filenames.

## **Helpful tool**

Sometimes regexes can be complex and difficult to read and understand—even for experienced programmers\! There are tools available to help break down the regex and explain what each part of the expression does. A common tool that you can use to help with understanding each stage of a regular expression is:

* [https://regex101.com/](https://regex101.com/)

## **Key takeaways**

Regular expressions offer powerful capabilities to programmers but, at times, can be complex and difficult to understand. The more you code with regular expressions, the more comfortable you will be using and understanding them. For more information on regex, check out the following links:

* [https://docs.python.org/3/howto/regex.html](https://docs.python.org/3/howto/regex.html)  
* [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)  
* [https://docs.python.org/3/howto/regex.html\#greedy-versus-non-greedy](https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy)

