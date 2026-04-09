import math

# Step 1: Euclidean Distance
def euclidean_distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        diff = p1[i] - p2[i]
        sum += diff * diff
    return math.sqrt(sum)


# Step 2: Majority Vote (Manual, no Counter)
def majority_vote(labels):
    freq = {}

    # Count frequency
    for label in labels:
        if label in freq:
            freq[label] += 1
        else:
            freq[label] = 1

    # Find label with max frequency
    max_count = -1
    result = None

    for label in freq:
        if freq[label] > max_count:
            max_count = freq[label]
            result = label

    return result


# Step 3: KNN Algorithm
def knn(X_train, y_train, X_test, k):
    predictions = []

    for test_point in X_test:
        distances = []

        # Calculate distances
        for i in range(len(X_train)):
            dist = euclidean_distance(test_point, X_train[i])
            distances.append((dist, y_train[i]))

        # Sort distances manually (simple bubble sort)
        for i in range(len(distances)):
            for j in range(i + 1, len(distances)):
                if distances[i][0] > distances[j][0]:
                    distances[i], distances[j] = distances[j], distances[i]

        # Pick k nearest neighbors
        neighbors = []
        for i in range(k):
            neighbors.append(distances[i][1])

        # Predict using majority vote
        prediction = majority_vote(neighbors)
        predictions.append(prediction)

    return predictions


# Step 4: Example Data
X_train = [
    [2, 4],
    [4, 6],
    [6, 8],
    [8, 10],
    [1, 3],
    [3, 5]
]

y_train = ['A', 'A', 'B', 'B', 'A', 'A']

X_test = [
    [5, 7],
    [2, 3]
]

k = 3

# Run KNN
result = knn(X_train, y_train, X_test, k)
print("Predictions:", result)