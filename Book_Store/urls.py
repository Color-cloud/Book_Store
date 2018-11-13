import xadmin
from django.conf.urls import url, include

from APPS.shouye import views

urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('ueditor/', include('DjangoUeditor.urls')),
    url('^$', views.shouye),
    url('account/',include("APPS.account.urls")),
    url('biaoqian/', include("APPS.biaoqian.urls")),
    url('search/', include("APPS.search.urls")),
    url('book_detail/', include("APPS.book_detail.urls")),
    url('shopcar/', include("APPS.shopcar.urls")),
    url('dingdan/', include("APPS.dingdan.urls")),
    url('pay/', include("APPS.mypay.urls")),

]
