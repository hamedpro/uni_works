given_list = list(map(lambda i : int(i) ,eval(input())))
positives_sum = None
negatives_sum = None
positive_numbers = list(filter(lambda x : x>0  , given_list))
negative_numbers = list(filter(lambda x : x<0  , given_list))

results =  {"negatives_sum" : sum(negative_numbers) , "positives_sum" : sum(positive_numbers)}
print("Sum of positive numbers: " + str(results['positives_sum']))
print("Sum of negative numbers: " + str(results['negatives_sum']))
