from django.utils.text import slugify


def slugify_instance_title(instance, new_slug=None, save=False):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Class = instance.__class__
    qs = Class.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        num = instance.id
        slug = f'{slug}-{num}'
        return slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
