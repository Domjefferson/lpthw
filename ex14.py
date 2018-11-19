from sys impor argv
script, user_name = argv
prompt='>'
print(f"hi{username}, I'm the {script}script.")
print("i'd like to aask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)
print(f"where do you live{user_name}?")
lives=input(prompt)
print("what kind of computer do you have?")
computer = input(prompt)
print(f"""
      alright, so you said{likes} about liking Me
      you live in {lives}   not sure where that is and you have a {computer}computer . """
      )
