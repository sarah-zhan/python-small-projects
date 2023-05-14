student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

#Create an empty dictionary called student_grades.
student_grades = {}

#add the grades to student_grades.
for name in student_scores:
  score = student_scores[name]
  if score > 90:
    student_grades[name] = 'Outstanding'
  elif score > 80:
    student_grades[name] = 'Exceeds Expectations'
  elif score > 70:
    student_grades[name] = 'Acceptable'
  else:
    student_grades[name] = 'Fail'

print(student_grades)


#########################################################
#dictionary in list

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
  add_on = {}
  add_on['country'] = country
  add_on['visits'] = visits
  add_on['cities'] = cities
  travel_log.append(add_on)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#########################################################
#blind auction

from replit import clear
from art import logo

print(logo)
print('Welcome to the secret auction program. ')

bids = {}

def winner(biddings):
  max = 0
  win = ''
  for name in biddings:
    bidding = biddings[name]
    if bidding > max:
      max = bidding
      win = name
  print(f'The winner is {win} with a bid of ${max}.')

game = True
while game:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bids[name] = bid
  clear()
  game_continued = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  if game_continued == 'no':
    game = False
    winner(bids)


