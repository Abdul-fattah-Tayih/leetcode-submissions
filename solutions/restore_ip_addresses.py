from typing import List

class RestoreIpAddresses:
    """
        93. Restore IP Addresses

        A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

        For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

        Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
        
        You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
    """
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        return self.recursively_find_addresses(s, 0, '', 0, [])
    
    def recursively_find_addresses(self, s: str, i: int, current_ip: str, dots: int, solutions: List[str]) -> List[str]:
        if dots == 4 and i == len(s):
            solutions.append(current_ip[:-1])
            return solutions
        
        if dots > 4:
            return []

        for j in range(i, min(i + 3, len(s))):
            current_substring = s[i:j+1]
            if int(current_substring) <= 255 and (i == j or s[i] != '0'):
                self.recursively_find_addresses(s, j + 1, f'{current_ip}{current_substring}.', dots + 1, solutions)

        return solutions


if __name__ == '__main__':
    obj = RestoreIpAddresses()

    assert obj.restoreIpAddresses("25525511135") == ["255.255.11.135","255.255.111.35"]