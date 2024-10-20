class ParsingABooleanExpression:
    """
        1106. Parsing A Boolean Expression

        A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

        - 't' that evaluates to true.
        - 'f' that evaluates to false.
        - '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
        - '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
        - '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
        
        Given a string expression that represents a boolean expression, return the evaluation of that expression.

        It is guaranteed that the given expression is valid and follows the given rules.
    """
    def parseBoolExpr(self, expression: str) -> bool:
        """
            Recursive solution

            - Time complexity: O(n) 97% faster than other solutions
            - Space complexity: O(n)

            The idea behind this solution is to go over the characters in the string and:
            - If the character is a logical operation (which is &, | or !), we start an expression evaluation until we reach a ')'
            - use the logical operation to run the operation
            - evaluate each coming element to either true or false (keep going if you find commas)
            - if we've just finished evaluating an expression, we're going to backtrack to the previous call,
                and to avoid recalculation, we start at the end of the previous expression
        """
        def parse_value(value: str) -> bool:
            if value == 't':
                return True
        
            return False

        def bfs(sign, i) -> tuple[bool, int]:
            if i >= len(expression):
                return False, i

            result = None
            while i < len(expression) and expression[i] != ')':
                if expression[i] == ',':
                    i += 1
                    continue
                
                current_expression = None
                if expression[i] in ('&', '|', '!'):
                    current_expression, i = bfs(expression[i], i + 2)

                if result is None:
                    if current_expression:
                        result = current_expression
                    else:
                        result = parse_value(expression[i])

                if not current_expression:
                    current_expression = parse_value(expression[i])

                if sign == '|':
                    result = result or current_expression
                elif sign == '&':
                    result = result and current_expression
                elif sign == '!':
                    result = not current_expression

                i += 1

            return (result, i)

        return bfs("", 0)[0]
    
if __name__ == '__main__':
    obj = ParsingABooleanExpression()
    print(obj.parseBoolExpr("&(|(f))"))
    print(obj.parseBoolExpr("|(f,f,f,t)"))
    print(obj.parseBoolExpr("!(&(f,t))"))
    print(obj.parseBoolExpr("&(t,t,|(f,t),t)"))
    print(obj.parseBoolExpr("&(t,t,|(f,t),&(t),f)"))