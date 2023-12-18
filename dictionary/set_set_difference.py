morning = {"Java", "C", "Ruby", "Lisp", "C#"}
afternoon = {"Python", "C#", "Java", "C", "Ruby" }

p = list(afternoon)
# possible_courses = morning ^ afternoon
possible_courses = morning.symmetric_difference(p)
print(possible_courses)

m = list(morning)
print(m)

p = list(afternoon)

po = set()