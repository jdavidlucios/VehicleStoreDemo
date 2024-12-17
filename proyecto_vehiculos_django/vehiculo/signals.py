from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Vehiculo

@receiver(post_save, sender=User)
def assign_permission(sender, instance, created, **kwargs):
    if created:  # Solo al crear el usuario
        content_type = ContentType.objects.get_for_model(Vehiculo)
        permission = Permission.objects.get(
            codename='visualizar_catalogo',
            content_type=content_type
        )
        instance.user_permissions.add(permission)
