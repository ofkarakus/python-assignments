# Problem :

# Task : Estimating the risk of death from coronavirus.

# Consider the following questions in terms of True/False regarding someone else.

# Are you a cigarette addict older than 75 years old? Variable → age

# Do you have a severe chronic disease? Variable → chronic

# Is your immune system too weak? Variable → immune

# Set a logical algorithm using boolean logic operators (and/or) and the given variables in order to 
# give us True (there is a risk of death) or False (there is not a risk of death) as a result.

age = True
chronic = False
immune = False

risk1 = not age or chronic and immune
risk2 = age and not chronic or immune
risk3 = age and chronic and immune

print(risk1, risk2, risk3, sep=', ')