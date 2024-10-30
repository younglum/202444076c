
class Score:
    def __init__(self,k,m,e):  #_ 2개가 붙어있는 함수들은 magic method(매직 매소드)라고 함
        self.kor=k
        self.mat=m
        self.eng=e

    def average(self):  #사용자가 선언한 method, 사용시 Score 때 선언한 값이 들어가야 함
        return (self.kor+self.mat+self.eng)/3
    
score3=Score(10,20,30)    #Score(10,20,30) 자체가 self에 들어감
print(score3.kor,score3.mat)
print(score3.average())
score3.kor=100
print(score3.kor,score3.mat)
print(score3.average())


scores1=[10,20,30]
scores2={"k":10,"e":20,"m":30}
def average_list(datas):
    return sum(datas)/len(datas)

def average_dict(datas):
    return sum(datas.values())/len(datas)

print(average_list(scores1))
print(average_dict(scores2))
