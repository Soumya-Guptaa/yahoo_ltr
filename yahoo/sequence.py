import pandas as pd 
df = pd.read_csv('output10.csv')
import numpy as np
def calculate_click_probability(relevance_score, epsilon, ymax, exam_prob):
    result = epsilon + (1 - epsilon) * ((2**relevance_score - 1) / (2**ymax - 1))
    return round(result * exam_prob, 3)

# Generate permutations and calculate click probabilities
permutation_results = []
epsilon = 0.1
ymax = 4
examination_prob = [0.68, 0.61, 0.48,0.34, 0.28, 0.20, 0.11, 0.10, 0.08, 0.06]
num_permutations = 2
for query_id in df['query_id'].unique():
    query_subset = df[df['query_id'] == query_id]
    for perm_id in range(num_permutations):        
        permuted_docs = query_subset.sample(frac=1).reset_index(drop=True)        
        permuted_docs['click_prob'] = [
            calculate_click_probability(relevance, epsilon, ymax, examination_prob[pos])
            for pos, relevance in enumerate(permuted_docs['relevance_score'])
        ]
        
        # Store the query_id, permutation_id, document numbers, and click probabilities
        permutation_info = {
            'query_id': query_id,
            'permutation_id': perm_id + 1
            
        }
        
        # Add document numbers and probabilities to the permutation info
        for position in range(1, 11):
            permutation_info[f'doc_{position}'] = permuted_docs.at[position - 1, 'document_no']
            permutation_info[f'click_prob_{position}'] = permuted_docs.at[position - 1, 'click_prob']
            permutation_info[f'relevance_score{position}'] = permuted_docs.at[position-1 , 'relevance_score']
        
        permutation_results.append(permutation_info)
    
    

# Create a DataFrame from the permutation results
permutations_df = pd.DataFrame(permutation_results)
permutations_df.to_csv('final_output.csv', index=False)



