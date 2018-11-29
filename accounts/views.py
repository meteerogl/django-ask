from django.shortcuts import render,HttpResponseRedirect,reverse, redirect, HttpResponse, get_object_or_404
from .forms import registerForm, loginForm, profileForm, askForm
from django.contrib.auth import authenticate, login,logout
from accounts.models import QUESTIONS, PROFILE, COUPLING
from random import shuffle
from django.views.generic import RedirectView
from django.contrib.auth.models import User




def register_view(request):
    userform = registerForm(prefix="register")
    userprofileform = profileForm(request.POST,prefix="profile")
    if request.method == "POST":
        register = registerForm(request.POST,prefix="register")
        userprofile= profileForm(request.POST,prefix="profile")
        if register.is_valid() * userprofile.is_valid():
            user = register.save()
            user.set_password(user.password)
            user.save()
            userp = userprofile.save(commit=False)
            userp.user = user
            userp.set_token()
            userp.subscribed = "1"
            userp.save()
            return HttpResponse("başarılı")
        else:
            return render(request,"register.html",context={"userform":userform,"userprofileform":userprofileform})
    else:
        return render(request,"register.html",context={"userform":userform,"userprofileform":userprofileform})


def login_view(request):
    form =loginForm(request.POST or None)
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts:wall"))
    else:
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                                password=form.cleaned_data["password"])
            if user:
                login(request,user)
                print(user)
                return HttpResponseRedirect(reverse("accounts:wall"))
    
    return render(request,"login.html",context={"form":form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:login"))

def wall(request):
    questions = QUESTIONS.objects.all()
    context = {"questions":questions}
    
    return render(request,"accounts/wall.html",context)


def question(request,id):
    try:
        soru = QUESTIONS.objects.get(id=id)
        cevaplar = [soru.answer_one,soru.answer_two,soru.answer_three,soru.answer_true]
        shuffle(cevaplar)
        if request.method == "POST":
            if soru.answer_true in request.POST:
                try:
                    coupling = COUPLING()
                    coupling.match_user=soru.author
                    coupling.matched_user= request.user
                    coupling.save()
                except:
                    print("hatalı kayıt")
                print("true")
                deneme = request.user.username
                print(str(deneme))
                print(request.user.username)
                print(soru.author)
            else:
                print("false")

    except:
        return HttpResponse("Soru Bulunamadı")
    return render(request,"accounts/question.html",context={"soru":soru,"cevaplar":cevaplar})

def profile_view(request,username):
    try:  
        if(request.user.is_authenticated):
            user = User.objects.get(username=username)
            questions = QUESTIONS.objects.all().filter(author_id=request.user.id)
            user_profile = PROFILE.objects.get(user_id=request.user.id)
            return render(request,"accounts/profile/profile.html",context={"user:":user,"user_profile":user_profile,"questions":questions})
    except:
        return HttpResponse("Kulanıcı bulunamadı ")


        
def user_view(request,username):
    try:
        user = User.objects.get(username=username)
        questions = QUESTIONS.objects.all().filter(author_id=user.id)
        user_profile = PROFILE.objects.get(user_id=user.id)
        return render(request,"profile.html",context={"kullanıcı":user,"user_profile":user_profile,"questions":questions})
    except:
        return HttpResponse("Kulanıcı bulunamadı ")

def ask_question(request):
    form1 = profileForm()
    if request.method == "POST":
        ask_form = askForm(request.POST)
        print("TAMAMMMMMMMMM")
        print(ask_form.is_valid())
        if ask_form.is_valid():
            soru = ask_form.save(commit=False)
            print("TAMAMMMMMMMMM22222")
            print(soru.answer_one)
            soru.author = request.user
            
            soru.save()
            return HttpResponse("BAŞARILI")
    else:
        ask_form = askForm()
    return render(request,"accounts/ask_question.html",context={"ask_form":ask_form,"prof":form1})




class QuestionLikeToggle(RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        id      = self.kwargs.get("id")
        soru    = get_object_or_404(QUESTIONS,id=id)
        url_    = soru.get_absolute_url()
        user    = self.request.user
        if user.is_authenticated:
            if user in soru.likes.all():
                soru.likes.remove(user)
            else:
                soru.likes.add(user)
        return url_ 

    #base deneme silinecek

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class QuestionLikeAPIToggle(APIView):
  
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request,id,format=None):
        id      = self.kwargs.get("id")
        soru    = get_object_or_404(QUESTIONS,id=id)
        url_    = soru.get_absolute_url()
        user    = self.request.user
        updated = False
        liked   = False
        if user.is_authenticated:
            if user in soru.likes.all():
                liked = False
                soru.likes.remove(user)
            else:
                liked = True
                soru.likes.add(user)
            updated = True
        data    ={
            "updated"   :updated,
            "liked"     :liked,
        }
        return Response(data) 

from rest_framework.views  import APIView
from rest_framework import generics, permissions
from rest_framework.authtoken.models  import Token
#REST API ICIN 

class Register(generics.CreateAPIView):
    def post(self,request,*args,**kwargs):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        serializer = serializer.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #GENERATE TOKEN
        token = Token.objects.create(user= user)
        return Response({'detail':'User has been created with token'+token.key})


from .serializers import LoginSerializer
class Restlogin(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request,user)
        token,created = Token.objects.get_or_create(user=user)

        return Response({"token":token.key},status=201)
    



def base(request):
    return render(request,"accounts/base.html")

def deneme(request):
    return render(request,"deneme.html")



    
