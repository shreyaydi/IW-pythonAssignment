# Write a Python program to sort a list of tuples using Lambda.
x = lambda dict: sorted(dict, key = lambda x: x['python'])
dict = [{'python':'django', 'javascript':'react', 'java':'maven',},{'python':'flask', 'javascript':'node', 'java':'jhipster'},{'python': 'cheerypy', 'javascript': 'angular', 'java':'guava'}]
print(x(dict))