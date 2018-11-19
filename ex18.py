def print_two(* args):
    arg1, arg2 = args
    print(f"arg1: {arg1} , arg2: {arg2}")
#creats a functuon that takes in two arguments

def print_two_again(arg1 , arg2):
    print(f"arg1: {arg1} , arg2: {arg2}")
#takes in two arguments but directly in the funtion
def print_one(arg1):
    print(f"arg1: {arg1}")


def prnt_none():
    print(f"I got nothing. ")
#takes in no arguments but orints  sting to the console
print_two(" dominic" ,"Jefferson")
print_two_again("Dominic","Jeffferson")

print_one("first")
prnt_none()
