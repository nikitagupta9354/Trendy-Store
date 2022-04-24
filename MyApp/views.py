from django.shortcuts import render

from django.contrib.messages import success,error
from django.shortcuts import HttpResponseRedirect,redirect
from django.db.models import Q

from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.mail import send_mail
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import *
import string
import random



# Create your views here.

def email_send(request,email,name):
    subject = 'Thanks '+name+' for registering to our site'
    message = ' it  means a lot to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )


@login_required(login_url='/login/')
def AdminDeliveredOrder(request):
    order = Order.objects.filter(status="Delivered")
    return render(request,"AdminDeliveredOrder.html", {"DeliveredOrder": order})


@login_required(login_url='/login/')
def AdminPendingOrder(request):
    order = Order.objects.filter(status="Ordered")

    return render(request,"AdminPendingOrder.html",{"PendingOrder":order,})


@login_required(login_url='/login/')
def AdminCancelOrder(request):
    order = Order.objects.filter(status="Canceled")
    return render(request,"AdminCancelOrder.html", {"Cancel_Order": order, })


@login_required(login_url='/login/')
def Adminpage(request):
    profile_user = Profile.objects.get(user__username__contains=request.user)
    address = Address.objects.filter(address_user=request.user)
    return render(request, "adminpage.html", {"User": profile_user, "Address": address})


@login_required(login_url='/login/')
def AdminProducts(request):
    Pro = Product.objects.all()
    return render(request,"adminProducts.html",{"Product": Pro})


@login_required(login_url='/login/')
def AddProduct(request):
    if request.method == 'POST':
        res = ''.join(random.choices(string.digits, k=7))
        pro = Product()
        pro.pid = res

        cn = request.POST.get('cat')
        ct = Category.objects.get(cname=cn)
        pro.cat = ct

        pro.name = request.POST.get('name')
        pro.description = request.POST.get('description')

        bn = request.POST.get('brand')
        bt = Brand.objects.get(bname=bn)
        pro.brand = bt

        pro.basicPrice = request.POST.get('basic_price')
        pro.discount = request.POST.get('discount')
        pro.price = request.POST.get('price')
        img1 = request.FILES.get('uimage1')
        img2 = request.FILES.get('uimage2')
        if img1:
            pro.img1 = img1
        if img2:
            pro.img2 = img2
        pro.save()
        ss = request.POST.getlist('checks[]')
        sizecat = Size.objects.all()
        for i in ss:
            for j in sizecat:
                if i == j.sname:
                    pro.size.add(j)
        pro.save()

        success(request, 'Saved successfully')

    cat = Category.objects.all()
    size = Size.objects.all()
    brand = Brand.objects.all()
    return render(request,"addproduct.html",{"CAT":cat,"Size":size,"Brand": brand,})


@login_required(login_url='/login/')
def EditPro (request,pro_id):
    pro = Product.objects.get(pid=pro_id)
    cat = Category.objects.all()
    size = Size.objects.all()
    brand = Brand.objects.all()
    if request.method == 'POST':
        cn = request.POST.get('cat')
        ct = Category.objects.get(cname=cn)
        pro.cat = ct

        pro.name = request.POST.get('name')
        pro.description = request.POST.get('description')

        bn = request.POST.get('brand')
        bt = Brand.objects.get(bname=bn)
        pro.brand = bt
        pro.basicPrice = request.POST.get('basic_price')
        pro.discount = request.POST.get('discount')
        pro.price = request.POST.get('price')
        img1 = request.FILES.get('uimage1')
        img2 = request.FILES.get('uimage2')
        if img1:
            pro.img1 = img1
        if img2:
            pro.img2 = img2
        ss = request.POST.getlist('checks[]')
        sizecat = Size.objects.all()
        for i in pro.size.all():
            pro.size.remove(i)

        for i in ss:
            for j in sizecat:
                if i == j.sname:
                    pro.size.add(j)



        '''some work need to be done here '''

        pro.save()
        success(request, 'Saved successfully')

    return render(request,"editpro.html",{"DATA":pro,"CAT":cat,"Size":size,"Brand":brand})


@login_required(login_url='/login/')
def DeliverOrder(request,order_no):
    delivered_order = Order.objects.get(orderno=order_no)
    '''
    MoveOrderToDelivered = PreviousOrder()
    MoveOrderToDelivered.orderid = delivered_order.orderid
    MoveOrderToDelivered.orderno = delivered_order.orderno
    MoveOrderToDelivered.order_user = delivered_order.order_user
    MoveOrderToDelivered.order_product= delivered_order. order_product
    MoveOrderToDelivered.order_state = delivered_order.order_state
    MoveOrderToDelivered.order_city = delivered_order.order_city
    MoveOrderToDelivered.order_pin = delivered_order.order_pin
    MoveOrderToDelivered.status = "Delivered"
    MoveOrderToDelivered.order_address = delivered_order.order_address
    MoveOrderToDelivered.count = delivered_order.count
    MoveOrderToDelivered.save()
    '''
    delivered_order.status = "Delivered"
    delivered_order.save()
    order = Order.objects.filter(status="Ordered")
    return render(request, "AdminPendingOrder.html", {"PendingOrder": order})


