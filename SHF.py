def sequence_harmonization(scores, z):
    """
    Calculate the Normalized Route Multipliers for a set of scores.

    :param scores: A list of scores for each task.
    :param z: The partition number for calculating the rational partition q.
    :return: A list of tuples with each task's index and its corresponding multiplier.
    """
    total_score = sum(scores)
    normalized_scores = [score / total_score for score in scores]

    multipliers = []
    for w in normalized_scores:
        multiplier = int(w * z)
        multipliers.append(multiplier)

    return multipliers

# Example usage
print("Initial sequence ∏ = { π_1, π_2, π_3, π_4 }")
task_scores = [2.5, 3.5, 1.0, 2.0]  # Scores for each task
print(f"Initial task scores")
for idx, score in enumerate(task_scores):
    print(f"Task {idx + 1}: Multiplier = {score}")
partition_number = 4  # z value

# Calculate the NRM multipliers
multipliers = sequence_harmonization(task_scores, partition_number)

# Print the results
print("Task Multipliers:")
for idx, multiplier in enumerate(multipliers):
    print(f"Task {idx + 1}: Multiplier = {multiplier}")

print("Final sequence ∏* = { π_1, π_2 }")

