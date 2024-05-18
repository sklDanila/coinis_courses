# Napisati program koji na osnovu varijabli a, pre, sub i num dodaje prefiks pre, i sufiks suf
# stringu a num puta i vraća novi prošireni string.
# Input 1: a = ‘test’, pre = ‘pr’, suf = ‘su’, num = 2;
# Output 1: ‘prprtestsusu’


def task_52():
    a = input("Enter the string: ")
    pre = input("Enter the prefix: ")
    suf = input("Enter the suffix: ")
    num = int(input("Enter the number of times to repeat the frefix and suffix: "))

    a = pre * num + a + suf * num
    print(a)


task_52()
