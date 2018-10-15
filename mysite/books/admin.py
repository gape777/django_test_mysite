# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Publisher, Author, Book
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    # 查询框
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    # 列表显示的字段
    list_display = ('title', 'publisher', 'publication_date')
    # 过滤器
    list_filter = ('publication_date',)
    # 过滤器2
    date_hierarchy = 'publication_date'
    # 字段排序
    ordering = ('-publication_date',)
    # 显示字段
    fields = ('title', 'authors', 'publisher', 'publication_date')
    # 过滤多选框
    filter_horizontal = ('authors',)
    # 外键显示方式
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
