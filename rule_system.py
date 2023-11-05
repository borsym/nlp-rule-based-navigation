import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)


# pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
# Define patterns for relevant phrases
# patterns = [
#     [{"LOWER": "person"}, {"LOWER": "left"}],
#     [{"LOWER": "person"}, {"LOWER": "left"}, {"LOWER": "frame"}],
#     [{"LOWER": "person"}, {"LOWER": "nearly"}, {"LOWER": "left"}, {"LOWER": "frame"}],
#     [{"LOWER": "bounding"}, {"LOWER": "box"}, {"LOWER": "disappeared"}],
#     [{"LOWER": "bounding"}, {"LOWER": "box"}, {"LOWER": "exceeded"}, {"LOWER": "frame"}],
# ]

patterns = [
    [{"DEP": "nsubj"}, {"LOWER": {"in": ["left", "nearlyleft", "disappeared", "exceeded"]}}]
]

matcher.add("FRAME_EVENT", patterns)

text = "The person left the frame. Please instruct them to go back to the middle."

doc = nlp(text)
matches = matcher(doc)


for match_id, start, end in matches:
        match_tokens = doc[start:end]
        match_text = match_tokens.text
        if "left" in match_text or "disappeared" in match_text:
            # Instruct the person to go back to the middle of the frame
            print("Instruct the person to move back to the middle of the frame.")