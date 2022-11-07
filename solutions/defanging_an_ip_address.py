class DefangingAnIpAddress:

    """
        O(n)
        Using string builtin method `.replace()`
    """
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

    """
        O(n)
    """
    def defangIpAddressManual(self, address: str) -> str:
        new_string = ''

        # we create a new string because strings are immutable
        for char in address:
            if char == '.':
                new_string += '[.]'
            else:
                new_string += char

        return new_string

if __name__ == '__main__':
    object = DefangingAnIpAddress()
    print(object.defangIPaddr('1.1.1.1'))
    print(object.defangIPaddr('255.100.50.0'))