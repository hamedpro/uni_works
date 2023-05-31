def fibonachi_number(n):
    if(n == 1 or n== 2) : 
        return 1
    else:
        return fibonachi_number(n-1) + fibonachi_number(n-2)
entered_number = int(input())
print(fibonachi_number(entered_number))