import json

# Load training data from train.json
with open('train.json', 'r') as f:
    train_data = json.load(f)

# Load testing data from test.json
with open('test.json', 'r') as f:
    test_data = json.load(f)

# Preview the data
print("Training Data:", train_data[:2])  # Displaying the first two records
print("Testing Data:", test_data[:2])
