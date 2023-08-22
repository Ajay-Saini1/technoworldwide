from django.shortcuts import render
import datetime
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.html import format_html
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView
from application.custom_classes import AjayDatatableView, AdminRequiredMixin, UserRequiredMixin
from .models import Blog
from .forms import BlogForm, EditBlogForm
# from django.contrib.auth.forms import BlogChangeForm


class CreateBlogView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/form.html'
    success_message = "Blog created successfully"
    success_url = reverse_lazy('blog_list')


class ListBlogView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'blog/list.html'


class ListBlogViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Blog
    columns = ['title', 'description', 'thumbnail_image', 'actions']
    exclude_from_search_columns = ['actions']


    def get_initial_queryset(self):
        return self.model.objects.all()

    def render_column(self, row, column):

        if column == 'actions':
            edit_action = '<a href={} role="button" class="btn btn-warning btn-xs mr-1 text-white">Edit</a>'.format(
                reverse('blog_edit', kwargs={'pk': row.pk}))
            delete_action = '<a href="javascript:;" class="remove_record btn btn-danger btn-xs" data-url={} role="button">Delete</a>'.format(
                reverse('blog_delete', kwargs={'pk': row.pk}))
            return edit_action + delete_action
        if column == 'thumbnail_image':
            if row.thumbnail_image:
                image_url = row.thumbnail_image.url
                return format_html('<img src="{0}" alt="Subcategory Image" width="80" height="80">', image_url)
            else:
                return ''
        else:
            return super(ListBlogViewJson, self).render_column(row, column)


class UpdateBlogView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'blog/form.html'
    success_message = "Blog updated successfully"
    success_url = reverse_lazy('blog_list')


class DeleteBlogView(AdminRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Blog

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        payload = {'delete': 'ok'}
        return JsonResponse(payload)