from django.views.generic import View
from django.http import JsonResponse
from .models import Key
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.


class GetKey(View):
    def get(self, request):
        key = Key.objects.filter(status=0)[0]
        key.status = '1'
        key.save()
        return JsonResponse({"key": key.key, "status": key.get_status_display()})


@method_decorator(csrf_exempt, name="dispatch")
class UseKey(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        try:
            key = data["key"]
        except KeyError:
            return JsonResponse({"error": "Not valid json"})

        try:
            key = Key.objects.get(key=key, status='1')
        except Key.DoesNotExist:
            return JsonResponse({"error": "Key does not exist, issued or used"})

        key.status = '2'
        key.save()
        return JsonResponse({"success": True})


@method_decorator(csrf_exempt, name="dispatch")
class CheckKey(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))

        try:
            key = data["key"]
        except KeyError:
            return JsonResponse({"error": "Not valid json"})

        try:
            key = Key.objects.get(key=key)
        except Key.DoesNotExist:
            return JsonResponse({"error": "Key does not exist"})

        return JsonResponse({"key": key.key, "status": key.get_status_display()})


class CountKeys(View):
    def get(self, request):
        keys = Key.objects.filter(status=0).count()
        return JsonResponse({"Not issued keys": keys})
