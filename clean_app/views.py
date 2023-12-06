import base64
import base64
from datetime import datetime, date
from django.conf import settings

from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from clean_app.models import *
# Create your views here.


def login(request):
    return render(request,'loginindex.html')
def login_post(request):
    a=request.POST['uname']
    b=request.POST['psw']
    result=Login.objects.filter(username=a,password=b)
    if result.exists():
        result2=Login.objects.get(username=a,password=b)
        request.session['lid']=result2.id
        if result2.type=='admin':
            return HttpResponse('''<script>alert('admin login success fully');window.location='/clean_app/admin_home/'</script>''')
        elif result2.type=='recycle':
            rpro = Recycle.objects.get(LOGIN_id=result2.id)
            return render(request, 'recycler/recycler_homepage.html', {'name':rpro.unit_name})
        elif result2.type=='user':
            w=Worker.objects.get(LOGIN_id=result2.id)
            return render(request,'worker/worker_home.html',{'name':w.name,'image':w.image})
        elif result2.type=='worker':
            return HttpResponse('''<script>alert('Worker login success fully');window.location='/clean_app/worker_home/'</script>''')
        else:
            return HttpResponse('invalid')
    else:
        return HttpResponse(
            '''<script>alert('invalid');window.location='/clean_app/login/'</script>''')

def forget_password(request):
    return render(request,'forget_password.html')

def forget_password_post(request):
    a=request.POST['forget']

    import random
    import string

    # characters = string.ascii_letters + string.digits + string.punctuation
    # password = ''.join(random.choice(characters) for _ in range(9))

    password=random.randint(0000000000,9999999999)
    var=Login.objects.filter(username=a)
    if var.exists():
        var2=Login.objects.get(username=a)
        message="Your Temparory Password is :"+ str(password)
        send_mail(
            'temp password',
            message,
            settings.EMAIL_HOST_USER,
            [a, ],
            fail_silently=False
        )
        var2.password=password
        var2.save()
        return HttpResponse('<script>alert("success");window.location="/clean_app/login/"</script>')
    else:
        return HttpResponse('<script>alert("invalid");window.location="/clean_app/login/"</script>')


def logout(request):
    request.session['lid']=''
    return HttpResponse( '''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')


def admin_change_password(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    return render(request,'admin/Admin_change_password.html')


def admin_change_password_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    old = request.POST['old_password']
    new = request.POST['new_password']
    confirm = request.POST['con_password']
    result=Login.objects.filter(id=request.session['lid'],password=old)
    if result.exists():
        if new==confirm:
            Login.objects.filter(id=request.session['lid']).update(password=confirm)
            return HttpResponse('''<script>alert('Successfully changed');window.location='/clean_app/login/'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid');window.location='/clean_app/admin_home/'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location='/clean_app/login/'</script>''')

