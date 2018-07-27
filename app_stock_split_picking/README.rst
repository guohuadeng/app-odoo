.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============
Split picking
=============

This module adds a "Split" button on the outgoing pickings form.

It works like the classical picking Transfer but it leaves both pickings
(picking and its backorder) as confirmed without processing the transfer.

Installation
============

This module only needs `stock` module.

Usage
=====

To use this module, you need to:

#. Go to **Inventory** dashboard and open any picking.
#. If picking state is **available** you can see an split button.
#. On the "Operations" tab, fill the field "Done" to the quantity you want to
   split for each line.
#. If you click on **Split** button, wizard will split current picking into
   two different pickings depends on quantity done you entered above.
#. Both pickings remain confirmed.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/154/11.0

Known issues / Roadmap
======================

* When splitting a picking in an unassigned state, wizard won't
  be auto completed with picking lines.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/stock-logistics-workflow/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======
Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.png>`_.

Contributors
------------

* Nicolas Bessi <nicolas.bessi@camptocamp.com>
* Guewen Baconnier <guewen.baconnier@camptocamp.com>
* Yannick Vaucher <yannick.vaucher@camptocamp.com>
* Vicent Cubells <vicent.cubells@tecnativa.com>
* Julien Coux <julien.coux@camptocamp.com>

Do not contact contributors directly about support or help with technical issues.

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
