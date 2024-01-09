import pandas as pd

# Initialize variables
data = []
current_query_id = None
doc_number = 0

# Read the file and process each line
with open('/Users/soumyagupta/yahoo_ltr/Learning to Rank Challenge/ltrc_yahoo/set1.train.txt', 'r') as file:
    for line in file:
        parts = line.split(' ')
        query_id = parts[1].split(':')[1]
        features = {f"feature{i}": float(0.0) for i in range(700)}
        
        
        # if query_id != current_query_id:
        #     current_query_id = query_id
        #     doc_number = 1
        # else:
        #     doc_number += 1
        # for part in parts[2:] :
        #     features[f"features{part.split(':')[0]}"] = float(part.split(':')[1])   
        # features['query_id'] = query_id
        # features['document_number'] = doc_number
        # data.append(features)
        
        


df = pd.DataFrame(data)  
# Export to CSV
df.to_csv('features.csv', index=False)