def admin_home(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')
    return render(request,'admin/home.html')






def waste(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')
    return render(request,'admin/waste.html')

def waste_post(request):

    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    name=request.POST['name']
    price=request.POST['price']
    var=Waste()
    var.type=name
    var.price=price
    var.save()

    return HttpResponse('''<script>alert('successfully added');window.location='/clean_app/waste/'</script>''')

def view_waste(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')
    var=Waste.objects.all()
    return render(request,'admin/view_waste.html',{'var':var})

def view_waste_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']
    var=Waste.objects.filter(type__contains=search)
    return render(request,'admin/view_waste.html',{'var':var})

def delete_waste(request,id):
    var=Waste.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert('successfully added');window.location='/clean_app/view_waste/'</script>''')

def wasteedit(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Waste.objects.get(id=id)
    return render(request,'admin/waste_edit.html',{'var':var})

def wasteedit_post(request):

    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    id = request.POST['id']
    name = request.POST['name']
    price = request.POST['price']
    var=Waste.objects.filter(id=id).update(type=name,price=price)
    return HttpResponse('''<script>alert('successfully updated');window.location='/clean_app/view_waste/'</script>''')

def view_worker(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker.objects.all()
    return render(request, 'admin/view_worker.html',{'var':var})
def view_worker_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')
    search=request.POST['search']
    var=Worker.objects.filter(name__icontains=search)
    return render(request, 'admin/view_worker.html',{'var':var})


def worker_aproved(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker.objects.filter(LOGIN_id=id).update(status='approved')
    var2=Login.objects.filter(id=id).update(type='worker')

    return HttpResponse('''<script>alert('Worker Approved');window.location='/clean_app/view_aproved_worker/'</script>''')

def view_aproved_worker(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')
    var=Worker.objects.filter(status='approved')
    return render(request,'admin/view_aproved_worker.html',{'var':var})

def view_aproved_worker_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']

    var=Worker.objects.filter(name__icontains=search)
    return render(request,'admin/view_aproved_worker.html',{'var':var})



def reject_worker(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker.objects.filter(LOGIN_id=id).update(status='Rejected')
    var2=Login.objects.filter(id=id).update(type='Rejected')
    return HttpResponse('''<script>alert('Worker Rejected');window.location='/clean_app/view_reject_worker/'</script>''')

def view_reject_worker_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']

    var=Worker.objects.filter(name__icontains=search)
    return render(request,'admin/view_reject_worker.html',{'var':var})


def view_reject_worker(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker.objects.filter(status='Rejected')
    return render(request,'admin/view_reject_worker.html',{'var':var})

def allocation(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker.objects.all()
    return render(request, 'admin/allocation.html',{'var':var})

def view_allocation(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Allocation.objects.all()
    # var2=Allocation.objects.all()
    return render(request,'admin/view_allocation.html',{'data':var})

def view_allocation_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    # area=request.POST['area']
    search=request.POST['search']
    var=Allocation.objects.filter(WORKER__name__icontains=search)

    # if area =='Select':
    #     var = Allocation.objects.filter(area__icontains=area)
    #
    # elif area =='Select':
    #     var=Allocation.objects.filter(WORKER__name__icontains=search,area__icontains=area)
    # else:
    #     var=Allocation.objects.filter(WORKER__name__icontains=search)

    var2=Allocation.objects.all()
    return render(request,'admin/view_allocation.html',{'data':var})


def edit_allocation(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var2=Worker.objects.all()
    var=Allocation.objects.get(id=id)
    return render(request,'admin/edit_allocation.html',{'data':var,'var2':var2})

def edit_allocation_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    id = request.POST['id']

    area = request.POST['area']
    date = request.POST['date']
    worker = request.POST['worker']

    var=Allocation.objects.filter(id=id).update(area=area,date=date,WORKER=worker)

    return HttpResponse('''<script>alert('Updated');window.location='/clean_app/view_allocation/'</script>''')

def delete_allocation(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Allocation.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/clean_app/view_allocation/'</script>''')

# def worker_view_user_requests(request):
#     if request.session['lid']=="":
#         return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')
#
#     lid=Login.objects.get(id=request.session['lid'])
#     wid=Worker.objects.get(LOGIN=lid)
#     rid=Request.objects.filter(WORKER=wid)
#     return render(request,'worker/worker_view_user_request.html',{'var':rid})



def worker_reply__request_post(request):

    return HttpResponse('''<script>alert( updated');window.location='/clean_app/worker_view_user_request/'</script>''')

def allocation_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    area = request.POST['area']
    date = request.POST['date']
    worker = request.POST['worker']

    var=Allocation()
    var.WORKER_id=worker
    var.area=area
    var.date=date
    var.save()

    return HttpResponse('''<script>alert('successfully updated');window.location='/clean_app/allocation/'</script>''')


def view_user(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=User.objects.all()
    return render(request, 'admin/view_user.html',{'var':var})

def view_user_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']
    var=User.objects.filter(name__icontains=search)
    return render(request, 'admin/view_user.html',{'var':var})




def view_complaint(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Complaint.objects.all()
    return render(request, 'admin/View_complaint.html',{'var':var})


def view_complaint_post(request, ):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    fromD=request.POST['f']
    to=request.POST['t']
    var=Complaint.objects.filter(date__range=[fromD,to])

    return render(request, 'admin/View_complaint.html', {'var': var})



def complaint_reply(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Complaint.objects.get(id=id)

    return render(request,'admin/complaint_reply.html',{'data':var})

def complaint_reply_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    id = request.POST['id']
    com = request.POST['reply']
    var = Complaint.objects.get(id=id)
    var.reply = com
    var.status = 'Replied'
    var.save()
    return HttpResponse('''<script>alert('successfully sent');window.location='/clean_app/view_complaint/'</script>''')


def category(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    return render(request, 'admin/category.html')

def category_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=request.POST['cat']
    result=Worker_category()
    result.category=var
    result.save()
    return HttpResponse('''<script>alert('successfully added');window.location='/clean_app/category/'</script>''')

def view_category(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker_category.objects.all()
    return render(request, 'admin/view_category.html',{'var':var})

def view_category_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    name=request.POST['name']
    var=Worker_category.objects.filter(category__icontains=name)
    return render(request, 'admin/view_category.html',{'var':var})

def detele_category(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker_category.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert('successfully deleted');window.location='/clean_app/view_category/'</script>''')

def edit_category(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker_category.objects.get(id=id)
    return render(request,'admin/edit_category.html',{'var':var})

def edit_category_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var = request.POST['cat']
    id = request.POST['id']
    result = Worker_category.objects.get(id=id)
    result.category = var
    result.save()
    return HttpResponse('''<script>alert('successfully updated');window.location='/clean_app/view_category/'</script>''')

def view_feedback(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Feedback.objects.all()
    return render(request, 'admin/view_feedback.html',{'var':var})

def view_feedback_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    fromdate=request.POST['fromsearch']
    todate=request.POST['to']
    var=Feedback.objects.filter(date__range=[fromdate,todate])
    return render(request, 'admin/view_feedback.html',{'var':var})

def worker_notification(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Worker.objects.all()
    return render(request,'admin/worker_notification.html',{'data':var})

def worker_notification_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    noti=request.POST['notification']
    date=request.POST['date']
    worker=request.POST['worker']
    var=Notification()
    var.notification=noti
    var.date=date
    var.WORKER_id=worker
    var.save()
    return HttpResponse('''<script>alert('successfully Added');window.location='/clean_app/worker_notification/'</script>''')

def admin_view_notification(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')
    var=Notification.objects.all()
    return render(request,'admin/adminview_notification.html',{'data':var})

def admin_view_notification_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    fromdate=request.POST['fromdate']
    to=request.POST['to']
    var=Notification.objects.filter(date__range=[fromdate,to])
    return render(request,'admin/adminview_notification.html',{'data':var})

def delete_notification(request,id):
    var=Notification.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert('successfully Deleted');window.location='/clean_app/admin_view_notification/'</script>''')


def view_pickup(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Pickup.objects.all()
    return render(request,'admin/view_pickup.html',{'data':var})

def view_pickup_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']
    var=Pickup.objects.filter(name__icontains=search)
    return render(request,'admin/view_pickup.html',{'data':var})

def aproved_pickup(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Pickup.objects.filter(LOGIN_id=id).update(status='approved')
    var2=Login.objects.filter(id=id).update(type='pickup')
    return HttpResponse('''<script>alert('successfully Aproved');window.location='/clean_app/view_pickup/'</script>''')

def reject_pickup(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Pickup.objects.filter(LOGIN_id=id).update(status="rejected")
    var2=Login.objects.filter(id=id).update(type='pending')
    return HttpResponse('''<script>alert(' Rejectd');window.location='/clean_app/view_pickup/'</script>''')


def view_Aproved_pickup(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Pickup.objects.filter(status="approved")
    return render(request,'admin/view_aproved_pickup.html',{'data':var})

def view_Aproved_pickup_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    search=request.POST['searching']
    var=Pickup.objects.filter(name__icontains=search)
    return render(request,'admin/view_aproved_pickup.html',{'data':var})

def view_Reject_pickup(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    var=Pickup.objects.filter(status="rejected")
    return render(request,'admin/view_reject_pickup.html',{'data':var})

def view_Reject_pickup_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script>alert(' Logout SuccessFully');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']
    var=Pickup.objects.filter(name__icontains=search)
    return render(request,'admin/view_reject_pickup.html',{'data':var})



# users




def login2(request):
    a = request.POST['uname']
    b = request.POST['psw']
    result = Login.objects.filter(username=a, password=b)
    if result.exists():
        result2 = Login.objects.get(username=a, password=b)
        if result2.type == 'user':
            lid=result2.id
            usr=User.objects.get(LOGIN_id=lid)
            return JsonResponse({'status':"ok",'lid':str(lid),'type':'user','photo':usr.image,'name':usr.name})
        elif result2.type == 'worker':
            lid=result2.id
            Wrk=Worker.objects.get(LOGIN_id=lid)
            return JsonResponse({'status':"ok",'lid':str(lid),'type':'worker','photo':Wrk.image,'name':Wrk.name})
        elif result2.type == 'pickup':
            lid=result2.id
            # pick=Pickup.objects.get(LOGIN_id=lid)

            return JsonResponse({'status':"ok",'lid':str(lid),'type':'pickup'})
        else:
            return JsonResponse({'status': 'not Ok'})
    else:
        return JsonResponse({'status': 'not Ok'})


def user_post(request):
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    district=request.POST['district']
    password=request.POST['password']
    conf=request.POST['confirm']

    if password==conf:
        image = request.POST['image']
        fs1 = base64.b64decode(image)
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\user\\' + date1, 'wb').write(fs1)

        path1 = "/media/user/" + date1

        var = Login()
        var.username = email
        var.password = password
        var.type = 'user'
        var.save()

        result = User()
        result.LOGIN = var
        result.name = name
        result.email = email
        result.place = place
        result.phone = phone
        result.pin = pin
        result.post = post
        result.image=path1
        result.district = district
        result.save()
        return JsonResponse({'status': "ok"})
    else:
        return JsonResponse({'status': "Not Ok"})





def user_profile(request):
    lid=request.POST['lid']
    var=User.objects.get(LOGIN_id=lid)
    return JsonResponse({'status': "ok",'name':var.name,'email':var.email,'phone':var.phone,'place':var.place,'post':var.post,'district':var.district,'pin':var.pin,'gender':var.gender,'image':var.image})


def edit_userprofile(request):
    lid=request.POST['loginid']
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    district=request.POST['district']
    gender=request.POST['gender']
    image=request.POST['image']

    result = User.objects.get(LOGIN_id=lid)
    result.name = name
    result.email = email
    result.place = place
    result.phone = phone
    result.pin = pin
    result.post = post
    result.gender = gender
    result.district = district

    if len(image)> 1:
        fs1 = base64.b64decode(image)
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\user\\' + date1, 'wb').write(fs1)
        path1 = "/media/user/" + date1
        result.image=path1

    result.save()
    return JsonResponse({'status': "ok"})

def add_waste_request(request):
    return JsonResponse({'status': "ok"})

def manage_feedback(request):
    lid = request.POST['lid']
    feedback = request.POST['feedback']
    uid=User.objects.get(LOGIN_id=lid)
    date=datetime.now().strftime('%Y-%m-%d')

    fobj=Feedback()
    fobj.feedback=feedback
    fobj.USER=uid
    fobj.date=date
    fobj.save()

    return JsonResponse({'status': "ok"})

def user_view_feedback(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)
    feed=Feedback.objects.filter(USER=var2)

    a=[]
    for i in feed:
        a.append({'id':i.id,'feedback':i.feedback,'date':i.date})
    return JsonResponse({'status': "ok",'data':a})


def user_complaint_post(request):
    var=request.POST['comp']
    lid=request.POST['lid']
    date=datetime.now()

    c_obj=Complaint()
    c_obj.complaint=var
    c_obj.date=date
    uid=User.objects.get(LOGIN_id=lid)
    c_obj.USER=uid
    c_obj.save()

    return JsonResponse({'status': "ok"})

def worker_category_request_sent(request):
    lid=request.POST['lid']
    wid=request.POST['workerid']
    req=request.POST['req']
    date=request.POST['date']

    var=Workerrequest()
    var.USER=User.objects.get(LOGIN_id=lid)
    var.WORKER=Worker.objects.get(id=wid)
    var.workinfo=req
    var.date=date
    var.status='Pending'
    var.save()

    return JsonResponse({'status': "ok"})


def cancel_request(request):
    id = request.POST['id']
    var = Workerrequest.objects.filter(id=id).update(status='Cancelled')
    return JsonResponse({'status': "ok"})



def view_worker_category_request(request):
    var=request.POST['lid']
    uid=Workerrequest.objects.filter(USER__LOGIN_id=var)

    l=[]
    for i in uid:
        l.append({'id':i.id,'date':i.date,'workinfo':i.workinfo,'status':i.status,'workname':i.WORKER.name})
    return JsonResponse({'status': "ok",'data':l})




def user_view_complaints(request):
    var=request.POST['lid']
    var2=User.objects.get(LOGIN=var)
    result=Complaint.objects.filter(USER=var2)
    l =[]
    for i in result:
        l.append({'id':i.id, 'complaint':i.complaint,'date':i.date,'reply':i.reply,'status':i.status})
    return JsonResponse({'status': "ok", 'data':l})

def viewrequestworker(request):
    cat=request.POST['cat']
    if cat=='':
        var=Worker.objects.all()
    else:
        var = Worker.objects.filter(CATEGORY__category=cat)
    l=[]
    for i in var:
        l.append({'id':i.id,'name':i.name,'place':i.place,'phone':i.phone,'district':i.district, 'cat':i.CATEGORY.category})

    return JsonResponse({'status': "ok",'data':l})


def user_add_waste(request):
    worker=request.POST['workerid']
    requests=request.POST['request']
    lid=request.POST['lid']
    waste=request.POST['waste']
    date=datetime.now().date()

    var=Request()
    var.USER=User.objects.get(LOGIN_id=lid)
    var.WORKER_id=worker
    var.request=requests
    var.WASTE=Waste.objects.get(id=waste)
    var.date=date
    var.save()
    return JsonResponse({'status': "ok"})

def view_worker_notification(request):
    var=Notification.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'notification':i.notification,'workerid':i.WORKER.id,'worker_name':i.WORKER.name,'date':i.date})
    return JsonResponse({'status':'ok','data':l})


def view_recycle_product(request):
    var=Product.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'name':i.name,'amount':i.amount,'recycleid':i.RECYCLE.id,'recycle_name':i.RECYCLE.unit_name})
    return JsonResponse({'status':'ok','data':l})

def u_add_to_cart(request):
    lid=request.POST['lid']
    prod_id=request.POST['product_id']
    qty=request.POST['qty']
    date=datetime.now()

    var=Cart()
    var.date=date
    var.PRODUCT_id=prod_id
    var.USER=User.objects.get(LOGIN_id=lid)
    var.quantity=qty
    var.save()
    return JsonResponse({'status':'ok'})


def view_cart(request):
    lid=request.POST['lid']
    var=Cart.objects.filter(USER__LOGIN_id=lid)

    l=[]
    total=0

    for i in var:
        total += (float(i.PRODUCT.amount) * int(i.quantity))
        l.append({'id':i.id,'date':i.date,'qty':i.quantity,'product':i.PRODUCT.name,'recycle_name':i.PRODUCT.RECYCLE.unit_name,'amount':i.PRODUCT.amount})

    return JsonResponse({'status':'ok','data':l,'total':total})


def remove_cart(request):
    id=request.POST['id']
    var=Cart.objects.filter(id=id).delete()

    return JsonResponse({'status':'ok'})





def user_change_password(request):
    lid=request.POST['lid']
    old=request.POST['old']
    newpass=request.POST['new']
    confirm=request.POST['confirm']

    var=Login.objects.filter(id=lid,password=old)
    if var.exists():
        if newpass==confirm:
            var2=Login.objects.filter(id=lid).update(password=confirm)
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'Not ok'})
    else:
        return JsonResponse({'status': 'NO'})

def user_forget_password(request):
    return JsonResponse({'status': 'ok'})

def user_payment(request):
    lid=request.POST['lid']
    cardnumber=request.POST['cardnumber']
    holdername=request.POST['name']
    expiredate=request.POST['expiredate']
    Cvv=request.POST['cvv']
    Amount=float(request.POST['amount'])

    if Bank.objects.filter(cardnumber=cardnumber, Acname=holdername, expiredate=expiredate, Cvv=Cvv, Balance__gte=Amount).exists():
        res = Cart.objects.filter(USER__LOGIN_id=lid).values_list('PRODUCT__RECYCLE__id').distinct()

        for i in res:
            print(i)
            res2 = Cart.objects.filter(USER__LOGIN_id=lid,PRODUCT__RECYCLE_id=i[0])
            boj = OrderMain()
            boj.USER=User.objects.get(LOGIN_id=lid)
            boj.amount=0
            boj.order_date = datetime.now().date().today()
            boj.RECYCLE_id = i[0]
            boj.save()

            # res3 =
            mytotal=0
            for j in res2:
                print(j)
                bs=OrderSub()
                bs.ORDERMAIN_id=boj.id
                bs.PRODUCT_id=j.PRODUCT.id
                bs.qty=j.quantity
                bs.save()

                mytotal+=(float(j.PRODUCT.amount)*j.quantity)
            Cart.objects.filter(PRODUCT__RECYCLE_id=i[0], USER__LOGIN_id=lid).delete()
            b1oj=OrderMain.objects.get(id=boj.id)
            b1oj.amount =mytotal
            b1oj.save()
            #
            # for i in
        return JsonResponse({'k':'0','status':"ok"})
    else:
        return JsonResponse({"status":"no"})

def waste_payment(request):
    lid = request.POST['lid']
    cardnumber = request.POST['cardnumber']
    holdername = request.POST['name']
    expiredate = request.POST['expiredate']
    Cvv = request.POST['cvv']
    requestid = request.POST['request']
    amount=Waste.objects.get(id=Request.objects.get(id=requestid).WASTE_id).price

    if Bank.objects.filter(cardnumber=cardnumber, Acname=holdername, expiredate=expiredate, Cvv=Cvv,
                           Balance__gte=amount).exists():
        var=WastePayment()
        var.USER_id=Login.objects.get(id=lid)
        var.status='Paid'
        # var2=Request.objects.get()
        var.WASTEREQUEST=Request.objects.get(id=requestid)
        var.date=datetime.now().date().today()
        var.save()
        Request.objects.filter(id=requestid).update(status='Paid')
        return JsonResponse({"status":"ok"})
    return JsonResponse({"status":"no"})



def view_order(request):
    lid=request.POST['lid']
    var=OrderMain.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'recycle':i.RECYCLE.unit_name,'date':i.order_date,'amount':i.amount})
    return JsonResponse({"status": "ok",'data':l})

def view_order_product(request):
    order=request.POST['order_id']

    var=OrderSub.objects.filter(ORDERMAIN_id=order)
    l=[]
    for i in var:
        l.append({'id':i.id,'productname':i.PRODUCT.name,'qty':i.qty,'amount':i.ORDERMAIN.amount})
    return JsonResponse({"status": "ok",'data':l})

def user_logout(request):
    return JsonResponse({"status": "ok"})


def user_view_waste_request(request):
    lid=request.POST['lid']
    var=Request.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'wastename':i.WASTE.type,'price':i.WASTE.price,'status':i.status,'request':i.request,'date':i.date})
    return JsonResponse({"status": "ok",'data':l})



# workerssss

def worker_home(request):
    return render(request,'worker/worker_home.html')

def view_worker_category(request):
    var=Worker_category.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'category':i.category})
    return JsonResponse({'status':'ok','data':l})


