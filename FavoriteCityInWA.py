# List of cities in Washington
cities = ['Seattle', 'Spokane', 'Tacoma', 'Bellevue']

# Dictionary to store votes
votes = {'Seattle': 0, 'Spokane': 0, 'Tacoma': 0, 'Bellevue': 0}

# Function to display the list of cities
def display_cities():
    print("Vote for your favorite city in Washington:")
    for city in cities:
        print(city)

# Function to cast a vote
def cast_vote():
    choice = input("What is your favorite city in washington?: ")
    if choice in votes:
        votes[choice] += 1
        print("Thank you for your vote!")
    else:
        print("Invalid choice. Please choose a valid city.")

# Function to display the results
def display_results():
    print("Voting Results:")
    for city, count in votes.items():
        print(f"{city}: {count} vote(s)")

for _ in range(5):  
    display_cities()
    cast_vote()

display_results()
