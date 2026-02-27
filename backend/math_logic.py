import re

class MathSolver:
    @staticmethod
    def get_lcm(a: int, b: int):
        import math
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def get_hcf(a: int, b: int):
        import math
        return math.gcd(a, b)

    @staticmethod
    def solve_expression(expression: str):
        """
        Parses a string expression (e.g., '12 + 5') and returns the result.
        Supports: +, -, *, /, LCM, HCF.
        """
        expression = expression.lower().replace('x', '*').replace('=', '').strip()
        
        # LCM/HCF detection
        lcm_match = re.search(r'lcm\s*\(?(\d+)\s*,\s*(\d+)\)?', expression)
        if lcm_match:
            return MathSolver.get_lcm(int(lcm_match.group(1)), int(lcm_match.group(2)))
        
        hcf_match = re.search(r'hcf\s*\(?(\d+)\s*,\s*(\d+)\)?', expression)
        if hcf_match:
            return MathSolver.get_hcf(int(hcf_match.group(1)), int(hcf_match.group(2)))

        # Simple arithmetic
        try:
            # Clean expression for eval (only allow numbers and operators)
            clean_expr = re.sub(r'[^0-9+\-*/.]', '', expression)
            if clean_expr:
                return eval(clean_expr)
        except Exception:
            pass

        return None

    @staticmethod
    def verify_answer(problem: str, student_answer: float):
        correct_answer = MathSolver.solve_expression(problem)
        if correct_answer is None:
            return False, "Could not solve problem"
        
        is_correct = abs(correct_answer - student_answer) < 1e-9
        return is_correct, correct_answer
