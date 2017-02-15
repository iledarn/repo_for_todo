# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProjectTaskTodo(models.Model):
    _name = "project.task.todo"
    _inherit = 'mail.thread'
    done = fields.Boolean(track_visibility="onchange")
    name = fields.Char()
    reviewer_id = fields.Many2one('res.users', 'Reviewer', select=True)
    user_id = fields.Many2one('res.users', 'Assigned to', select=True)
    task_id = fields.Many2one('project.task', 'Task', ondelete='cascade', required=True, select="1")
    _track = {
        'done': {
            'todo_project.mt_todo_done': lambda self, cr, uid, obj, ctx=None: obj.done,
        }
    }


class Task(models.Model):
    _inherit = "project.task"
    todo_ids = fields.One2many('project.task.todo', 'task_id', 'To do')

