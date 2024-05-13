#지폐 교환기
money=int(input('금액을 입력하세요 >> '))
오만=money//50000
만=(money%50000)//10000
오천=((money%50000)%10000)//5000
천=(((money%50000)%10000)%5000)//1000

print('금액: {:,}'.format(money))
print('오만원: {}\n만원: {}\n오천원: {}\n천원: {}'.format(오만,만,오천,천))

money=245678000
print('{:,}'.format(money))
