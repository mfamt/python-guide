---
title: Defining a main function for a Python module
ordernum: 1600
references:
  - url: http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    title: "What does `if __name__ == “__main__”:` do?" 

tldr: |
  
  Inside a Python script file:
  ~~~py
  if __name__ == "__main__":
      do_something()
      that_you_want_to_do()
      when_this_script_is_executed()
      # but not when it is merely included as an import
  ~~~

---


