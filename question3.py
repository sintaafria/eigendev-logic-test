# Terdapat dua buah array yaitu array INPUT dan array QUERY, 
# silahkan tentukan berapa kali kata dalam QUERY terdapat pada array INPUT

def count_query_occurrences(input_arr, query_arr):
    res = []
    for query in query_arr:
        count = 0
        for input in input_arr:
            if (input == query):
                count += 1
        res += [count]
                  
    return res

INPUT = ['xc', 'dz', 'bbb', 'dz']
QUERY = ['bbb', 'ac', 'dz']

OUTPUT = count_query_occurrences(INPUT, QUERY)

print(OUTPUT)