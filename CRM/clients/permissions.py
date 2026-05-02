from typing import Any

from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.views import View


class RoleRequiredMixin(View):
    allowed_roles: list[str] = []

    def dispatch(
        self,
        request: HttpRequest,
        *args: Any,
        **kwargs: Any,
    ) -> HttpResponse:
        if request.user.role not in self.allowed_roles:
            return HttpResponseForbidden(
                "You do not have permission to access this page."
            )

        return super().dispatch(request, *args, **kwargs)
