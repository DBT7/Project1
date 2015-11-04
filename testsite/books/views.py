from django.shortcuts import render

from django.http import HttpResponse, Http404
# Create your views here.
import MySQLdb



def book_list(request):
    db=MySQLdb.connect(user='root',db='test',host='localhost')
    
    cursor=db.cursor()
    
    cursor.execute('SELECT Title FROM example1 ORDER BY Title')
    
    names = [row[0] for row in cursor.fetchall()]
    
    db.close()
    
    return render(request,str(names))

def display_meta(request):
    values=request.META.items()
    values.sort()
    
    html=[]
    for k,v in values:
        html.append('<tr><td>%s</td>n<td>%s</td></tr></br>' % (k,v))
    return HttpResponse(html)