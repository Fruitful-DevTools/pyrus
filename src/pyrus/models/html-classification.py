import spacy
import random
from spacy.util import minibatch, compounding

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Define the entities we want to extract
labels = ["PERSON", "JOB_TITLE", "EMAIL", "PHONE_NUMBER"]

# Define the training data
TRAIN_DATA = 

# Define the training function
def train_spacy_ner(nlp, train_data, labels, iterations=100):
    # Add the NER pipe to the pipeline if it doesn't exist
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner)
    else:
        ner = nlp.get_pipe("ner")

    # Add the labels to the NER pipe
    for label in labels:
        ner.add_label(label)

    # Disable the other pipes in the pipeline
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            random.shuffle(train_data)
            losses = {}
            batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.5, losses=losses)
            print("Iteration:", itn, "Losses:", losses)
    
    # Save the trained model
    nlp.to_disk("trained_model")

# Train the NER model
train_spacy_ner(nlp, TRAIN_DATA, labels)
