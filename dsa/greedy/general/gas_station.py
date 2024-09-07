def canCompleteCircuit(gas, cost):
    total_gas, total_cost = sum(gas), sum(cost)

    # If total gas is less than total cost, no solution exists
    if total_gas < total_cost:
        return -1

    start, tank = 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        # If we can't reach the next station, reset the start point
        if tank < 0:
            start = i + 1
            tank = 0

    return start
