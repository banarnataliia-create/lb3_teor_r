import math

def analyze_lottery(name, x1, x2, p=0.5, a=0.1):
    x_mean = p * x1 + (1 - p) * x2
    
    u_x1 = a * (x1 ** 2)
    u_x2 = a * (x2 ** 2)
    m_u = p * u_x1 + (1 - p) * u_x2
    
    x_eq = math.sqrt(m_u / a)
    
    pi_risk = x_mean - x_eq
    
    print(f"--- {name} ---")
    print(f"Сподіваний виграш (x̄): {x_mean:.2f}")
    print(f"Сподівана корисність (M(U(X))): {m_u:.2f}")
    print(f"Детермінований еквівалент (x̂): {x_eq:.2f}")
    print(f"Премія за ризик (π(X)): {pi_risk:.2f}\n")
    
    return m_u, pi_risk, x_eq > x_mean

m_u1, pi1, risk_prone1 = analyze_lottery("Лотерея L1(0; 0.5; 20)", 0, 20)
m_u2, pi2, risk_prone2 = analyze_lottery("Лотерея L2(10; 0.5; 30)", 10, 30)

print("=== ВИСНОВКИ ===")
chosen_lottery = "L2" if m_u2 > m_u1 else "L1"
print(f"1. Особа обере лотерею {chosen_lottery}, оскільки її сподівана корисність більша ({max(m_u1, m_u2):.2f} > {min(m_u1, m_u2):.2f}).")

if risk_prone1 and risk_prone2:
    print("2. Особа є СХИЛЬНОЮ до ризику, тому що детермінований еквівалент перевищує сподіваний виграш (x̂ > x̄), а премія за ризик від'ємна (π(X) < 0).")