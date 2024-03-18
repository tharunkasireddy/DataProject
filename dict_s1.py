def even_or_odd(input_data):
    output_data = []
    for number in input_data:
        output_result = {}
        if number%2 == 0:
            result = True
            output_result["input"]= number
            output_result["output"]= result
            output_data.append(output_result)
        else:
            result = False
            output_result["input"]= number
            output_result["output"]= result
            output_data.append(output_result)
    return output_data

""" key_value_pairs = zip(input_data,output_data)
    output_dict = dict(key_value_pairs)
    return output_dict"""

a = [1,2,3,4,5,6,7,8,9,10]
print(even_or_odd(a))