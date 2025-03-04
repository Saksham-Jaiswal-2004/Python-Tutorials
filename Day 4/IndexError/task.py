states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_india = ["West Bengal", "Haryana", "Madhya Pradesh", "Assam", "Rajasthan", "Mumbai", "Delhi", "Goa", "Hyderabad", "Odisha"]

states = [states_of_america, states_of_india] #A nested list which contains two lists

num1 = len(states_of_america) #len() function gives the length of the given data type passed in its parameter
num2 = len(states_of_india) #len() function gives the length of the given data type passed in its parameter

print(num1, num2)
print(states)
