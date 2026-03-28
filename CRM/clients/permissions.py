from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class RoleRequiredMixin: # LoginRequiredMixin
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in self.allowed_roles:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)