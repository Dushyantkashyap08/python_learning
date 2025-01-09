#a spam comment is defined as a text containing following words:
#"make a lot of money", "buy now", "subscribe this", "click this".
#make a program to detect these spams

# text = input("enter the text : ")
# if "make a lot of money" in text:
#     print("this is a spam")
# elif "buy now" in text:
#     print("this is a spam")
# elif "subscribe this" in text:
#     print("this is a spam")
# elif "click this" in text:
#     print("this is a spam")
# else:
#     print("this is not a spam")
    

#more optimised way
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# Input text
text = input("Enter the text: ")

if any(keyword in text for keyword in spam_keywords):
    print("This is a spam")
else:
    print("This is not a spam")
