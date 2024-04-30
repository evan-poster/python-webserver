import csv
import server.settings

# Function to load data from csv file
def load_data():
    result = {}
    # Load data from csv file
    with open(server.settings.data_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Each record has three columns: word, part of speech, definition
        # Create a dictionary key as needed, and the value is a list of definitions such as [["definition", "part of speech"],...]
        for row in reader:
            lower_row = row[0].lower()
            if lower_row not in result:
                result[lower_row] = []
            result[lower_row].append([row[1], row[2]])
    return result

def parse_query(query):
    query = query.lower()
    if query[0] == "/":
        query = query[1:]
    return str(query)
