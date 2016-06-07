# -*- coding: utf-8 -*-
import logging
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

logger = logging.getLogger('sca')


class FormsetMixin(object):
    """FormsetMixin

    """
    formset_class = None
    form_extra_fields = {}

    def get(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = self.get_form(self.formset_class)
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formset = self.get_form(self.formset_class)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        if self.form_extra_fields:
            self.object = form.save(commit=False)
            for name, value in self.form_extra_fields.items():
                setattr(self.object, name, value)
            self.object.full_clean()
            self.object.save()
        else:
            self.object = form.save()

        formset.instance = self.object
        formset.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )


class AjaxRequestMixin(object):
    """AjaxTemplateMixin

    """
    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            return super(AjaxRequestMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404
