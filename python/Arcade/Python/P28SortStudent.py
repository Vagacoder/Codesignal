#
# * Python 28, Sort Student
# * Easy

# * You are given a list of students who want to apply to the internship at 
# * CodeSignal. For the ith student you know their full name students[i], which 
# * can consist of up to 5 words (where a word is a set of consecutive letters). 
# * It is guaranteed that the surname is always the last name of student's full 
# * name.

# * Your task is to sort the students lexicographically by their surnames. If two 
# * students happen to have the same surname, their order in the result should be 
# * the same as in the original list.

# * Example

# For

# students = ["John Smith", "Jacky Mon Simonoff", 
#             "Lucy Smith", "Angela Zimonova"]

# the output should be

# sortStudents(students) = ["Jacky Mon Simonoff", "John Smith", 
#                           "Lucy Smith", "Angela Zimonova"]

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string students

#     Array of students, where each student is given by their full name consisting of at most 5 words. For each i students[i] consists of English letters and whitespace (' ') characters.

#     Guaranteed constraints:
#     1 ≤ students.length ≤ 30,
#     1 ≤ students[i].length ≤ 50.

#     [output] array.string

#     Array of students sorted as described above.

#%%

# * Solution 1
def sortStudents(students:list)-> list:
    students.sort(key=lambda student: student.split(' ')[-1])
    return students


a1 = ["John Smith", "Jacky Mon Simonoff", "Lucy Smith", "Angela Zimonova"]
r1 = sortStudents(a1)
print(r1)



# %%
