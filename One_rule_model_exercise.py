# ONE RULE MODEL EXERCISE

# ONE RULE MODEL PSEUDO-CODE
# (from book 'Data Mining: Practical Machine Learning Tools and Techniques', 2011
# by I.H. Witten, E. Frank, M.A. Hall - 3rd edition, pag. 86)
# For each attribute,
#   for each value of the attribute, make a rule as follows:
#       count how often each class appears
#       find the most frequent class
#       make the rule assigning that class to this attribute value.
#   Calculate the error rate of the rules.
# Choose the rule with the smallest error rate.

# For this exercise I assume that input data are given as a csv file stored in the same folder where running the flow
# The csv file must contain non-numerical labels and these are located as last value of each row in the csv file

import csv

def one_r_model(file_in):
    '''This is the main function, which reads the input csv file, calls the other functions
    and then prints out best rule and best accuracy'''
    csv_file_dict = read_csv_file(file_in)
    one_r_rule = best_rule(csv_file_dict)
    rule_out, rule_accuracy = one_r_rule
    print ('The best rule is:', rule_out)
    print ('Its accuracy is:', rule_accuracy)


def read_csv_file(csv_file_in):
    '''This function reads the csv file and put information into a dictionary form
    where the keys are the attributes and outcome and the values are lists of relevant variables and labels'''
    print('Notes on the expected csv file: The first row must contain the name of the attributes and outcome.')
    print('The label must be stored as the last value of each row.')
    print('The label must also be non-numerical, for example as <yes> or <no>.')
    print('When there is no majority on type of labels, ex number of yes = number of no, than preference on rule'
          ' is given according to alphabetical order.')
    with open(csv_file_in,'r') as csvfile:
        my_csv_file=csv.reader(csvfile, delimiter=',')
        mycsv_rows=list(my_csv_file)
        my_headers_list=mycsv_rows[0]
        my_headers_list[-1]='outcome'
        my_var_rowlists=mycsv_rows[1:]
        my_var_col_lists=[]
        n_col=len(my_headers_list)
        for i in range(0,n_col):
            my_var_col_lists.append([x[i] for x in my_var_rowlists])
        csvdict_lists = zip(my_headers_list,my_var_col_lists)
        my_csv_dict = dict(csvdict_lists)
        print('The csv dictionary looks as follows:', my_csv_dict)
        return my_csv_dict

# for example using file play_data_set.csv, my_csv_dict will look like:
    #{'humidity': ['humid', 'humid', 'humid', 'dry', 'dry', 'dry'],
    #'outcome': ['yes', 'no', 'no', 'no', 'yes', 'yes'],
    #'temperature': ['hot', 'hot', 'mild', 'mild', 'cold', 'cold'],
    #'weather': ['sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'clear']}


def attribute_rule(my_csv_dict,attribute):
    '''This function defines the best rule for each value of the attribute
    and calculates the accuracy of the rule for that attribute'''
    my_var_outcome = []
    col_var_list = my_csv_dict[attribute]
    col_outcome_list = my_csv_dict['outcome']
    for i in range(0,len(col_var_list)):
        my_var_outcome.append((col_var_list[i],col_outcome_list[i]))
    # ex. my_var_outcome for weather is:
    # [('sunny', 'yes'), ('sunny', 'no'), ('sunny', 'no'), ('rainy', 'no'), ('rainy', 'yes'), ('clear', 'yes')]

    dict_var_outs={}
    for x in my_var_outcome:
        if x[0] in dict_var_outs.keys():
            dict_var_outs[x[0]].append(x[1])
        else:
            dict_var_outs[x[0]]=[x[1]]
    # ex for weather, dict_var_outs = {'sunny':['yes','no','no'],'rainy':['no','yes'],'clear':'yes'}

    count_dict = {}
    for var in dict_var_outs.keys():
        list_outcomes = dict_var_outs[var]
        count_dict[var] = [(i, list_outcomes.count(i)) for i in set(list_outcomes)]
    # ex. for weather, count_dict = {'sunny': [('yes', 1), ('no', 2)],
    # 'rainy': [('yes', 1), ('no', 1)], 'clear': [('yes', 1)]}

    my_attr_rule_dict = {}
    for var in count_dict.keys():
        my_sorted_outs = sorted(count_dict[var], key= lambda tup:(-tup[1],tup[0]))
        my_attr_rule_dict[var] = my_sorted_outs[0][0]
    # in this way I obtain my rule for weather column:
    # {'sunny': 'no', 'rainy': 'no', 'clear': 'yes'}

    # the following is to calculate the accuracy for each attribute
    count_correct = []
    my_tot_instances =len(my_csv_dict[attribute])
    for variable in my_attr_rule_dict.keys():
        count_correct.append(dict_var_outs[variable].count(my_attr_rule_dict[variable]))
    tot_correct = sum(count_correct)
    attrib_accuracy = tot_correct/my_tot_instances
    return (my_attr_rule_dict,attrib_accuracy)


def best_rule(my_csv_dict):
    '''This function chooses the rule with the best accuracy'''
    best_score = -1
    best_rule = {}
    for attribute in my_csv_dict.keys():
        if attribute == 'outcome':
            continue
        temp_rule, temp_score = attribute_rule(my_csv_dict,attribute)
        if temp_score > best_score:
            best_score = temp_score
            best_rule = temp_rule
    return (best_rule,best_score)