'''To Cancel'''


@login_required(login_url='/login/')
def cancel_order(request,username,order):
    profile_user = Profile.objects.get(user__username__contains=username)
    order_int = int(order)
    order = Order.objects.filter(order_user=request.user)

    cancel_order = Order.objects.get(orderno=order_int)
    '''
    MoveOrderToCancel = CancelOrder()
    MoveOrderToCancel.orderid = delivered_order.orderid
    MoveOrderToCancel.orderno = delivered_order.orderno
    MoveOrderToCancel.order_user = delivered_order.order_user
    MoveOrderToCancel. order_product= delivered_order. order_produc
    MoveOrderToCancel.order_address = delivered_order.order_address
    MoveOrderToCancel.order_city = delivered_order.order_city
    MoveOrderToCancel.order_state = delivered_order.order_state
    MoveOrderToCancel.order_pin = delivered_order.order_pin
    MoveOrderToCancel.status = "Canceled"
    MoveOrderToCancel.save()
    '''
    '''Cancel order'''
    cancel_order.status = "Canceled"
    cancel_order.save()
    return render(request, "Orders.html", {"User": profile_user, 'Order': order})








'''To Delete'''


def DeletePro(request,pro_id):
    pep = Product.objects.get(pid=pro_id)
    pep.delete()
    Pro = Product.objects.all()
    return render(request, "adminProducts.html", {"Product": Pro})


def cart(request,cn):
    cat = Category.objects.all()
    brand = Brand.objects.all()
    if (request.method == 'POST'):
        sr = request.POST.get('search')
        data = Product.objects.filter(Q(name__icontains=sr)|Q(cat__cname__icontains=sr)|Q(brand__bname__icontains=sr))
        datacount = data.count()
        noData = ""
        if (datacount == 0):
            noData = "No Such product found"
            data = Product.objects.all()
        return render(request, 'shop.html', {"Data": data, "Cat": cat,"Brand":brand , "No": noData})
    else:

        if (cn == "sample"):
            data = Product.objects.all()

        else:
            data = Product.objects.filter(cat__cname=cn)
        return render(request,'shop.html',{"Cat":cat,"Data":data,"Brand":brand
                                       })


def cart2(request,b):
    cat = Category.objects.all()
    brand = Brand.objects.all()
    if (request.method == 'POST'):
        sr = request.POST.get('search')
        data = Product.objects.filter(Q(name__icontains=sr)|Q(cat__cname__icontains=sr)|Q(brand__bname__icontains=sr))
        datacount = data.count()
        noData = ""
        if (datacount == 0):
            noData = "No Such product found"
            data = Product.objects.all()
        return render(request, 'shop2.html', {"Data": data, "Cat": cat,"Brand":brand , "No": noData})
    else:

        if (b == "all"):
            data = Product.objects.all()

        else:
            data = Product.objects.filter(brand__bname=b)
        return render(request, 'shop2.html', {"Cat": cat,"Brand":brand, "Data": data
                                         })


def home(request):
    pro = Product.objects.all()
    return render(request,'nav.html',{"Pro":pro,})


def pdetails(request,num):
    data=Product.objects.get(pid=num)
    if request.method == 'POST':
        error(request,"Please select a size")

    return render(request, 'productdetails.html', {"Data": data})


def pdetails2(request,num,s):
    data = Product.objects.get(id=num)


    if (request.method == 'POST'):
        try:
            d = Cart.objects.get(cart_product__pid=num, cart_user=request.user)
            d.count = int(d.count) + 1
            d.save()
        except:
            c = Cart()

            c.count = int(request.POST.get('count'))
            # c.count=int(a)
            c.cart_user = request.user
            c.cart_product = data
            c.cpsize = s
            b = data.price
            c.total = b * c.count
            c.save()
    return render(request, 'productdetails.html', {"Data": data},{'s':s})


@login_required(login_url='/login/')
def Cartt(request):
    data = Cart.objects.filter(cart_user=request.user)
    uname=request.user.username
    user = User.objects.get(username=uname)
    count =0
    if data:
        ms = ""
        for i in data:
            count += i.total
        return render(request, 'cartk.html', {"Data": data, 'ms': ms, "user": user,"Grand_total":count,})
    else:
        ms='Your Cart is Empty '
        return render(request,'cartk.html',{"Data": data,'ms':ms,"user":user})

