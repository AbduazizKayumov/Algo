import random


# Suppose that you need to hire a new office assistant
# You have N candidates and you need to interview them one by one daily
# After each interview, if the candidate is better than the current assistant
# you decide to hire the newly interviewed candidate
# Interviewing has a low cost, whereas hiring is expensive since on each hiring
# you need to give an employment package


def interview(candidate):
    return candidate ** 2


def hire(candidate):
    return candidate


# if the candidates come in an increasing order
# the overall cost would be very expensive because
# you are basically hiring a new assistant after each interview
def hire_assistant(candidates):
    cost = 0
    best = 0
    for candidate in candidates:
        feedback = interview(candidate)
        if feedback > best:
            employment_package = hire(candidate)
            cost += employment_package
            best = feedback
    return cost


# Candidates are hired approx. lnn times:
# the probability that ith candidate will be hired: 1 / i
# the overall expected hires:
# E[hires] = 1/1 + 1/2 + 1/3 + ... + 1/n ≈ lnn
def randomized_hire_assistant(candidates):
    # randomly permute the candidates
    random.shuffle(candidates)
    return hire_assistant(candidates)


candidates = []
for i in range(10, 100):
    candidates.append(i)
overall_cost = hire_assistant(candidates)
print("Overall cost = ", overall_cost)

overall_cost = randomized_hire_assistant(candidates)
print("Overall cost = ", overall_cost)
