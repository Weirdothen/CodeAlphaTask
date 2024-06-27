def generate_fibonacci_sequence(n_terms):

    fib_term1 = 0

    fib_term2 = 1

    fibonacci_sequence = []


    if n_terms <= 0:

        return "Number of terms must be a positive integer."

    for _ in range(n_terms):

        fibonacci_sequence.append(fib_term1)

        next_term = fib_term1 + fib_term2

        fib_term1 = fib_term2

        fib_term2 = next_term

    return fibonacci_sequence

