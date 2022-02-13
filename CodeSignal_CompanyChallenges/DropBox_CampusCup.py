from collections import defaultdict

def campusCup(emails):
  domains = defaultdict(int)
  for e in emails:
    name, domain = e.split('@')
    domains[domain] += 20
  for k, v in domains.items():
    if v < 100:
      v = 0
    elif v >= 100 and v < 200:
      v = 3
    elif v >= 200 and v < 300:
      v = 8
    elif v >= 300 and v < 500:
      v = 15
    else:
      v = 25
    domains[k] = v
    return [x[0] for x in sorted(domains.items(), key=lambda x:(-x[1], x[0]))]

print(campusCup(["b@harvard.edu","c@harvard.edu", "d@harvard.edu","e@harvard.edu", "f@harvard.edu","a@student.spbu.ru", "b@student.spbu.ru", "c@student.spbu.ru","d@student.spbu.ru", "e@student.spbu.ru", "f@student.spbu.ru","g@student.spbu.ru"]))

print(campusCup(["john.doe@mit.edu", "admin@rain.ifmo.ru", "noname@mit.edu"]))

print(campusCup(["a@rain.ifmo.ru", "b@rain.ifmo.ru","c@rain.ifmo.ru","d@rain.ifmo.ru", "e@rain.ifmo.ru","noname@mit.edu"]))