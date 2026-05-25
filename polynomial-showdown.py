def solve_poly(coeffs):
    # coeffs is a list of 9 integers, from degree 8 down to 0
    terms = []
    for i, c in enumerate(coeffs):
        deg = 8 - i
        if c == 0:
            continue
        
        # Determine sign and absolute value
        is_negative = c < 0
        abs_c = abs(c)
        
        # Determine coefficient string
        if deg == 0:
            coeff_str = str(abs_c)
        else:
            if abs_c == 1:
                coeff_str = ""
            else:
                coeff_str = str(abs_c)
        
        # Determine variable string
        if deg == 0:
            var_str = ""
        elif deg == 1:
            var_str = "x"
        else:
            var_str = f"x^{deg}"
            
        term_str = coeff_str + var_str
        terms.append((is_negative, term_str))
        
    if not terms:
        return "0"
        
    res = ""
    for i, (is_neg, t_str) in enumerate(terms):
        if i == 0:
            if is_neg:
                res += "-" + t_str
            else:
                res += t_str
        else:
            if is_neg:
                res += " - " + t_str
            else:
                res += " + " + t_str
    return res

print(solve_poly([0, 0, 0, 1, 22, -333, 0, 1, -1]))
print(solve_poly([0, 0, 0, 0, 0, 0, -55, 5, 0]))