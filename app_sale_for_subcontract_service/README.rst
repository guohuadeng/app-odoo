.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================
Subcontracted services
======================

This module allows a user to indicate that a service is subcontracted.
It provides the ability to create purchases from procurement processes.

This is a base module, upon specific modules for sale / manufacuturing, modules
will need to rely on. By itself it does not provide any function to the end user.

Possible uses of this module can be:

* Add subcontracted services to BOMs. When a manufacturing order is created a
  PO is triggered for the service to be subcontracted. See

* Add subcontracted services to sales order. When the SO is confirmed, it
  creates a PO for the service.


Configuration
=============

To configure this module, you need to:

#. Configure your service product with the flag
   ``property_subcontracted_service`` in product form if this product should
   trigger a procurement.
#. Add supplier in your product form.
#. Additionally and despite a predefined rule is created in each warehouse,
   you can configure the 'Subcontracting_service procurement rule' for each
   warehouse through 'Inventory / Configuration / Warehouse Management /
   Warehouse'.

Usage
=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/142/11.0


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/purchase-workflow/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.png>`_.

Contributors
------------

* Damien Crier <damien.crier@camptocamp.com>
* Jordi Ballester Alomar <jordi.ballester@eficent.com>
* Lois Rilo <lois.rilo@eficent.com>


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
