# Django imports
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def is_manager_or_superuser(method):

  def wrap(request, *args, **kwargs):
      is_manager_or_superuser = hasattr(request.user, 'manager') or request.user.is_superuser
      if is_manager_or_superuser:
          return method(request, *args, **kwargs)
      else:
          raise PermissionDenied

  return wrap  


def is_manager(method):

    def wrap(request, *args, **kwargs):
        is_manager = hasattr(request.user, 'manager')
        if is_manager:
            return method(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap