=================
Dynamic Product Pack eCommerce
=================

.. |License| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

|License|

Este modulo añade la funcionalidad de crear paquetes dinámicos dentro del *Sitio Web*.

**Tabla de contenidos**

.. contents::
   :local:

Uso & Configuración
=====

Para usar este modulo necesitas:

#. Ir a  *Ventas > Productos > Productos*, crear or seleccionar un producto y marcar
   *Is Pack?*
#. Se habilitará la ventana "Configuración de paquete".
  * En el campo "Grupos" se añaden los grupos de producto previamente creado y asignados
    a estos.
  * En el campo "Tamaño de paquete" se define cuantos espacios tendrá disponible.
  * En el campo "Cantidad por grupo" se define separado por comas sin espacios; la
    cantidad exacta de productos por grupo.
  * El campo "Precio de paquete" es una referencia del precio del producto.


#. Al crear el *Paquete* aparece en el campo "Enlace paquete" la url para crearlo en
   el sitio web.
#. Al acceder a este enlace en la web podemos conformar nuestro *Paquete dinámico*.
#. Una vez añadido al carrito solo se podrá remover el paquete y no las lineas de este.


Conoce los problemas
======================

* Si se crea un *Paquete* y no se le añade grupos no aparecerán productos para
  añadir a este en el sitio web.
* Si se añaden espacios dentro de el campo "Cantidad por grupo" no se calculará
  bien si el paquete está listo, por lo tanto no se podrá añadir al carrito.

Rastreo de errores
===========

* ToDo

Credits
=======

Authores
~~~~~~~

* `Octupus Technologies S.L. <https://octupus.es>`_
* `Yhasmani Valdes <mailto:yvaldes@octupus.es>`_

Contribuidores
~~~~~~~~~~~~

* `Marcos Jaime <mailto:marcos.jaime@octupus.es>`_


Mantenedores
~~~~~~~~~~~

Este modulo es mantenido por `Octupus Technologies S.L. <https://octupus.es>`_

.. image:: https://www.octupus.es/wp-content/uploads/2021/05/logo-octupus-odoo-madrid-gold-partner-shopify-prestashop_main.png
   :alt: Octupus Technologies
   :target: https://octupus.es