def view_waste_category(request):
    var=Waste.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'type':i.type})


    return JsonResponse({'status':'ok','data':l})



def worker_post(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    place = request.POST['place']
    pin = request.POST['pin']
    post = request.POST['post']
    district = request.POST['district']
    password = request.POST['password']
    confpassword = request.POST['confpassword']
    dob = request.POST['date']
    qualification = request.POST['qualification']
    category = request.POST['category']
    image1 = request.POST['image1']

    if password==confpassword:
        import base64
        fs = base64.b64decode(image1)
        date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\worker\image\\'+date,'wb').write(fs)
        path='/media/worker/image/'+date


        proof = request.POST['proof']
        import base64
        fs1=base64.b64decode(proof)
        date1=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\worker\id_proof\\'+date1,'wb').write(fs1)
        path1="/media/worker/id_proof/"+date1



        var = Login()
        var.username = email
        var.password = password
        var.type = 'pending'
        var.save()

        result = Worker()
        result.LOGIN = var
        result.name = name
        result.email = email
        result.place = place
        result.phone = phone
        result.pin = pin
        result.post = post
        result.district = district
        result.dob=dob
        result.image=path
        result.proof=path1
        result.qualification=qualification
        result.CATEGORY_id=category

        result.save()
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'Error Occured'})





