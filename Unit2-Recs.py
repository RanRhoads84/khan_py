import time

# Program that takes the input of a student's grade and favorite subject
# and recommends subjects to study

# define the subject dictonaries

ele_dict_math = {
    01: "Arithmetic",
    02: "Fractions and Decimals",
    03: "Basic Geometry",
    04: "Introduction to Algebra",
    05: "Basic Measurement",
    06: "Intro to Probability and Statistics",
    07: "Basic Number Theory",
    08: "Algebra I",
    09: "Algebra II",
    10: "Geometry",
    11: "Trigonometry",
    12: "Precalculus",
    13: "Probability and Statistics",
    14: "Discrete Mathematics",
    15: "Mathematical Modeling"
}
ele_dict_science = {
    01: "General Science (Basic observation, scientific method)",
    02: "Life Science (Plants, animals, ecosystems, human body basics)",
    03: "Earth Science (Weather, rocks/minerals, planets, natural resources)",
    04: "Physical Science (motion, forces, matter, energy)",
    05: "Environmental Science (Conservation, pollution, recycling)",
    06: "Biology (Cells, genetics, evolution, ecology, human anatomy)",
    07: "Chemistry (Atoms, reactions, periodic table, stoichiometry)",
    08: "Earth Science/Geology",
    09: "Basic Environmental Science",
    10: "Intro to Anatomy",
    11: "Intro to Astronomy",
    12: "Intro to Physiology",
    13: "Intro to Physics"
}
ele_dict_arts_human = {
    01: "Reading and Basic Literature",
    02: "Writing (Basic Composition and Grammar)",
    03: "Art (Drawing, Painting, Crafts)",
    04: "Music (Singing, Basic Instruments)",
    05: "Social Studies (Introductory History, Geography, Civics)",
    06: "Drama and Performance Arts (Basic Theater)",
    07: "Literature (American, British, World)",
    08: "Advanced Composition and Writing (Essays, Creative Writing)",
    09: "History (U.S. History, World History)",
    10: "Geography (Human and Physical Geography)",
    11: "Civics and Government (Introduction to Political Systems)",
    12: "Visual Arts (Painting, Drawing, Sculpture, Photography)",
    13: "Music (Band, Orchestra, Choir, Music Theory)",
    14: "Performing Arts (Drama, Theater Production, Dance)",
    15: "Foreign Languages (Introductory to Intermediate levels)",
    16: "Philosophy (Introductory Ethics, Logic)"
}
uni_math = {
    01: "Calculus",
    02: "Linear Algebra",
    03: "Differential Equations",
    04: "Advanced Probability and Statistics",
    05: "Abstract Algebra",
    06: "Real Analysis",
    07: "Complex Analysis",
    08: "Topology",
    09: "Numerical Analysis",
    10: "Discrete Mathematics",
    11: "Mathematical Logic",
    12: "Mathematical Modeling and Optimization"
}
uni_science = {
    01: "Biology",
    02: "Chemistry",
    03: "Physics",
    04: "Geosciences",
    05: "Environmental Sciences",
    06: "Astronomy",
    07: "Geology",
    08: "Oceanography",
    09: "Meteorology",
    10: "Ecology"
}
uni_arts_human = {
    01: "Literature (Comparative Literature, Literary Criticism, Advanced Literary Theory)",
    02: "Philosophy (Ethics, Metaphysics, Epistemology, Advanced Logic)",
    03: "History (Specialized Areas: Medieval, Modern, Intellectual, Cultural, etc.)",
    04: "Fine Arts (Advanced Studio Art, Art History, Digital Arts)",
    05: "Performing Arts (Theater, Dance, Advanced Acting Techniques, Film Studies)",
    06: "Music (Musicology, Composition, Advanced Performance)",
    07: "Foreign Languages and Literature",
    08: "Religious Studies/Theology",
    09: "Cultural Studies and Anthropology (Humanities-focused)",
    10: "Classics (Ancient Languages, Literature, History)",
}

ele_dicts = {
    'mat':"ele_dict_mat",
    'sci':"ele_dict_sci",
    'art':"ele_dict_art"
}
uni_dicts = {
    "mat":"uni_dict_mat",
    "sci":"uni_dict_sci",
    "art":"uni_dict_art"
}


subject = []
grade = 0
uni_yr = 0

print('Welcome to the class recomendation bot!')
time.sleep(2)
print('Given your grade or college year I recommend classes for your favorite subject!\n')
time.sleep(2)
print('Subjects are: Math, Science, and Art/Humanities.\n')

# Takes subject input and stores it as the subject variable
input('What is your favorite subject?\n').strip().lower()[:3]
subject == input
print('Execllent Choice!')
print(subject)

dict.keys(subject)






# Function to set the dictonary for the favorite subject
def grade():
    input('Are you in Uni? (yes/no)\n').strip().lower()[:1]
    if input == "y":
        uni_yr = int(input('What year are you in?'))
        print(uni_yr)
    else:
        print("You'll be there soon enough!")
    input("What grade are you in?\n")
    if input == "k":
        grade == 1
    else:
        input == grade
        print(grade)