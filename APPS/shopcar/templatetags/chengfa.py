"""
1> 语法格式
2> 内置过滤器
3>自定义过滤器
1>在app下新建一个templatetags的文件夹
2>在该文件下新建一个py文件
3> 实例化注册器  register = template.Library()
4> 声明过滤器(过滤器的本质是一个函数)
5> 注册过滤器 @register.filter
6> 可以在模板中使用
6.1> 在需要自定义的过滤器的模板中  {% load chengfa %}
6.2>
"""
from django import template

# 实例化注册器 (规定格式)
register = template.Library()


# value1|chengfa:value2
@register.filter
def chengfa(value1, value2):
    return value1 * value2
# 如果前端接收数据是通过{% for ** in**s%}遍历得到的
# 变量传值格式是  {{ **.##|chengfa:**.### }}