def worker_edit_profile(request):
    lid=request.POST['lid']
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    place = request.POST['place']
    pin = request.POST['pin']
    post = request.POST['post']
    district = request.POST['district']

    dob = request.POST['date']
    qualification = request.POST['qualification']
    category = request.POST['category']
    image1 = request.POST['image1']

    proof = request.POST['proof']



    result = Worker.objects.get(LOGIN_id=lid)
    result.name = name
    result.email = email
    result.place = place
    result.phone = phone
    result.pin = pin
    result.post = post
    result.district = district
    result.dob = dob
    if len(image1) > 1:
        import base64
        fs = base64.b64decode(image1)
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\worker\image\\' + date, 'wb').write(fs)
        path = '/media/worker/image/' + date

        result.image = path
    if len(proof) > 1:

        import base64
        fs1 = base64.b64decode(proof)
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\worker\id_proof\\' + date1, 'wb').write(fs1)
        path1 = "/media/worker/id_proof/" + date1

        result.proof = path1
    result.qualification = qualification
    result.CATEGORY_id = category

    result.save()
    return JsonResponse({'status': 'ok'})


def worker_profile(request):
    lid=request.POST['lid']
    var=Worker.objects.get(LOGIN_id=lid)
    return JsonResponse({'status': 'ok','name':var.name,'email':var.email,'phone':var.phone,'district':var.district,'dob':var.dob,'place':var.place,'pin':var.pin,'post':var.post,'category':var.CATEGORY.category,'image':var.image,'proof':var.proof,'qualification':var.qualification})

