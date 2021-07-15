from django.shortcuts import render
import MySQLdb 
#this view process the result page
def home(request):
    if request.method=='POST':
        htno=request.POST['hallticket']
        dob=request.POST['dateofbirth']
        try:
            conn=MySQLdb.connect(host='localhost',user='root',passwd='waste@mysql80',database='sample')
            cur=conn.cursor()
            q='select * from csec_marks where Hallticket=%s'
            v=(htno,)
            cur.execute(q,v)
            conn.rollback()
            conn.close()
            fr=[i for i in cur ]
            if len(fr)!=0:
                r={'ht':fr[0][1],'reg':fr[0][2],'et':fr[0][3],'fe02':fr[0][4],'fe06':fr[0][5],'fe12':fr[0][6],'ee52':fr[0][7],'ci02':fr[0][8],'fe62':fr[0][9],'fe60':fr[0][10],'cs60':fr[0][11],'me75':fr[0][12],'sgpa':fr[0][13]}
                if 'F' in fr[0][4:]:
                    r['status']='FAIL'
                else:
                    r['status']='PASS'
                return render(request,'display.html',r)
            else:
                return render(request,'error.html')
        except:
            conn.close()
            return render(request,'error.html')
    return render(request,'home.html')
