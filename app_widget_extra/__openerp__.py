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

# base on 'author': "Gilvan Leal",
# website': "https://gilvanleal.github.io/odoowidgets/",
{
    'name': "App widget extra(Inputmask Widget)",
    'author': "广州欧度智能",
    'website': 'http://www.sunpop.cn',
    'currency': 'EUR',
    'price': 38,

    'summary': """
   A Widget to make masks on form fields""",

    'description': """
================
Inputmask Widget
================

Based on jquery.inputmask 3.x `Docs in GitHub
<http://robinherbots.github.io/Inputmask/>`_.

| An Inputmask Widget helps the user with the input by ensuring a predefined format.
| This can be useful for dates, numerics, phone numbers, ...

Instructions:
-------------

- Just add attribute *widget="mask"* and *data-inputmask[-<attribute>]="<value>"* to **<field />** on form, tree and kanban

   Some examples::

    <field widget="mask" data-inputmask="'alias': 'date'" name="name" />
    <field widget="mask" data-inputmask="'mask': '99/99/9999'" name="name" />
    <field widget="mask" data-inputmask="'mask': '99-aa-**-AA-&amp;&amp;-##'" name="name" />
    <field widget="mask" data-inputmask="'mask': '9', 'repeat': 10, 'greedy' : false" name="name" />

   Or::

     <field widget="mask" data-inputmask-alias="date" name="name" />
     <field widget="mask" data-inputmask-mask="99/99/9999" name="name" />
     <field widget="mask" data-inputmask-mask="99-aa-**-AA-&amp;&amp;-##" name="name" />
     <field widget="mask" data-inputmask-mask="9" data-inputmask-repeat="10" data-inputmask-greedy="false" name="name" />

   **Note:** Use *contenteditable="true"* for apply mask in others HTML tags: span, div, etc. **Improve**


- Just add attribute *widget="mask_regex"* and *data-inputmask[-regex]="<value>"* to **<field />**

   With the regex extension you can use any regular expression as a mask. Currently this does only input restriction. There is no further masking visualization.

   Example email validation::

    <field widget="mask_regex" data-inputmask-regex="[a-zA-Z0-9._%-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}" name="name"/>

- Masking definition:

   :9: Numeric value
   :a: Alphabetical value
   :\*: Alphanumeric value
   :A: Alphabetical uppercasing
   :&: Alfanumeric uppercasing - (Use **&amp;** for escape **&** in XML file)
   :#: Hexadecimal

- Attributes:

   :mask: The mask to use.
   :repeat: Mask repeat function. Repeat the mask definition x-times.
   :greedy: Toggle to allocate as much possible or the opposite. Non-greedy repeat function.
   :placeholder: Change the mask placeholder. Default: "_"
   :autounmask: Automatically unmask the value when retrieved. Default: false.
   :removemaskonsubmit: Remove the mask before submitting the form.Default: false
   :clearmaskonlostfocus: Remove the empty mask on blur or when not empty removes the optional trailing part Default: true
   :insertmode: Toggle to insert or overwrite input. Default: true.
   :clearincomplete: Clear the incomplete input on blur.
   :alias: The alias to use.

- Aliases:

   Some aliases found in the extensions are: email, currency, decimal, integer, date, datetime, dd/mm/yyyy, url, ip, etc.

   Docs:

   * `Date and Datetime <https://github.com/RobinHerbots/Inputmask/blob/3.x/README_date.md>`_
   * `Numeric <https://github.com/RobinHerbots/Inputmask/blob/3.x/README_numeric.md>`_
   * `Regex <https://github.com/RobinHerbots/Inputmask/blob/3.x/README_regex.md>`_
   * `Phone <https://github.com/RobinHerbots/Inputmask/blob/3.x/README_phone.md>`_
   * `Other <https://github.com/RobinHerbots/Inputmask/blob/3.x/README_other.md>`_""",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    "data": ['views/inputmask_templates.xml'],
    "qweb": ['static/src/xml/*.xml'],
    'images': ['static/description/main_screenshot.png']
}