def workerchangepassword(request):
    lid = request.POST['lid']
    old = request.POST['old']
    newpass = request.POST['new']
    confirm = request.POST['confirm']

    var = Login.objects.filter(id=lid, password=old)
    if var.exists():
        if newpass == confirm:
            var2 = Login.objects.filter(id=lid).update(password=confirm)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'Not ok'})
    else:
        return JsonResponse({'status': 'NoT Ok'})



# def worker_view_user_request_and_reply(request):
#     return JsonResponse({'status': 'ok'})


def view_worker_allocation(request):
    lid=Login.objects.get(id=request.session['lid'])
    wid=Worker.objects.get(LOGIN=lid)
    A_id=Allocation.objects.filter(WORKER=wid)
    return render(request,'worker/view_worker_allocation.html',{'data':A_id})

def view_notification(request):
    lid=Login.objects.get(id=request.session['lid'])
    wid=Worker.objects.get(LOGIN=lid)
    Nid=Notification.objects.filter(WORKER=wid)
    return render(request,'worker/view_notification.html',{'data':Nid})


def worker_view_allocation(request):
    lid=request.POST['lid']
    var=Worker.objects.get(LOGIN=lid)
    a=Allocation.objects.filter(WORKER=var)
    l=[]
    for i in a:
        l.append({'id':i.id,'area':i.area,'date':i.date})
    return JsonResponse({'status':'ok','data':l})

