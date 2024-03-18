def even_or_odd(input_data):
    output_data = []
    for number in input_data:
        if number%2 == 0:
            result = True
            output_data.append(result)
        else:
            result = False
            output_data.append(result)
    key_value_pairs = zip(input_data,output_data)
    output_result = dict(key_value_pairs)
    return output_result
a = [1,2,3,4,5,6,7,8,9,10]
print(even_or_odd(a))