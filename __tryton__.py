#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Stock Supply Management',
    'name_de_DE': 'Lagerverwaltung Beschaffung',
    'name_fr_FR': 'Gestion des approvisionnements de stock',
    'version': '0.0.1',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': '''Supply Management Module with:
    - Order point
    - Purchase Request

With schedulers:
    - to generate purchase request based on order points
    - to generate internal packing based on order points
''',
    'description_de_DE': '''Beschaffungsmodul mit:
    - Bestellpunkten
    - Auftragserstellung

Mit automatischer Auftragserstellung per Zeitplaner:
    - um Bestellungen auf der Basis von Bestellpunkten zu erstellen
    - um internen Versand auf der Basis von Bestellpunkten zu erstellen
''',
    'description_fr_FR': '''Module de gestion des approvisionnements avec:
    - Règles d'approvisionnement
    - Demandes d'achat

Et les planificateurs pour générer:
    - des demandes d'achat et
    - des colisages internes
sur base des règles d'approvisionnement
''',

    'depends': [
        'ir',
        'res',
        'product',
        'stock',
        'purchase',
        'party',
    ],
    'xml': [
        'order_point.xml',
        'purchase_request.xml',
        'packing.xml',
    ],
    'translation': [
        'de_DE.csv',
        'es_ES.csv',
        'fr_FR.csv',
    ]
}
