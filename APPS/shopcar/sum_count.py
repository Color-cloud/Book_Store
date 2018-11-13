from django.db.models import Sum
from APPS.shopcar.models import Shopcar


def book_count(request):
    count = 0
    uid = request.user.id
    if request.user.is_authenticated():
        count = Shopcar.objects.filter(user_id_id=uid, is_delete=0).aggregate(
            sum=Sum('count')).get('sum')
    return {'count': count}
