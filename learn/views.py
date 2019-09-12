# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import pymssql


def index(request):
    a = request.GET['a']
    s=a+'阿黄'
    return HttpResponse(s)


def test1(request):
    dct={}
    dct['txt1']='asdfasdfsadf阿sdf'
    dct['num']=8
    dct['dct']={'n1':'张三','n2':'李四'}
    return render(request, 'f1/test1.html',dct)

def test2(request):
    s=''
    s1=''
    dct={}
    list=[];
    connect = pymssql.connect('192.168.1.91', 'sa', 'rootroot', 'Catjc')  # 建立连接
    if connect:
        cursor = connect.cursor(as_dict=True)  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
        sql = "SELECT TOP 10 * FROM [Catjc].[dbo].[user_user]"
        cursor.execute(sql)  # 执行sql语句
        row = cursor.fetchone()  # 读取查询结果,
        while row:  # 循环读取所有结果
            list.append(row)
            row = cursor.fetchone()
    cursor.close()
    connect.close()
    dct['list']=list
    # dct['items']=list[0]
    return render(request, 'f1/test2.html',dct)