'''
def Checkoutt(request,uname):

    data = Address.objects.filter(address_user=request.user)
    address_count = Address.objects.filter(address_user=request.user).count()
    user = User.objects.get(username=uname)
    d = Cart.objects.filter(cart_user=request.user)
    res = ''.join(random.choices(string.digits, k=7))
    r = ''.join(random.choices(string.ascii_uppercase, k=7))

    if address_count != 0:
        return render(request, '1.html', {"Data": data})

    else:
        if request.method == 'POST':
            address = Address()
            address.address_user = request.user
            address.address_city = request.POST.get('city')
            address.address_pin = request.POST.get('pin')
            address.address_state = request.POST.get('state')
            address.address_street = request.POST.get('address')
            address.save()
            c = Checkout()
            c.checkid = r
            c.chname = request.POST.get('uname')
            c.checkout_user = request.user
            c.mobile = request.POST.get('mobile')
            c.email = request.POST.get('email')
            c.state = address.address_state
            c.city = address.address_city
            c.pin = address.address_pin
            c.address = address.address_street
            c.save()
            for i in d:
                o = Order()
                o.orderno = res
                o.order_user = request.user
                o.order_product = i.cart_product
                o.cpsize = i.cpsize
                o.count = 1
                b = i.cart_product.price
                o.total = b
                o.status = 'Ordered'
                o.order_address = c
                o.save()

                return render(request, '1.html', {"Data": data})

        else:
            return render(request, 'addaddress.html',{"user": user})

'''


def Checkoutt(request,uname,gtot):
    data = Address.objects.filter(address_user=request.user)
    add_tot = data.count()
    if add_tot == 0:
        return HttpResponseRedirect("/select_address/")



    else:
        user = Profile.objects.get(user__username__contains=uname)
        if request.method == 'POST':
            address = Address()
            address.address_user = request.user
            address.address_city = request.POST.get('city')
            address.address_pin = request.POST.get('pin')
            address.address_state = request.POST.get('state')
            address.address_street = request.POST.get('address')
            address.save()
            return HttpResponseRedirect('/select_address/' + gtot)

        else:
            return render(request, 'addaddress.html',{"user": user,"gtot":gtot})

@login_required(login_url='/login/')
def select_address(request,gtot):
    data = Address.objects.filter(address_user=request.user)
    user = Profile.objects.get(user__username__contains=request.user)
    d = Cart.objects.filter(cart_user=request.user)

    r = ''.join(random.choices(string.ascii_uppercase, k=7))
    if request.method == 'POST':
        c = Checkout()
        c.checkid = r
        c.chname = request.POST.get('uname')
        c.checkout_user = request.user
        c.mobile = request.POST.get('mobno')
        c.email = request.POST.get('email')
        c.state = request.POST.get('state')
        c.city = request.POST.get('city')
        c.pin = request.POST.get('pin')
        c.address = request.POST.get('address')

        c.save()
        for i in d:
            o = Order()
            res = ''.join(random.choices(string.digits, k=7))
            o.orderno = res
            o.order_user = request.user
            o.order_product = i.cart_product
            o.cpsize = i.cpsize
            o.count = i.count
            b = i.cart_product.price
            o.total = b * i.count
            o.status = 'Ordered'
            o.order_address = c.address
            o.order_state = c.state
            o.order_pin = c.pin
            o.order_city = c.city
            o.save()


    return render(request,'1.html',{"Data":data,"user":user,"gtot":gtot})


def add_address(request,uname):
    user = User.objects.get(username=uname)
    data = Address.objects.filter(address_user=request.user)
    if request.method == 'POST':
        address = Address()
        address.address_user = request.user
        address.address_city = request.POST.get('city')
        address.address_pin = request.POST.get('pin')
        address.address_state = request.POST.get('state')
        address.address_street = request.POST.get('address')
        address.save()
        return HttpResponseRedirect('/select_address/')

    else:
        return render(request, 'addaddress.html', {"user": user})


def Login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pward = request.POST.get('psw')

        user = auth.authenticate(username=uname, password=pward)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect('/adminpage')
            else:
                return HttpResponseRedirect('/')
        else:
            error(request, "Invalid User")
    return render(request,'login.html')


def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        try:
            match = User.objects.get(username=uname)
            if match:
                error(request, "UserName already Exist")
        except:
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            email = request.POST.get('email')
            pward = request.POST.get('pass')
            cpward = request.POST.get('cpa')
            mobno = request.POST.get('mobno')
            if pward == cpward:
                User.objects.create_user(username=uname,
                                         first_name=fname,
                                         last_name=lname,
                                         email=email,
                                         password=pward)
                use = User.objects.all()
                for u in use:
                    if u.username == uname:
                        data = Profile()
                        userr = request.POST.get('uname')
                        ct = User.objects.get(username=userr)
                        data.user = ct
                        data.mobile_no = mobno

                        data.save()
                return redirect('/')
                success(request, "Account is created")
                email_send(request, mail, uname)
            else:
                error(request, "Password & Confirm Password not Matched")
    return render(request,'signup.html')


