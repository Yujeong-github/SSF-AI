input_data=5
weight=3
target=8
learning_rate=0.1
pred=weight*input_data


error=pred-target #계산후 제곱하므로 순서 상관없음,오류계산
print("original error:",error)

slope=2*input_data*error #기울기 계산
print("slope:",slope)

new_weight=weight-learning_rate*slope #새로운 가중치 업데이트
print("new weight:",new_weight)

new_pred=new_weight*input_data #새로운 가중치로 새로운 예측값
print("new prediction:",new_pred)

new_error=new_pred-target #새로운 오류 계산
print("new error:",new_error)