#
# def worker_view_user_request(request):
#     var=Request.objects.all()
#     l=[]
#     for i in var:
#         l.append({'id':i.id,'request':i.request,'username':i.USER.name,'status':i.status,'area':i.USER.place,'date':i.date})
#     return JsonResponse({'status':'ok','data':l})


def worker_view_user_request(request):
    lid=request.POST['lid']
    var=Workerrequest.objects.filter(WORKER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'username':i.USER.name,'workinfo':i.workinfo,'status':i.status,'date':i.date})
    return JsonResponse({'status':'ok','data':l})



# pickup

def pickup_post(request):
    name=request.POST['name']
    email=request.POST['email']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    phone=request.POST['phone']
    password = request.POST['password']
    confpassword = request.POST['confpassword']

    if password==confpassword:
        proof = request.POST['proof']
        fs1 = base64.b64decode(proof)
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\pickup\id_proof\\' + date1, 'wb').write(fs1)
        path1 = "/media/pickup/id_proof/" + date1

        var = Login()
        var.username = email
        var.password = password
        var.type = 'pending'
        var.save()


        var2=Pickup()
        var2.name=name
        var2.qualification=qualification
        var2.LOGIN=var
        var2.proof=path1
        var2.experience=experience
        var2.phone=phone
        var2.save()
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'Not ok'})


