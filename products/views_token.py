from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class TokenFormView(TokenObtainPairView):
    template_name = 'products/token_form.html'

    @method_decorator(csrf_exempt)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # If response is JSON, pass it to template
        try:
            data = response.data
        except Exception:
            data = None
        return render(request, self.template_name, {'token_data': data})
