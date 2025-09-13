import numpy as np

def simulate_fair_dice_rolls(sides=6, rolls=100000):
    """Simulate rolling a fair dice and return results as a numpy array."""
    return np.random.choice(np.arange(1, sides + 1), size=rolls)

def calculate_statistics(data):
    """Return mean, variance of given numpy array."""
    mean = np.mean(data)
    variance = np.var(data)
    return round(mean, 3), round(variance, 3)

def simulate_sum_of_two_dice(sides=6, rolls=100000, probabilities=None):
    """Simulate rolling two dice and summing the results."""
    dice = np.arange(1, sides + 1)
    d1 = np.random.choice(dice, size=rolls, p=probabilities)
    d2 = np.random.choice(dice, size=rolls, p=probabilities)
    sum_throws = d1 + d2
    return sum_throws

def probability_mass_function(data):
    """Return empirical PMF from simulated data."""
    values, counts = np.unique(data, return_counts=True)
    pmf = {int(v): round(c/len(data), 3) for v, c in zip(values, counts)}
    return pmf

def theoretical_pmf_two_dice(sides=6, probabilities=None):
    """Compute exact PMF for sum of two dice."""
    dice = np.arange(1, sides + 1)
    if probabilities is None:
        probabilities = np.ones(sides)/sides
    pmf = {s: 0 for s in range(2, 2*sides + 1)}
    for a, pa in zip(dice, probabilities):
        for b, pb in zip(dice, probabilities):
            pmf[a+b] += pa * pb
    return {k: round(v, 3) for k, v in pmf.items()}

def cumulative_probability(pmf):
    """Return cumulative probabilities given a PMF dict."""
    sums = sorted(pmf.keys())
    cum_probs = np.cumsum([pmf[s] for s in sums])
    return dict(zip(sums, np.round(cum_probs, 3)))