def Pickup_edit_profile(request):
    lid=request.POST['lid']
    name = request.POST['name']
    email = request.POST['email']
    qualification = request.POST['qualification']
    experience = request.POST['experience']
    phone = request.POST['phone']


    proof = request.POST['proof']



    var2 = Pickup.objects.get(LOGIN_id=lid)
    var2.name = name
    var2.qualification = qualification
    var2.email = email
    if len(proof)> 1:
        fs1 = base64.b64decode(proof)
        date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        open(r'C:\Users\GAYATHRI\Desktop\clean html\clean_sweap\media\pickup\id_proof\\' + date1, 'wb').write(fs1)
        path1 = "/media/pickup/id_proof/" + date1
        var2.proof = path1
    var2.experience = experience
    var2.phone = phone
    var2.save()
    return JsonResponse({'status': 'ok'})


def collect_waste_request(request):
    rid=request.POST['rid']
    var=Request.objects.filter(id=rid).update(status='collected')
    return JsonResponse({'status': 'ok'})

def worker_update_status_request(request):
    rid=request.POST['rid']
    var=Workerrequest.objects.filter(id=rid).update(status="Approve")
    return JsonResponse({'status': 'ok'})

def worker_update_status_request_reject(request):
    rid=request.POST['rid']
    var=Workerrequest.objects.filter(id=rid).update(status="Reject")
    return JsonResponse({'status': 'ok'})


def worker_update_request(request):
    return JsonResponse({'status':'ok'})


def pick_profile(request):
    lid=request.POST['lid']
    var=Pickup.objects.get(LOGIN_id=lid)
    return JsonResponse({'status': 'ok','name':var.name,'email':var.email,'phone':var.phone,'proof':var.proof,'qualification':var.qualification,'experience':var.experience})

def pickupchangepassword(request):
    lid = request.POST['lid']
    old = request.POST['old']
    newpass = request.POST['new']
    confirm = request.POST['confirm']

    var = Login.objects.filter(id=lid, password=old)
    if var.exists():
        if newpass == confirm:
            var2 = Login.objects.filter(id=lid).update(password=confirm)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'Not ok'})
    else:
        return JsonResponse({'status': 'NoT Ok'})

def view_user_waste_request(request):
    var=Request.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'request':i.request,'username':i.USER.name,'status':i.status,'area':i.USER.place,'date':i.date})
    return JsonResponse({'status':'ok','data':l})













# recycle
def recycle_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    return render(request,'recycler/recycler_homepage.html')

def recycle_reg(request):
    return render(request,'recycler/recycle_reg.html')
def recycle_reg_post(request):
    name=request.POST['name']
    place=request.POST['Place']
    post=request.POST['post']
    Pin=request.POST['Pin']
    Phone=request.POST['Phone']
    email=request.POST['email']
    district=request.POST['district']
    password=request.POST['psw']
    confirmpassword=request.POST['psw2']

    if password==confirmpassword:
        var = Login()
        var.username = email
        var.password = password
        var.type = 'pending'
        var.save()

        var2 = Recycle()
        var2.LOGIN = var
        var2.unit_name = name
        var2.place = place
        var2.post = post
        var2.pin = Pin
        var2.district = district
        var2.phone = Phone
        var2.email = email
        var2.save()
        return HttpResponse('''<script>alert('Register success fully ');window.location='/clean_app/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('Password Can't Match');window.location='/clean_app/login/'</script>''')

