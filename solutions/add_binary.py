from math import remainder


class AddBinary:
    def addBinary(self, a: str, b: str) -> str:
        result = self.convert_binary_to_int(a) + self.convert_binary_to_int(b)

        return self.convert_int_to_binary(result)

    def convert_binary_to_int(self, binary: str) -> int:
        power_of_two = len(binary) - 1
        int_value = 0

        for character in binary:
            int_value += int(character) * (2 ** power_of_two)
            power_of_two -= 1

        return int_value

    def convert_int_to_binary(self, integer: int) -> str:
        B_Number = 0
        exponent = 0
        while (integer != 0):
            remainder = integer % 2
            c = pow(10, exponent)
            B_Number += remainder * c
            integer //= 2
            
            exponent += 1
        
        return str(B_Number)

if __name__ == '__main__':
    solution = AddBinary()
    print(solution.addBinary('11', '1')) # should be 100 (4)
    print(solution.addBinary('1010', '1011')) # should be 10101 (21)