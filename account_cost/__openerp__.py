# -*- coding: utf-8 -*-
{
    'name': "GOODERP 费用模块",
    'author': "德清武康开源软件工作室",
    'website': "无",
    'category': 'gooderp',
    "description":
    '''
                        该模块实现了费用通结算单（往来）管理的功能，将费用按入库金额分摊至不同的出入库单。
    ''',
    'version': '11.11',
    'depends': ['buy'],
    'data': [
        'views/cost_order_view.xml',
        'views/cost_action.xml',
        'views/cost_menu.xml',
        'security/ir.model.access.csv',
        'security/cost_sequence.xml',
    ],
    'demo': [
             'data/cost_order_demo.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
}
