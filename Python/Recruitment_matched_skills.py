# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:08:00 2023

@author: erenz
"""

job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
candidate_skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
"""
The expression list(job_skills & candidate_skills) forms a 
list by taking the intersection of the job_skills and candidate_skills 
sets. 
However, assuming that there might be multiple elements in this list, 
the [0] index is used to access the first element of the list.
"""
print(list(job_skills&candidate_skills)[0])

# Find the matched skills
matched_skills = job_skills.intersection(candidate_skills)

# Output the matched skills
print("Matched skills:")
for skill in matched_skills:
    print(skill)