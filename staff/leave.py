# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError
import time,datetime

# 请假单审核状态可选值
LEAVE_STATES = [
    ('draft', u'未审核'),
    ('done', u'已审核'),]

class staff_leave(models.Model):
    _name = 'staff.leave'

    @api.model
    def _set_staff_id(self):
        return self.env.uid

    name = fields.Text(string=u'请假缘由',
                readonly = True,
               states = {'draft': [('readonly', False)]},
    )
    user_id = fields.Many2one('res.users',
                              string=u'请假人',
                              default=_set_staff_id,
                              readonly=True,
                              states={'draft': [('readonly', False)]}
                              )
    date_start = fields.Datetime(string=u'离开时间',
                                 readonly=True,
                                 states={'draft': [('readonly', False)]}
                                 )
    date_stop = fields.Datetime(string=u'回来时间',
                                readonly = True,
                                states = {'draft': [('readonly', False)]})
    leave_type = fields.Selection([('no_pay', u'无薪'),('with_pay', u'带薪'),
                                   ('compensation_day', u'补偿日数'),('sick_leave', u'病假')],
                                    default='no_pay', string=u'准假类型',readonly = True,
                                states = {'draft': [('readonly', False)]})
    leave_dates = fields.Float(u'请假时长',readonly = True,
               states = {'draft': [('readonly', False)]})
    state = fields.Selection(LEAVE_STATES, u'审核状态', readonly=True,
                             help=u"购货订单的审核状态", index=True, copy=False,
                             default='draft')


    @api.one
    def leave_done(self):
        '''审核请假单'''
        if self.state == 'done':
            raise UserError(u'请不要重复审核！')
        self.state = 'done'


    @api.one
    def leave_draft(self):
        '''反审核请假单'''
        if self.state == 'draft':
            raise UserError(u'请不要重复反审核！')
        self.state = 'draft'