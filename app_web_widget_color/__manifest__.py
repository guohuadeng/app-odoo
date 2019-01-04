# Odoo, Open Source Web Widget Color
# Copyright (C) 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# Copyright (C) 2014 Anybox <http://anybox.fr>
# Copyright (C) 2015 Taktik SA <http://taktik.be>
# Copyright (C) 2018 Alexandre Díaz <dev@redneboa.es>
# Copyright (C) 2018 Ivan deng <300883@qq.com>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "App Web Widget Color",
    'category': "web",
    'version': "11.0.11.04",
    "author": "Sunpop.cn",
    'price': 38.00,
    'currency': 'EUR',
    'summary': """
    Use for quick select color. can be use in product attribute and other color variant. color widget. color pick.
    """,
    'images': ['static/description/banner.png'],
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'view/web_widget_color_view.xml',
    ],
    'qweb': [
        'static/src/xml/widget.xml',
    ],
    'license': 'AGPL-3',
    'auto_install': False,
    'installable': True,
    'web_preload': True,
}
