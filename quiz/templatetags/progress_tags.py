from django import template
from quiz.models import Progress
register = template.Library()

@register.simple_tag
def progress():
    a=[]
    f=Progress.objects.all()
    for i in range(0,len(f)):
        m=Progress.objects.all()[i]
        j=m.user
        a.append(j)
    return a
@register.simple_tag
def progress1():
    a=[]
    f=Progress.objects.all()
    for i in range(0,len(f)):
        m=Progress.objects.all()[i]
        j=m.score
        u=j[15]
        a.append(u)
    return a
@register.simple_tag
def progress2():
    a=[]
    f=Progress.objects.all()
    for i in range(0,len(f)):
        m=Progress.objects.all()[i]
        j=m.score
        u=j[17]
        a.append(u)
    return a
@register.simple_tag
def progress3():
    a=[]
    b=[]
    # c=[]
    # d=[]
    f=Progress.objects.all()
    for i in range(0,len(f)):
        m=Progress.objects.all()[i]
        j=m.user
        a.append(j)    
    for i in range(0,len(f)):
        m=Progress.objects.all()[i]
        j=m.score
        u=j[15]
        b.append(u)        
    # for i in range(0,len(f)):
    #     m=Progress.objects.all()[i]
    #     j=m.score
    #     u=j[17]
    #     c.append(u)   
# ==========================================percentage calculator================================
    # for i in range(0,len(f)):
    #     m=Progress.objects.all()[i]
    #     j=m.score
    #     p=int(j[15])
    #     u=int(j[17])
    #     y=(p/u)*100  
    #     z=round(y)
    #     r=str(z)
    #     d.append(r)
    # ============================================================
    try:     
        m=zip(b,a)
        q=sorted(m)
        s=[element for _, element in q]
        q=s[::-1]
        z=sorted(b)
        t=z[::-1]
        n=zip(q,t)
        return n
    except:  
        f=Progress.objects.all() 
        c=[]
        d=[]
        m=zip(a,b)
        t=dict(m)
        y={k: v for k, v in sorted(t.items(), key=lambda item: item[1])}
        for k,v in y.items():
            c.append(k)
            d.append(v)
        r=c[::-1]
        x=d[::-1]
        g=zip(r,x)
        
        # c=[]  
        # for i in a:
        #     v=t[i]
        #     c.append(v)
        # n=zip(a,c)
        
                   
        # t=sorted(m)
        # for i in range(0,len(f)):
        #     k=t[i][0]
        #     c.append(k)
        # for i in range(0,len(f)):
        #     l=t[i][1]
        #     d.append(l)
        # h=zip(c,d)                       
        return g  
        
        
   