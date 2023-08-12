from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
import datetime

# Create your views here.
from Remote_User.models import review_Model,attack_Model,ClientRegister_Model,postdetails_model,recommend_Model,rating_Model


def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:

            enter = ClientRegister_Model.objects.get(username=username, password=password)
            request.session["userid"] = enter.id
            return redirect('View_All_Post_Details')
        except:
            pass

    return render(request,'RUser/login.html')



def Register1(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city)

        return render(request, 'RUser/Register1.html')
    else:

        return render(request,'RUser/Register1.html')


def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})

def Review(request,pk):
    userid = request.session['userid']
    userObj = ClientRegister_Model.objects.get(id=userid)
    username = userObj.username
    ucity=userObj.city

    objs = postdetails_model.objects.get(id=pk)
    tname = objs.names
    fcity = objs.c_name

    datetime_object = datetime.datetime.now()

    result = ''
    pos = []
    neg = []
    oth = []
    se = 'se'
    rtype='negative'
    rtype1=''
    if request.method == "POST":
        uname = request.POST.get('uname')
        fname = request.POST.get('fname')
        feedback = request.POST.get('feedback')
        fc = request.POST.get('fc')
        yc = request.POST.get('yc')
        cmd = request.POST.get('review')


        if '#' in cmd:
            startingpoint = cmd.find('#')
            a = cmd[startingpoint:]
            endingPoint = a.find(' ')
            title = a[0:endingPoint]
            result = title[1:]
        # return redirect('')

        for f in cmd.split():
            if f in ('good', 'nice', 'better', 'best', 'excellent', 'extraordinary','beautiful', 'happy', 'won', 'love', 'greate',):
                pos.append(f)
            elif f in ('worst', 'waste', 'poor', 'error', 'imporve', 'bad', 'ridicules'):
                neg.append(f)
            else:
                oth.append(f)
        if len(pos) > len(neg):
            se = 'positive'
        elif len(neg) > len(pos) :
            se = 'negative'

            rtype1 = 'User Review'
        else:
            se = 'neutral'



        review_Model.objects.create(uname=uname , ureview=cmd,sanalysis=se,dt=datetime_object,fname=fname ,feedback=feedback,rtype=rtype1)

    return render(request,'RUser/Review.html', {'objc':username,'objc1':tname,'result': result, 'se': se,'ucity':ucity,'fcity':fcity})



def External_Spam_Attacker(request):


    datetime_object = datetime.datetime.now()


    if request.method == "POST":
        uname = request.POST.get('uname')
        pname = request.POST.get('pname')
        feedback = request.POST.get('feedback')
        cmd = request.POST.get('cont')
        se = 'Attack'

        obj = get_object_or_404(postdetails_model, names=pname)
        obj.f_story = cmd
        obj.save(update_fields=['f_story'])


        attack_Model.objects.create(uname=uname , dcont=cmd,dt=datetime_object,pname=pname ,feedback=feedback)

    return render(request,'RUser/External_Spam_Attacker.html')

def Recommend(request,pk):
    userid = request.session['userid']
    userObj = ClientRegister_Model.objects.get(id=userid)
    username = userObj.username

    objs = postdetails_model.objects.get(id=pk)
    appname = objs.names

    if request.method == "POST":
        username1 = request.POST.get('uname')
        fname = request.POST.get('fname')
        loc = request.POST.get('loc')
        recommend = request.POST.get('recommend')

        datetime_object = datetime.datetime.now()

        recommend_Model.objects.create( f_story=recommend, uname1=username1,loc=loc, dt=datetime_object, fname=fname)

    return render(request,'RUser/Recommend.html', {'objc':username,'objc1':appname})


def View_All_Post_Details(request):

    if request.method == "POST":
        kword = request.POST.get('keyword')
        obj = postdetails_model.objects.filter(f_story__contains=kword)
        return render(request, 'RUser/View_All_Post_Details.html', {'objs': obj})
    return render(request,'RUser/View_All_Post_Details.html')

def View_Post_Reviews(request):

    obj = review_Model.objects.all()

    return render(request,'RUser/View_Post_Reviews.html',{'list_objects': obj})




def ratings(request,pk):
    userid = request.session['userid']
    userObj = ClientRegister_Model.objects.get(id=userid)
    username = userObj.username
    ucity = userObj.city

    objs = postdetails_model.objects.get(id=pk)
    tname = objs.names
    fcity = objs.c_name
    rtype1=''
    datetime_object = datetime.datetime.now()
    vott1, vott, neg = 0, 0, 0
    if request.method == "POST":
        uname = request.POST.get('uname')
        fname = request.POST.get('fname')
        rate = request.POST.get('rate')
        fc = request.POST.get('fc')
        yc = request.POST.get('yc')
        rate1 = int(rate)

        rtype1 = 'User Rating'

        datetime_object = datetime.datetime.now()
        objs = postdetails_model.objects.get(id=pk)
        unid = objs.id
        vot_count = postdetails_model.objects.all().filter(id=unid)
        for t in vot_count:
            vott = t.ratings
            vott1 = vott + rate1
            obj = get_object_or_404(postdetails_model, id=unid)
            obj.ratings = vott1
            obj.save(update_fields=["ratings"])


        rating_Model.objects.create(uname=uname,fname=fname,rate=rate,dt=datetime_object,yc=yc,fc=fc,rtype=rtype1)

    return render(request,'RUser/ratings.html',{'objc':username,'objc1':tname,'ucity':ucity,'fcity':fcity})


def dislikes(request,pk):
    vott1, vott, neg = 0, 0, 0
    objs = postdetails_model.objects.get(id=pk)
    unid = objs.id
    vot_count = postdetails_model.objects.all().filter(id=unid)
    for t in vot_count:
        vott = t.dislikes
        vott1 = vott - 1
        obj = get_object_or_404(postdetails_model, id=unid)
        obj.dislikes = vott1
        obj.save(update_fields=["dislikes"])
        return redirect('View_All_Post_Details')
    return render(request,'RUser/dislikes.html',{'objs':vott1})

def ViewTrending(request):
    topic = postdetails_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return render(request, 'RUser/ViewTrending.html', {'objects': topic})

def View_Post_Recommends(request):
    obj = recommend_Model.objects.all()

    return render(request, 'RUser/View_Post_Recommends.html', {'list_objects': obj})

def likes(request,pk):
    vott1, vott, neg = 0, 0, 0
    objs = postdetails_model.objects.get(id=pk)
    unid = objs.id
    vot_count = postdetails_model.objects.all().filter(id=unid)
    for t in vot_count:
        vott = t.likes
        vott1 = vott + 1
        obj = get_object_or_404(postdetails_model, id=unid)
        obj.likes = vott1
        obj.save(update_fields=["likes"])
        return redirect('View_All_Post_Details')

    return render(request,'RUser/likes.html',{'objs':vott1})

