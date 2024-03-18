
#create a function to return a list having true for even numbers false for odd numbers for a given list

# create function
# list is input having numbers
# give conditions to get result
# if remaimder is 0 then true else false

def even_or_odd(input_data):
    output_data = []
    for number in input_data:
        if number%2 == 0:
            result = True
            output_data.append(result)
        else:
            result = False
            output_data.append(result)
    return output_data
a = [1,2,3,4,5,6,7,8,9,10]
print(even_or_odd(a))