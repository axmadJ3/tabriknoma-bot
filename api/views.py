from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from api.models import Customer, Category, Event
from api.serializers import CustomerSerializer, CategorySerializer, EventSerializer


class CustomerRegisterView(CreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer


@api_view(['GET'])
def get_customer_view(request):
    telegram_id = request.GET.get('telegram_id')
    print(telegram_id)
    customer = Customer.objects.filter(telegram_id=telegram_id)
    if customer:
        customer = CustomerSerializer(customer.last()).data
        return Response({'customer': customer})
    else:
        return Response({}, 404)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['GET'])
def events_view(request):
    category_name = request.GET.get('category')
    category = Category.objects.filter(name=category_name).last()
    events = Event.objects.filter(category=category)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)
    