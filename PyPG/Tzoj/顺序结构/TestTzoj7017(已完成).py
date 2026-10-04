s = int(input())
day=s // 86400
mouth = day // 30
year = mouth // 12
print(f"{1970+year} {(1+mouth)%12} {(1+day)%30}")