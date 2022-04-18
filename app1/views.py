from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from app1.forms import PersonForm
def index(request):
    name = '数字媒体专业19数媒 刘章乐1922987'
    return render(request, 'index.html', {"name": name})

def get_massage(request):
    if request.method=='POST':
        form=PersonForm(request.POST) #点击提交后，将post请求中的页面数据放到personform中
        print(form)
        if form.is_valid(): #判断输入数据是否通过相关输入规则校验
            data=form.cleaned_data #获取输入的数据，存放到data
            print(data)
            name=data['name'] #获取姓名，学号....
            num=data['num']
            phone=data['phone']
            academy=data['academy']
            sex=data['sex']
            subject=data['subject']
            #将输入信息显示到massage页面
            return render(request,'massage.html',{"name":name,"num":num,"phone":phone,"academy":academy,"sex":sex,"subject":subject})
        else:
            return HttpResponseRedirect('/error/')
    else:
        return render(request,'login.html',{'form': PersonForm()})


