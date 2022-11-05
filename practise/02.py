#coding:utf-8
#创建Exercise运动类,包含对象属性name,time
#创建列表exercises
#根据Exercise类创建三个对象存储到列表中
#循环遍历列表，在控制台显示对应的运动与运动时间
class Exercise():
    def __init__(self,name,time):
        self.name = name
        self.time = time
exercises = [Exercise('瑜伽','30min'),Exercise('爵士舞','45min'),Exercise('动感单车','50min')]
for i in range(len(exercises)) :
    print(exercises[i].name+'运动了'+exercises[i].time)
