#
# * Python 42, Correct Scholarships
# * Easy

# * For the upcoming academic year the Coolcoders University should decide which 
# * students will get the scholarships. Scholarships are considered to be correctly 
# * distributed if all best students have it, but not all students in the university 
# * do. Obviously, only university students should be able to get a scholarship, 
# * i.e. there should be no outsiders in the list of the students that will get 
# * a scholarships.

# * You are given lists of unique student ids bestStudents, scholarships and 
# * allStudents, representing ids of the best students, students that will get a 
# * scholarship and all the students in the university, respectively. Return true 
# * if the scholarships are correctly distributed and false otherwise.

# * Example

#     For bestStudents = [3, 5], scholarships = [3, 5, 7], and
#     allStudents = [1, 2, 3, 4, 5, 6, 7], the output should be
#     correctScholarships(bestStudents, scholarships, allStudents) = true;

#     For bestStudents = [3, 5], scholarships = [3, 5], and
#     allStudents = [3, 5], the output should be
#     correctScholarships(bestStudents, scholarships, allStudents) = false.

#     All students get a scholarship, which is not correct.

#     For bestStudents = [3], scholarships = [1, 3, 5], and
#     allStudents = [1, 2, 3], the output should be
#     correctScholarships(bestStudents, scholarships, allStudents) = false.

#     There's no student with id 5, yet somehow he managed to get a scholarship.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.integer bestStudents

#     Array of unique elements representing ids of the best students in the university. It is guaranteed that all bestStudents are present in allStudents.

#     Guaranteed constraints:
#     0 ≤ bestStudents.length ≤ 30,
#     1 ≤ bestStudents[i] ≤ 1000.

#     [input] array.integer scholarships

#     Array of unique elements representing ids of the students that will get a scholarship.

#     Guaranteed constraints:
#     0 ≤ scholarships.length ≤ 30,
#     1 ≤ scholarships[i] ≤ 1000.

#     [input] array.integer allStudents

#     Array of unique elements representing ids of the students that will get a scholarship.

#     Guaranteed constraints:
#     0 ≤ allStudents.length ≤ 30,
#     1 ≤ allStudents[i] ≤ 1000.

#     [output] boolean

#     true if the scholarships are correctly distributed and false otherwise.

#%%

# * Solution 1
def correctScholarships1(bestStudents, scholarships, allStudents):
    return all(x in scholarships for x in bestStudents) and all(x in allStudents for x in scholarships) and len(scholarships) < len(allStudents)



# * Solution 2
# ! Set Operations
def correctScholarships2(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)



bs = [3,5]
s = [3, 5, 7]
as1 = [1, 2, 3, 4, 5, 6, 7]
r1 = correctScholarships1(bs, s, as1)
print(r1)

# %%
