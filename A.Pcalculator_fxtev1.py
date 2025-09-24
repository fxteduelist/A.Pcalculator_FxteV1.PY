# ap_calculator.py
def ap_nth_term(a, d, n):
    """Calculate nth term of AP: a + (n-1)*d"""
    return a + (n-1)*d

def ap_sum(n, a, d):
    """Calculate sum of first n terms: n/2 * (2a + (n-1)d)"""
    return n/2 * (2*a + (n-1)*d)

print("=== A.P  Calculator ===")
print("might upd later with more features -fxteduelist_")
while True:
    print("\nOptions:\n1. Find nth term\n2. Find sum of n terms\n3. Exit")
    choice = input("Choose option (1-3): ")
    if choice == '1':
        a = float(input("Enter first term a: "))
        d = float(input("Enter common difference d: "))
        n = int(input("Enter term number n: "))
        print(f"The {n}th term is: {ap_nth_term(a,d,n)}")
    elif choice == '2':
        a = float(input("Enter first term a: "))
        d = float(input("Enter common difference d: "))
        n = int(input("Enter number of terms n: "))
        print(f"The sum of first {n} terms is: {ap_sum(n,a,d)}")
    elif choice == '3':
        print("exit")
        break
    else:
        print("Invalid")