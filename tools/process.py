import argparse
import json

##############################
#### Global metrics
##############################

# Reverse Indexing: 
#   Key: symbol
#   Value: files that have that
metric_distinct_latex_symbols = dict()

# Reverse Indexing: 
#   Key: latex keywords that start with '\'
#   Value: files that have that
metric_distinct_latex_keywords = dict()

##############################

def count_distinct_latex_symbols(json_data):
    image_file = json_data['ImageFile'].encode('ascii', 'ignore')
    label = json_data['Label'].encode('ascii', 'ignore')

    latex_symbols = label.split(' ')
    
    for latex_symbol in latex_symbols:
        file_list = metric_distinct_latex_symbols.get(latex_symbol, [])
        file_list.append(image_file)
        metric_distinct_latex_symbols.update({latex_symbol: file_list})

        # Check keyword
        if len(latex_symbol) > 0 and latex_symbol.startswith('\\'):
            file_list = metric_distinct_latex_keywords.get(latex_symbol, [])
            file_list.append(image_file)

            metric_distinct_latex_keywords.update({latex_symbol: file_list})

def process_data_file(dataset_location):
    # Processing
    print("start processing...")

    # Load data
    with open(dataset_location, 'r') as data_file:
        file_lines = data_file.readlines() 
    
    for line in file_lines:
        data_item = json.loads(line)
        count_distinct_latex_symbols(data_item)

def print_result():    
    # Printing
    sorted_keywords = metric_distinct_latex_keywords.keys()
    sorted_keywords.sort()
    #print('\n'.join(sorted_keywords))

    sorted_symbols = metric_distinct_latex_symbols.keys()
    sorted_symbols.sort()
    print('\n'.join(sorted_symbols))

if __name__ == "__main__":
    # Set args
    parser = argparse.ArgumentParser(description='Print out the latex.')
    parser.add_argument('dataset', type=str, nargs=1,
                    help='the data set location')

    # Get location
    args = parser.parse_args()
    dataset_location = args.dataset[0]

    process_data_file(dataset_location)

    print_result()