# -*- coding: utf-8 -*-
from openerp import http

# class TodoProject(http.Controller):
#     @http.route('/todo_project/todo_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_project/todo_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_project.listing', {
#             'root': '/todo_project/todo_project',
#             'objects': http.request.env['todo_project.todo_project'].search([]),
#         })

#     @http.route('/todo_project/todo_project/objects/<model("todo_project.todo_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_project.object', {
#             'object': obj
#         })