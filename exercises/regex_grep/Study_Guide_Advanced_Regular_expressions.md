# Study guide: Advanced regular expressions

Advanced regular expressions—commonly referred to as advanced regexes—are used by developers to execute complicated pattern matching against strings. In this reading, you will learn about some of the common examples of advanced regular expressions.

## **Alterations**

An alteration matches any one of the alternatives separated by the pipe | symbol. Let’s look at an example:

 **r"location.\*(London|Berlin|Madrid)"** 

This line of code will match the text string **location is London**, **location is Berlin**, or **location is Madrid**.

## **Matching only at the beginning or end**

If you use the circumflex symbol (also known as a caret symbol) ^ as the first character of your regex, it will match only if the pattern occurs at the start of the string. Alternatively, if you use the dollar sign symbol $ at the end of a regex, it will match only if the pattern occurs at the end. Let’s look at an example:

**r”^My name is (\\w+)”** 

This line of code will match **My name is Asha** but not **Hello. My name is Asha.**

## **Character ranges**

Character ranges can be used to match a single character against a set of possibilities. Let’s look at a couple of examples:

**r”\[A-Z\]** This will match a single uppercase letter.

**r”\[0-9$-,.\]** This will match any of the digits zero through nine, or the dollar sign, hyphen, comma, or period.

The two examples above are often combined with the repetition qualifiers. Let’s look at one more example:

**r”(\[0-9\]{3}-\[0-9\]{3}-\[0-9\]{4})”**

This line of code will match a U.S. phone number such as **888-123-7612**.

## **Backreferences**

A backreference is used when using re.sub() to substitute the value of a capture group into the output. Let’s look at an example:

**\>\>\> re.sub(r”(\[A-Z\])\\.\\s+(\\w+)”, r”Ms. \\2”, “A. Weber and B. Bellmas have joined the team.”)**

This line of code will produce **Ms. Weber and Ms. Bellmas have joined the team**.

## **Lookahead**

A lookahead matches a pattern only if it’s followed by another pattern. Let’s look at an example:

If the regex was **r”(Test\\d)-(?=Passed)”** and the string was **“Test1-Passed, Test2-Passed, Test3-Failed, Test4-Passed, Test5-Failed”** the output would be:

**Test1, Test2, Test4**

## **Key takeaways**

The types of advanced regular expressions explained in this reading are just some of the more commonly used ones by developers. They are beneficial in pattern matching, text manipulation, and data validation. For more information, check out the following link:

* [https://regexcrossword.com/](https://regexcrossword.com/)

