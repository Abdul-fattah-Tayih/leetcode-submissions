from typing import List

class GasStation:
    """
        134. Gas Station

        There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

        Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
    """
    def can_complete_circuit(self, gas: List[int], cost: List[int]) -> int:
        """
            O(n)

            Greedy solution

            In each iteration, we calculate the difference between gas and cost for the ith station

            If at any point the gas tank is < 0, then we simply try starting from the next station
        """
        if sum(gas) < sum(cost):
            return -1

        gas_tank = 0
        result = 0
        for station in range(len(gas)):
            gas_tank += (gas[station] - cost[station])
            
            if gas_tank < 0:
                gas_tank = 0
                result = station + 1

        return result

    def can_complete_circuit_brute_force(self, gas: List[int], cost: List[int]) -> int:
        """
            O(n^2) Brute force solution

            We loop over all stations, and subtract the cost of the gas station, we exit early if at any point the cost is greater than the current amount of gas

            Fails due to time constraints
        """

        for starting_station, starting_gas in enumerate(gas):
            gas_tank = starting_gas
            for current_station in range(starting_station, len(cost) + starting_station):
                current_station = current_station % len(cost)
                next_station = (current_station + 1) % len(cost)
                
                gas_tank = gas_tank - cost[current_station]

                if next_station == (starting_station % len(cost)):
                    if gas_tank >= 0:
                        return starting_station
                    break

                if gas_tank < 0:
                    break

                gas_tank += gas[next_station]

        return -1

if __name__ == '__main__':
    obj = GasStation()
    assert obj.can_complete_circuit([1,2,3,4,5],[3,4,5,1,2]) == 3
    assert obj.can_complete_circuit([2,3,4], [3,4,3]) == -1
