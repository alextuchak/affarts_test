from rest_framework.views import APIView
from users.models import User
from django.http import JsonResponse
from .serializers import FlowerSerializers, LotCreateSerializers, OrderCreateSerializers, OrderShowSerializers
from .models import Lot, Order


class FlowerCreateView(APIView):
    serializers_class = FlowerSerializers

    def post(self, request):
        if not 'user' in request.data:
            return JsonResponse({'status': False})
        user = User.objects.filter(id=request.data["user"]).first()
        if user.type != 'seller':
            return JsonResponse({'status': False, 'message': 'only for sellers'}, status=403)
        flower_serializers = self.serializers_class(data=request.data)
        if flower_serializers.is_valid():
            flower = flower_serializers.save()
            return JsonResponse({'Status': True}, status=201)
        else:
            return JsonResponse({'Status': False}, status=403)


class LotView(APIView):

    def check_data(self, request):
        if not 'seller' in request.data:
            return {'status': False, 'message': 'user id is required!'}
        user = User.objects.filter(id=request.data["seller"]).first()
        if user.type != 'seller':
            return {'status': False, 'message': 'only for sellers!'}

    def post(self, request):
        data_check = self.check_data(request)
        if not data_check['status']:
            return JsonResponse({'status': False, 'message': data_check['message']}, status=403)
        lot_serializer = LotCreateSerializers(data=request.data)
        if lot_serializer.is_valid():
            lot_serializer.save()
            return JsonResponse({'Status': True}, status=201)
        else:
            return JsonResponse({'Status': False}, status=403)

    def put(self, request):
        data_check = self.check_data(request)
        if not data_check['status']:
            return JsonResponse({'status': False, 'message': data_check['message']}, status=403)
        if Lot.objects.filter(seller=request.data['seller'], id=request.data['lot']).exists():
            Lot.objects.filter(seller=request.data['seller'], id=request.data['lot']).update(
                visibility=request.data['visibility'])
            return JsonResponse({'status': True}, status=202)
        else:
            return JsonResponse({'Status': False}, status=403)


class OrderView(APIView):
    def check_data(self, request):
        if not 'buyer' in request.data:
            return {'status': False, 'message': 'user id is required!'}
        user = User.objects.filter(id=request.data["buyer"]).first()
        if user.type != 'buyer':
            return {'status': False, 'message': 'only for buyers!'}
        return {"status": True}

    def get(self, request):
        serializer = OrderShowSerializers(Order.objects.filter(buyer=request.query_params["id"]), many=True, )
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data_check = self.check_data(request)
        if not data_check['status']:
            return JsonResponse({'status': False, 'message': data_check['message']}, status=403)
        order_serializers = OrderCreateSerializers(data=request.data)
        if order_serializers.is_valid():
            order_serializers.save()
            return JsonResponse({'Status': True}, status=201)
        else:
            return JsonResponse({'Status': False}, status=403)
