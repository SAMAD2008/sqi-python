# Project Overview:
# Develop an Exam Wizard program in Python that hardcodes a set of at least 5 theory 
# questions and evaluates the student's answers based on the presence of specific keywords or phrases. The program should ask these questions to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Keywords:
# Create at least 5 theory questions.
# For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# Assign weights to each keyword based on its importance.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Evaluate the user's answers based on the presence of the specified keywords..
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score out of the max score e.g. 10/12.
# Sample Question and Evaluation Criteria:
# Question: Explain the process of photosynthesis.

# Ideal Answer: Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.

# Keywords and Weights:
# Photosynthesis (2 points)
# Light energy (1 point)
# Chemical energy (1 point)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# ATP (1 point)
# Example of Keyword-Based Marking:
# Student's Answer: Photosynthesis is a process in which plants use sunlight to make 
# food. It happens in the chloroplasts where chlorophyll absorbs light. The plants take in carbon dioxide and water, and produce glucose and oxygen.
# Marked Answer:
# Photosynthesis (2 points)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# Total Score: 9 out of 12 points.

questions = [
    {
        "question": "Explain the process of photosynthesis.",
        "keywords": {
            "Photosynthesis": 2,
            "Light energy": 1,
            "Chemical energy": 1,
            "Chloroplasts": 2,
            "Chlorophyll": 1,
            "Carbon dioxide": 1,
            "Water": 1,
            "Glucose": 1,
            "Oxygen": 1,
            "ATP": 1
        }
    },
    {
        "question": "Describe the water cycle.",
        "keywords": {
            "Evaporation": 2,
            "Condensation": 2,
            "Precipitation": 2,
            "Collection": 1,
            "Sun": 1
        }
    },
    {
        "question": "What are the main functions of the human respiratory system?",
        "keywords": {
            "Oxygen intake": 2,
            "Carbon dioxide removal": 2,
            "Breathing": 1,
            "Lungs": 1,
            "Alveoli": 1
        }
    },
    {
        "question": "Explain the theory of evolution by natural selection.",
        "keywords": {
            "Evolution": 2,
            "Natural selection": 2,
            "Adaptation": 1,
            "Survival of the fittest": 1,
            "Genetic variation": 1
        }
    },
    {
        "question": "Describe the structure and function of DNA.",
        "keywords": {
            "Double helix": 2,
            "Nucleotides": 2,
            "Genetic information": 2,
            "Replication": 1,
            "Genes": 1
        }
    }
]
score = 0

for question in questions:
    print(question['question'])
    student_answer = input(": ").lower()
    for keyword, weight in question['keywords'].items():
        if keyword.lower() in student_answer:
            score += weight
    print('Current Score:', score)


print(f'Your total score is {score}')


          
          
