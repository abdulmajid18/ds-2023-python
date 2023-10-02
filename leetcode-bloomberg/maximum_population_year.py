def maxi_population(logs):
    events = []

    # Create events for births and deaths.
    for birth, death in logs:
        events.append((birth, 1))  # 1 represents a birth event
        events.append((death, -1))  # -1 represents a death event

    events.sort()  # Sort events based on the year.

    current_population = 0
    max_population = 0
    max_year = -1

    for year, event in events:
        current_population += event  # Update population based on birth or death event.

        if current_population > max_population:
            max_population = current_population
            max_year = year

    return max_year