def recycle_change_password(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')


    return render(request,'recycler/recycle_change_password.html')

def recycle_change_password_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')


    old=request.POST['old_password']
    new=request.POST['new_password']
    conf=request.POST['con_password']
    var=Login.objects.filter(id=request.session['lid'],password=old)

    if var.exists():
        if new==conf:
            var2 = Login.objects.filter(id=request.sesion['lid']).update(password=conf)
            return HttpResponse(
                '''<script>alert('password change  success fully ');window.location='/clean_app/login/'</script>''')

        else:
            return HttpResponse(
                '''<script>alert('password doesnot  match ');window.location='/clean_app/recycle_change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert('password change  success fully ');window.location='/clean_app/recycle_change_password/'</script>''')


def view_recycle(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')


    var=Recycle.objects.all()
    return render(request,'admin/view_recycle.html',{'var':var})

def view_recycle_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']
    var=Recycle.objects.filter(unit_name__icontains=search)
    return render(request,'admin/view_recycle.html',{'var':var})




def recycle_aproved(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    Recycle.objects.filter(LOGIN_id=id).update(status='approved')
    Login.objects.filter(id=id).update(type='recycle')
    return HttpResponse('''<script>alert('recycler aproved ');window.location='/clean_app/view_aproved_recycler/'</script>''')

def recycle_reject(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    var=Recycle.objects.filter(LOGIN_id=id).update(status='Rejected')
    Login.objects.filter(id=id).update(type='pending')
    return HttpResponse('''<script>alert('recycler Rejected ');window.location='/clean_app/view_reject_recycler/'</script>''')

def view_aproved_recycler(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    var=Recycle.objects.filter(status='Approved')
    return render(request,'admin/view_aproved_recycler.html',{'var':var})

def view_aproved_recycler_post(request):
    search = request.POST['search']
    var = Recycle.objects.filter(unit_name__icontains=search)
    return render(request,'admin/view_aproved_recycler.html',{'var':var})

def view_reject_recycler(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    var=Recycle.objects.filter(status='Rejected')

    return render(request,'admin/view_reject_recycler.html',{'var':var})

def view_reject_recycler_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    search=request.POST['search']
    var=Recycle.objects.filter(unit_name__icontains=search)
    return render(request,'admin/view_reject_recycler.html',{'var':var})




def recycle_profile(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    var=Recycle.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'recycler/recycle_profile.html',{'var':var})

def recycler_edit(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    var=Recycle.objects.get(id=id)
    return render(request,'recycler/recycle_edit_profile.html',{'var':var})

def recycler_edit_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    id=request.POST['id']
    name = request.POST['name']
    place = request.POST['Place']
    post = request.POST['post']
    Pin = request.POST['pin']
    Phone = request.POST['Phone']
    email = request.POST['email']
    district = request.POST['district']
    var=Recycle.objects.filter(id=id).update(unit_name=name,place=place,post=post,pin=Pin,district=district,phone=Phone,email=email)
    return HttpResponse('''<script>alert('Edit success fully ');window.location='/clean_app/recycle_profile/'</script>''')

def view_user_request(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    return render(request,'recycler/view_user_request.html')

def product_add(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')



    return render(request,'recycler/products_add.html')

def product_add_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    lid=Login.objects.get(id=request.session['lid'])
    rid=Recycle.objects.get(LOGIN_id=lid)

    name= request.POST['name']
    price = request.POST['price']

    var=Product()
    var.RECYCLE=rid
    var.name=name
    var.amount=price
    var.save()
    return HttpResponse('''<script>alert('Successfully added');window.location='/clean_app/product_add/'</script>''')

def product_view(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    var=Product.objects.all()
    return render(request,'recycler/product_view.html',{'data':var})

def product_edit(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    var=Product.objects.get(id=id)
    return render(request,'recycler/product_edit.html',{'data':var})

def product_edit_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('Logout success fully ');window.location='/clean_app/login/'</script>''')

    id=request.POST['id']
    name = request.POST['name']
    price = request.POST['price']

    var=Product.objects.get(id=id)
    var.name=name
    var.amount=price
    var.save()
    return HttpResponse('''<script>alert('Successfully updated');window.location='/clean_app/product_view/'</script>''')


def product_delete(request,id):
    var=Product.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/clean_app/product_view/'</script>''')


def recylcer_view_product_order(request):
    rid=Recycle.objects.get(LOGIN=request.session['lid'])
    oid=Payment.objects.filter(ORDERMAIN__RECYCLE=rid)

    return render(request,'recycler/view_product_order.html',{'data':oid})
def recylcer_view_ordersub(request,id):
    var=OrderSub.objects.filter(ORDERMAIN_id=id)
    return render(request,'recycler/recycler_view_ordersub.html',{'data':var})

def View_collected_user_request(request):
    var=Request.objects.filter(status='collected')
    return render(request,'recycler/view_collected_user_request.html',{'data':var})