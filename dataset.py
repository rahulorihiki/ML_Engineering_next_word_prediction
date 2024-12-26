import random

def generate_text_data(file_path: str, num_sentences: int = 1000):
    """
    Generate synthetic text data for training a Next Word Prediction model.

    Args:
        file_path (str): Path to save the generated text data file.
        num_sentences (int): Number of sentences to generate.
    """
    subjects = ["The cat", "A dog", "The car", "The bird", "A programmer", "An engineer"]
    verbs = ["jumps", "runs", "codes", "flies", "drives", "builds"]
    objects = ["over the fence", "fast", "a program", "high in the sky", "on the road", "a robot"]
    connectors = ["and", "while", "because", "when", "but", "as"]

    sentences = []
    for _ in range(num_sentences):
        subject = random.choice(subjects)
        verb = random.choice(verbs)
        obj = random.choice(objects)
        if random.random() < 0.5:
            connector = random.choice(connectors)
            continuation = f"{connector} {random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"
            sentence = f"{subject} {verb} {obj}, {continuation}."
        else:
            sentence = f"{subject} {verb} {obj}."
        sentences.append(sentence)

    # Save to file
    with open(file_path, "w") as file:
        for sentence in sentences:
            file.write(sentence + "\n")

    print(f"Generated {num_sentences} sentences and saved to {file_path}")

if __name__ == "__main__":
    # Generate a dataset with 1000 sentences
    generate_text_data("data.txt", num_sentences=1000)
