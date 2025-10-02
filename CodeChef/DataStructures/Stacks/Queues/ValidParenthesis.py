# cook your dish here
def check(s):
    st = []
    for i in s:
        if i == ")":
            if st and st[-1] == "(":
                st.pop()
            else:
                return False
        else:
            st.append(i)
    if st:
        return False
    return True


for t in range(int(input())):
    s = input()
    if check(s):
        print(1)
    else:
        print(0)
