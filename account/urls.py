# -*- coding:utf-8 -*-
# author: JXF
# created: 2018-4-27

from django.conf.urls import url
from .views import (
    UserResetPasswordView,
    UserChangeInfoView,
    UserDetailView,
    UserLoginView,
    UserBindPhoneView,
    MakeFriendView,
    FollowAndFansView,
)


urlpatterns = [
    url(r'^login/$', UserLoginView.as_view(), name='user_login'),
    url(r'^detail/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^(?P<pk>\d+)/changeInfo/$', UserChangeInfoView.as_view(), name='change_info'),
    url(r'^(?P<pk>\d+)/resetPassword/$', UserResetPasswordView.as_view(), name='reset_password'),
    url(r'^(?P<pk>\d+)/phone/$', UserBindPhoneView.as_view(), name='bind_phone'),
    url(r'^(?P<idol>\d+)/(?P<fans>\d+)/$', MakeFriendView.as_view(), name='make_friend'),
    url(r'^follow_fans/(?P<pk>\d+)/$', FollowAndFansView.as_view(), name='follow_fans')

]