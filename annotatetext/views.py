from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest, \
    HttpResponseForbidden, HttpResponseNotAllowed

from annotatetext.forms import NewAnnotationForm
from annotatetext.models import Annotation

def post_annotation(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    if request.user.is_anonymous():
        return HttpResponseForbidden(_("Sorry, only logged users can annotate."))
    form = NewAnnotationForm(request.POST)
    if form.is_valid():
        new_annotation = Annotation(content_type=form.cleaned_data["content_type"],
                    object_id=form.cleaned_data["object_id"],
                    user=request.user,
                    selection_start=form.cleaned_data["selection_start"],
                    selection_end=form.cleaned_data["selection_end"],
                    comment=form.cleaned_data["comment"],
                    flags=form.cleaned_data["flags"],
                    color=form.cleaned_data["color"])
        new_annotation.save()
        return HttpResponseRedirect(new_annotation.get_absolute_url())
    else:
        return HttpResponseBadRequest()

def delete_annotation(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    if request.user.is_anonymous() or not request.user.is_staff:
        return HttpResponseForbidden(_("Sorry, only staff meembers can delete annotations."))
    if not "annotation_id" in request.POST:
        return HttpResponseBadRequest()
    try:
        annoid = int(request.POST["annotation_id"])
    except (TypeError, ValueError):
        return HttpResponseBadRequest()
    annotation = get_object_or_404(Annotation, id=annoid)
    content_url = annotation.content_object.get_absolute_url()
    annotation.delete()
    return HttpResponseRedirect(content_url)
