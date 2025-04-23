import csv
import matplotlib.pyplot as plt

# Define the scoring rules
score_mapping = {
    "Yes, greatly affected": 2,
    "Yes, always": 2,
    "Glance at the screen to see the directions": 2,
    "Yes, often": 2,
    "Yes, this has happened many times": 2,
    "No": 2,
    "Yes, only a few times": 1,
    "Yes, this has happened a few times": 1,
    "Yes, sometimes": 1,
    "Both": 1,
    "Yes, somewhat affected": 1,
    "No, not a significant effect": 0,
    "No, never": 0,
    "No, I prefer to get help from someone": 0,
    "Utilize voice navigation to tell me the directions": 0,
    "Yes, many times": 0,
    "No, this has never happened": 0
}

# Function to calculate score for a given response
def calculate_score(response):
    return score_mapping.get(response, 0)

# Process the CSV file and write results to a new CSV file
def process_csv(file_path):
    results = []
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Read the header row
        header = next(csv_reader)
        
        # Process each respondent's answers
        for idx, row in enumerate(csv_reader):
            respondent_letter = chr(65 + idx) # Assign letters A, B, C,... to each respondent
            timestamp = row[0]
            score_details = []
            total_score = 0
            
            # Calculate scores for columns 21 through 35 (index 20 to 34)
            for i in range(20, 35):
                response = row[i]
                score = calculate_score(response)
                score_details.append(score)
                total_score += score
            
            # Append the results for the current respondent
            results.append({
                'Respondent': respondent_letter,
                'Timestamp': timestamp,
                'Scores': score_details,
                'Total Score': total_score
            })
    
    # Sort results by Total Score in ascending order (lowest to highest)
    results.sort(key=lambda x: x['Total Score'])
    
    # Write results to a new CSV file
    with open('result3s.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Respondent', 'Timestamp', 'Scores', 'Total Score'])
        
        for result in results:
            csv_writer.writerow([result['Respondent'], result['Timestamp'], result['Scores'], result['Total Score']])
    
    return results

# Plot the score results as a bar chart sorted by score
def plot_results(results):
    respondents = [result['Respondent'] for result in results]
    total_scores = [result['Total Score'] for result in results]
    
    plt.figure(figsize=(10, 6))
    plt.bar(respondents, total_scores, color='#4101B9')
    plt.xlabel('Respondent')
    plt.ylabel('Total Score')
    plt.title('Total Scores of Survey Respondents (Sorted by Score)')
    plt.ylim(0, 30) # Set the range of the y-axis from 0 to 30
    plt.tight_layout()
    
    # Save the plot as an image file
    plt.savefig('score_results_sorted.png')
    
    # Show the plot
    plt.show()

# Example usage
file_path = 'survey_responses.csv'
results = process_csv(file_path)
plot_results(results)