@login_required(login_url='/login/')
def ProfileView(request,username):
    profile_user = Profile.objects.get(user__username__contains=username)
    address = Address.objects.filter(address_user__username__contains=username)
    user = User.objects.get(username=username)
    j=1
    if request.method == 'POST':
        for i in address:
            i.address_state = request.POST.get('state ' + str(j))
            i.address_city = request.POST.get('city ' + str(j))
            i.address_pin = request.POST.get('pin ' + str(j))
            i.address_street = request.POST.get('street ' + str(j))
            i.save()
            j += j
        img = request.FILES.get("uimage")
        if img:
            profile_user.user_image = img
        profile_user.save()
    if user.is_superuser:
        return render(request,"adminpage.html",{"User": profile_user,"Address":address})
    else:
        return render(request,"user.html",{"User": profile_user,"Address":address})

@login_required(login_url='/login/')
def ProfileOrders(request,username):
    profile_user = Profile.objects.get(user__username__contains=username)
    order = Order.objects.filter(order_user=request.user)

    return render(request,"Orders.html",{"User":profile_user,'Order':order})

@login_required(login_url='/login/')
def AccountView(request,uname):
    use = User.objects.get(username__contains=uname)
    users = Profile.objects.get(user__username__contains=uname)
    if request.method =='POST':
        new_username = request.POST.get('new_username')
        confirm_username = request.POST.get('confirm_new_username')
        current_username = request.POST.get('current_username')
        new_mobile = request.POST.get('new_mobile')
        confirm_mobile = request.POST.get('confirm_new_mobile')
        current_mobile = request.POST.get('current_mobile')

        if new_username == confirm_username and current_username == users.user.username:
            alluser = User.objects.all()
            user_not_exist = True
            for i in alluser:
                if new_username == i.username:
                    user_not_exist = False

            if user_not_exist:
                use.username = new_username
                use.save()
                users.user.username = new_username
                users.save()
                success(request, "Saved")
                return HttpResponseRedirect('/')
            else:
                error(request,"user already exist")



        else:
            error(request,"username already exist")

        if new_mobile == confirm_mobile and current_mobile == users.mobile_no:
            users.mobile_no = new_mobile
        else:
            error(request,"please correct mobile number")

        users.save()

    return render(request,"account.html",{"User":users})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')




def c3(request,num):
    data = Checkout.objects.get(checkid=num)
    dataa=Checkout.objects.filter(checkout_user=request.user)
    r = ''.join(random.choices(string.ascii_uppercase, k=7))
    d = Cart.objects.filter(cart_user=request.user)
    res = ''.join(random.choices(string.digits, k=7))
    c = Checkout()
    c.checkid = r
    c.chname = data.chname
    c.checkout_user = request.user
    c.mobile = data.mobile
    c.email = data.email
    c.state = data.state
    c.city = data.city
    c.pin = data.pin
    c.address = data.address
    c.save()
    for i in d:
        o = Order()
        o.orderno = res
        o.order_user = request.user
        o.order_product = i.cart_product
        o.cpsize = i.cpsize
        o.count = 1
        b = i.cart_product.price
        o.total = b
        o.status = 'Ordered'
        o.order_address = c
        o.save()
    return render(request, '1.html', {"Data": dataa})


def user_view_products(request):
    pro = Product.objects.all()
    name = "nikita"
    return render(request,'products.html',{"pro":pro},)


def CartDelete(request,num):
    data=Cart.objects.get(cart_product__pid=num,cart_user=request.user)
    data.delete()
    s=request.user.username
    return HttpResponseRedirect('/c')

def CartEdit(request,num):
    data=Cart.objects.get(cart_product__pid=num,cart_user=request.user)
    data.count= int(data.count)+1
    data.save()
    s=request.user.username
    return HttpResponseRedirect("/c")
def CartEdit1(request,num):
    data=Cart.objects.get(cart_product__pid=num,cart_user=request.user)
    data.count= int(data.count)-1
    if(int(data.count)==0):
        data.count=1
    data.save()
    s = request.user.username
    return HttpResponseRedirect("/c")


def invoice(request,uname,c,s,street,p):
    d = Cart.objects.filter(cart_user=request.user)
    up = Profile.objects.get(user__username__contains=uname)
    count=0
    for i in d:
        count += i.total
    return render(request,'invoice.html',{"car":d,"city":c,"state":s,"street":street,"pin":p,"user":up,"grand":count})





