import generate

def q1(random):
    start = random.randint(0, 5)
    end = start + 1

    return f"""
    Evaluate the surface integral: \[ \iint_S xdS \]

    where $S$ is the part of the paraboloid $x = y^2 + z^2$ given by ${start} \leq x \leq {end}$.
    """

generate.generate(q1)