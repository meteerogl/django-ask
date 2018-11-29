from django.conf.urls import url
from .views import *



app_name = "accounts"
urlpatterns = [
    url(r"login/",login_view,name ="login"),
    url(r"wall/",wall,name ="wall"),
    url(r"ask/",ask_question,name="ask-question"),
    url(r"logout/",logout_view,name ="logout"),
    url(r"question/(?P<id>[-\w]+)/$",view=question,name="question"),
    url(r"deneme/",deneme,name ="deneme"),
    url(r"^question/(?P<id>[-\w]+)/like/$",view=QuestionLikeToggle.as_view(),name="like-toggle"),
    url(r"^api/question/(?P<id>[-\w]+)/like/$",view=QuestionLikeAPIToggle.as_view(),name="like-api-toggle"),
    url(r"^(?P<username>[-\w]+)/$",profile_view,name="account-profile"),

    #base deneme silinecek

    url(r"base/",base,name ="base")
]