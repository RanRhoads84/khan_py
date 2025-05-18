import time

# Program that takes the input of a student's grade and favorite subject
# and recommends subjects to study

# define the subject dictonaries

ele_math = {
    1: "Arithmetic",
    2: "Fractions and Decimals",
    3: "Basic Geometry",
    4: "Introduction to Algebra",
    5: "Basic Measurement",
    6: "Intro to Probability and Statistics",
    7: "Basic Number Theory",
    8: "Algebra I",
    9: "Algebra II",
    10: "Geometry",
    11: "Trigonometry",
    12: "Precalculus",
    13: "Probability and Statistics",
    14: "Discrete Mathematics",
    15: "Mathematical Modeling"
}
ele_sci = {
    1: "General Science (Basic observation, scientific method)",
    2: "Life Science (Plants, animals, ecosystems, human body basics)",
    3: "Earth Science (Weather, rocks/minerals, planets, natural resources)",
    4: "Physical Science (motion, forces, matter, energy)",
    5: "Environmental Science (Conservation, pollution, recycling)",
    6: "Biology (Cells, genetics, evolution, ecology, human anatomy)",
    7: "Chemistry (Atoms, reactions, periodic table, stoichiometry)",
    8: "Earth Science/Geology",
    9: "Basic Environmental Science",
    10: "Intro to Anatomy",
    11: "Intro to Astronomy",
    12: "Intro to Physiology",
    13: "Intro to Physics"
}
ele_arts = {
    1: "Reading and Basic Literature",
    2: "Writing (Basic Composition and Grammar)",
    3: "Art (Drawing, Painting, Crafts)",
    4: "Music (Singing, Basic Instruments)",
    5: "Social Studies (Introductory History, Geography, Civics)",
    6: "Drama and Performance Arts (Basic Theater)",
    7: "Literature (American, British, World)",
    8: "Advanced Composition and Writing (Essays, Creative Writing)",
    9: "History (U.S. History, World History)",
    10: "Geography (Human and Physical Geography)",
    11: "Civics and Government (Introduction to Political Systems)",
    12: "Visual Arts (Painting, Drawing, Sculpture, Photography)",
    13: "Music (Band, Orchestra, Choir, Music Theory)",
    14: "Performing Arts (Drama, Theater Production, Dance)",
    15: "Foreign Languages (Introductory to Intermediate levels)",
    16: "Philosophy (Introductory Ethics, Logic)"
}
uni_math = {
    1: "Calculus",
    2: "Linear Algebra",
    3: "Differential Equations",
    4: "Advanced Probability and Statistics",
    5: "Abstract Algebra",
    6: "Real Analysis",
    7: "Complex Analysis",
    8: "Topology",
    9: "Numerical Analysis",
    10: "Discrete Mathematics",
    11: "Mathematical Logic",
    12: "Mathematical Modeling and Optimization"
}
uni_sci = {
    1: "Biology",
    2: "Chemistry",
    3: "Physics",
    4: "Geosciences",
    5: "Environmental Sciences",
    6: "Astronomy",
    7: "Geology",
    8: "Oceanography",
    9: "Meteorology",
    10: "Ecology"
}
uni_arts = {
    1: "Literature (Comparative Literature, Literary Criticism, Advanced Literary Theory)",
    2: "Philosophy (Ethics, Metaphysics, Epistemology, Advanced Logic)",
    3: "History (Specialized Areas: Medieval, Modern, Intellectual, Cultural, etc.)",
    4: "Fine Arts (Advanced Studio Art, Art History, Digital Arts)",
    5: "Performing Arts (Theater, Dance, Advanced Acting Techniques, Film Studies)",
    6: "Music (Musicology, Composition, Advanced Performance)",
    7: "Foreign Languages and Literature",
    8: "Religious Studies/Theology",
    9: "Cultural Studies and Anthropology (Humanities-focused)",
    10: "Classics (Ancient Languages, Literature, History)",
}

ele_dicts = {
    'mat': ele_math,
    'sci': ele_sci,
    'art': ele_arts
}
uni_dicts = {
    "mat": uni_math,
    "sci": uni_sci,
    "art": uni_arts
}


# subject = []
# grade = 0
# uni_yr = 0

'''print('Welcome to the class recomendation bot!')
print('Given your grade or college year I recommend classes for your favorite subject!\n')
time.sleep(2)
print('Subjects are: Math, Science, and Arts/Humanities.')

# Takes subject input and stores it as the subject variable'''
subject = input('What is your favorite subject?\n').strip().lower()[:3]

print('Execllent Choice!\n')
print(subject)

# Function to set the dictonary for the favorite subject


def ask_grade():
    uni_answer = input('Are you in Uni? (yes/no)\n').strip().lower()[:1]
    if uni_answer == "y":
        use_dict = uni_dicts.get(subject)
        grade_num = int(input('What year are you in?'))
        return use_dict, grade_num

    else:
        print("You'll be there soon enough!")
        grade = input("What grade are you in? (K-12):\n")
        if grade == "k":
            grade_num = 1
        else:
            grade_num = int(grade)
        use_dict = ele_dicts.get(subject)
        return grade_num


use_dict, grade_num = ask_grade()
recommended = use_dict.get(grade_num)

ask_grade()
print(recommended)
# print(subject)
# print(grade_num)
# print(recommended)
