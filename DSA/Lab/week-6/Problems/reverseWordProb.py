def reverseWords(string):
   stack = []
   reverseString = ""
   word = ""
   
   for char in string:
       if char == " ":
           stack.append(word)
           word = ""
       else:
           word += char

   stack.append(word)
   
   while stack:
       reverseString += stack.pop()
       if stack:
           reverseString += " "
    
   return reverseString
    
    
            


print(reverseWords("Sher Khan"))

