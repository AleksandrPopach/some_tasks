# алгоритм Кнута - Морриса - Пратта по поиску подстроки в строке
def prefix_f(s):
    """ возвращает список с Пи - функциями (макс. собственный суффикс, являющийся префиксом) всех срезов строки
    """
    F = [0] * len(s)
    if s[0] == s[1]:
        F[1] = 1
    for i in range(2, len(s)):
        p = F[i - 1]
        while p > 0 and s[i] != s[p]:
            p = F[p - 1]
        if s[i] == s[p]:
            p += 1
        F[i] = p
    return F

s = 'aaabasaaahabakjabyahabasaa'
sub = 'aaa'
new = sub + '#' + s
result = prefix_f(new)
for i in range(len(result)):
    if result[i] == len(sub):
        ind = i - result[i] - len(sub)
        print(ind)  # индексы всех вхождений подстроки в строку
