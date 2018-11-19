def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses")
    print(f"you have {boxes_of_crackers} boxes of crackers!:")
    print("thats more than enough ")
    print ("get a drink \n")

print ("we can just give the function numbers directly ")
cheese_and_crackers(25, 50)

print("or , we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#declares a vairiable and sets amounts for cheese and crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")
cheese_and_crackers(10+20,5 + 6)
#adds vaiables to the cheese and crackers method
print("And we can combine the two , variables and math:")
cheese_and_crackers(amount_of_cheese+250 , amount_of_crackers+1000)
#uses the method to set cvairables and add numbers useing operators
