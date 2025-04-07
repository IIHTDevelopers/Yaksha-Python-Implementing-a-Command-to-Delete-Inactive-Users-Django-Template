from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import logging

class RestrictAccessMiddleware(MiddlewareMixin):
    ALLOWED_IPS = ['192.168.1.1', '203.0.113.5']  # Add allowed IPs here
    logger = logging.getLogger(__name__)

    def process_request(self, request):
        user_ip = self.get_client_ip(request)
        if user_ip not in self.ALLOWED_IPS:
            return JsonResponse({'error': 'Forbidden'}, status=403)
        return None

    def get_client_ip(self, request):
        """Get the client IP address from the request headers."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
