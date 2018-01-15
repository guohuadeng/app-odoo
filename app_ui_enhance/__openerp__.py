# -*- coding: utf-8 -*-

# Created on 2017-11-05
# author: 广州尚鹏，http://www.sunpop.cn
# email: 300883@qq.com
# resource of Sunpop
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Odoo在线中文用户手册（长期更新）
# http://www.sunpop.cn/documentation/user/10.0/zh_CN/index.html

# Odoo10离线中文用户手册下载
# http://www.sunpop.cn/odoo10_user_manual_document_offline/
# Odoo10离线开发手册下载-含python教程，jquery参考，Jinja2模板，PostgresSQL参考（odoo开发必备）
# http://www.sunpop.cn/odoo10_developer_document_offline/
# description:
{
    'name': 'App Web UI Enhance(Search by date or number range,List background color,Barcode Setting.)',
    'version': '10.0.1.0',
    'author': 'Sunpop.cn',
    'category': 'web',
    'website': 'http://www.sunpop.cn',
    'license': 'AGPL-3',
    'sequence': 2,
    'summary': """
    UI Enhance for Odoo. 
    1.Search by date or number range in List view and Pivot view. 
    2.Instructions for Activating List background color property. 
    3.Reset the barcode format.
    """,
    'description': """

1.Search by date or number range in List view and Pivot view
--------------------------------------------------
2.Instructions for Activating List background color property

Just add tree attribute like style and colors with condition you want.

bg_colors="grey:state=='cancel';green:state=='draft';blue:state in ('done');red:state in ('waiting')"


eg.

    <record id="view_demo_tree" model="ir.ui.view">
        <field name="name">demo.tree</field>
        <field name="model">demo.model</field>
        <field name="arch" type="xml">
            <tree bg_colors="grey:state=='cancel';green:state=='draft';blue:state in ('done');red:state in ('sale')" name="demo_tree">
                <field name="name" string="Appointment" />
                <field name="state" />
            </tree>
        </field>
    </record>
--------------------------------------------------

    """,
    'depends': ['web', 'app_odoo_customize'],
    'data': [
        'views/app_ui_config_settings_view.xml',
        'views/template_view.xml',
        # data
        'data/ir_config_parameter.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    "price": 68.00,
    "currency": "EUR",

    'images': ['static/description/list_pivot.png'],

    'installable': True,
    'auto_install': False,
    'application': True,
}
