import time  # to add a delay for print statements

# Program that takes the input of a student's grade and favorite subject
# and recommends subjects to study


# define the subject dictonaries
ele_math = {
    1: "Numbers and Counting",
    2: "Arithmetic",
    3: "Basic Geometry",
    4: "Basic Measurement",
    5: "Fractions and Decimals",
    6: "Introduction to Algebra",
    7: "Algebra I",
    8: "Geometry",
    9: "Algebra II",
    10: "Precalculus",
    11: "Trigonometry",
    12: "Basic Number Theory",
    13: "Intro to Probability and Statistics",
    14: "Intro to Physics"
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

# Introduction to the recomendation bot
print('Welcome to the class recomendation bot!')
print('Given your grade or college year I recommend classes for your favorite subject!\n')
time.sleep(1)  # Gives use a chance to read the intro
print('Subjects are: Math, Science, and Arts/Humanities.')

# Takes subject input and stores it as the subject variable'''
subject = input('What is your favorite subject?\n').strip().lower()[:3]
print('Execllent Choice!\n')

# Function to set the dictonary for the favorite subject and grade number


def ask_grade():
    # Sets the variable of being in college or not
    # and sets the year to determine class recommendations
    uni_answer = input(
        'Are you in College/University? (yes/no)\n').strip().lower()[:1]
    # Takes Year as input and sets which dictionary to use
    if uni_answer == "y":
        use_dict = uni_dicts.get(subject)
        grade_num = int(input('What year are you in? (1-4)\n'))
        # Pushes the variables out of the funtion and to the main program
        return use_dict, grade_num
    # If not in College, runs the else section to find the grade
    else:
        print("You'll be there soon enough!")
        # Takes grade as input and sets which dictionary to use
        grade = input("What grade are you in? (K-12):\n")
        if grade == "k":
            grade_num = 1
        else:
            grade_num = int(grade)
        use_dict = ele_dicts.get(subject)
        # Pushes the variables out of the funtion and to the main program
        return use_dict, grade_num


# Initializes the variables from the funtion
use_dict, grade_num = ask_grade()

# This will return a subject from the dict based on their grade/year input
# recommended = use_dict.get(grade_num)


# Because range is exclusive at the end, not inclusive, we have to use +3 in python.
# Key_range finds the range around the grade_num input
key_range = range(max(1, grade_num - 2), grade_num + 3)

# Runs a for loop to return the recommended classes around the grade/year input
# k = key. So the loop finds the key value, then sets the range (-2, +3) around the key and returns
# 5 recommended classes.
recommended_range = [use_dict.get(k)
                     for k in key_range if use_dict.get(k) is not None]

# Prints the 5 recommded classes for the users favorite subject,
# based on their education level
print("Recommended subjects in your range:")
for rec in recommended_range:
    print("-", rec)
