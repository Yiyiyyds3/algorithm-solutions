from decimal import ROUND_HALF_UP, Decimal
n=int(input())
max_rate=Decimal(0)

nums=list(map(int,input().split()))
max_ai=nums[0]
for j in range(1,n):
    rate=Decimal(max_ai)/Decimal(nums[j])
    if rate>max_rate:
        max_rate=rate
    if nums[j]>max_ai:
        max_ai=nums[j]

max_a=max(Decimal(10),max_rate*Decimal(10))

result=max_a.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
print(result)