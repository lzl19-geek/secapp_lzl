from django import forms

TOPIC_CHOICES = (
    # 下拉列表
    ('信息技术学院', "信息技术学院"),
    ('机电学院', "机电学院"),
    ('职业技术学院', "职业技术学院"),
    ('外国语学院', "外国语学院"),
    ('商学院', "商学院"),
)

RADIO_CHOICES = (
    #单选列表
            ('男', "男"),
            ('女', "女"),
    )

class PersonForm(forms.Form):
    name = forms.CharField(label='你的名字', max_length=20)
    num = forms.CharField(label='你的学号', max_length=20)
    phone = forms.CharField(label='联系方式', max_length=20)
    academy = forms.ChoiceField(label='你的学院', choices=TOPIC_CHOICES) #下拉列表
    sex= forms.ChoiceField(label='你的性别',widget=forms.RadioSelect, choices=RADIO_CHOICES) #单选
    subject = forms.CharField(label='你的专业', max_length=20)