url = input()
ans = url[0]

for i in range(1,len(url)):
    if(url[i] == '/' and url[i-1] == '/'):
        continue
    else:
        ans+= url[i]

print(ans)