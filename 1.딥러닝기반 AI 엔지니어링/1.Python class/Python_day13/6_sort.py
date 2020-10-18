#bubble sort
#가장 기본적인 정렬
#두가지 요소를 비교함
#오름차순 또는 내림차순이 아닐경우 교체를 기반으로하는 간단한 정렬 알고리즘

# 단점: 데이터가 엄~~청 많은 경우 너무 오래걸림...


data = [15,20,31,20,30,23,212, 32]

for p in range(len(data)-1,0,-1):
    # print(p) #4 3 2 1
    # 총 길이가 7인경우
    # 가장 큰 값은 data[6]으로 
    # 그다음 가장 큰 값은 data[5]로
    #                   .
    #                   .
    #                   .
    # 결국 가장 작은 값이 data[0]으로 들어오면서 bubble sorting 완료
    for i in range(p):
        # 4  0
        # 4  1
        # 4  2
        # 4  3
        # 3  0
        # 3  1
        # 3  2
        # 2  0
        # 2  1
        # 1  0
        if data[i] > data[i+1]: 
            #비교
            #0>1,1>2,2>3,3>4
            #0>1,1>2,2>3
            #0>1,1>2
            #0>1 
            temp = data[i] #더 큰값을 임시 저장
            data[i]=data[i+1] #큰값을 지우고 작은값을 넣어줌 
            data[i+1] = temp #더 큰값으로 교환 완료
        print(p, '', i)


print(data) #bubble sorting 됨

