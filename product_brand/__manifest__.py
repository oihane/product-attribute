# © 2009 NetAndCo (<http://www.netandco.net>).
# © 2011 Akretion Benoît Guillot <benoit.guillot@akretion.com>
# © 2014 prisnet.ch Seraphine Lantible <s.lantible@gmail.com>
# © 2016-Today Serpent Consulting Services Pvt. Ltd.
#    (<http://www.serpentcs.com>)
# © 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Product Brand Manager',
    'version': '11.0.1.0.1',
    'category': 'Product',
    'summary': "Product Brand Manager",
    'author': 'NetAndCo, Akretion, Prisnet Telecommunications SA'
              ', MONK Software, Odoo Community Association (OCA)'
              ', SerpentCS Pvt. Ltd., Apertoso N.V.',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        ],
    'data': [
        'views/product_brand_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False
}
