fruit = {'peach':'복숭아','orange':'오렌지','apple':'사과',
       'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}
answer=0
wrong=0
#영어 단어장 프로그램
#복숭아 영어로 입력하시오.
for f in fruit:
    eng_in =input('{}를 영어로 입력하시오. >> '.format(fruit[f]))
    #프로그램 하시오.
    if eng_in==f:
        answer+=1
        print('정답입니다.')
        print('입력한 단어: {}'.format(eng_in))
    else:
        wrong+=1
        print('오답입니다.')
print('[ 문제 체크 ]')
print('총 문제:',len(fruit))
print('정답:',answer)
print('오답:',wrong)
# for f in fruit:
#     print('키: ',f, 'value: ',fruit[f])
    