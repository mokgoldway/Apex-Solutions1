# -*- coding: utf-8 -*-
{
    'name': "Apex Shipping Manifest",
    'summary': """ Shipping Manifest""",
    'description': """
Shipping Manifest
=================
* [2040902]
    - PAGE 1
        1. Description of Fields present in manifest:
        2. INVOICE/MANIFEST NUMBER: This will be the Sales Order number – pull from name field on sale.order
        3. ATTACHED PAGE(S)? to be typed in manually by client
        4. ACTUAL DATE AND TIME OF DEPARTURE: to be typed in manually by client
        5. ESTIMATED DATE AND TIME OF ARRIVAL: to be typed in manually by client
        6. SHIPPER INFORMATION: Will be a drop down Many to One field to add the Contact from -res.partner view:
            1. State License Number: Present on res.partner Form
            2. Type of License: Present on res.partner Form
            3. Business Name: Name of res.partner
            4. Business Address: Address on res.partner
            5. City, State, Zip Code: Present on res.partner Form
            6. Phone Number: Present in res.partner Form
            7. CONTACT NAME: Selection field to pull from Employees - hr.employee
        7. RECEIVER INFORMATION: This will be the Customer on the sales.order
            1. State License Number: Present on contact Form res.partner
            2. Type of License: Present on res.partner Form
            3. Business Name: Name of res.partner
            4. Delivery Address: Address on res.partner
            5. City, State, Zip Code: Present on res.partner
            6. Phone Number: Present in res.partner Form
        8. DISTRIBUTOR INFORMATION: Always takes the info selected in the SHIPPER INFORMATION fields above
            1. State License Number: Present on res.partner Form
            2. Type of License: Present on res.partner
            3. Business Address: Address on res.partner
            4. City, State, Zip Code: Present on res.partner Form
            5. Phone Number: Present in res.partner Form
            6. CONTACT NAME: Always takes the info selected in the SHIPPER INFORMATION contact name field above
            7. Drivers Info:
                1. DRIVER’S NAME: Selection field to pull from Employees in hr.employee
                2. CA DRIVER’S LICENSE# : Present in Employee contact hr.employee view – x_studio_drivers_license_no_1
                3. VEHICLE MAKE: To pull from model_id in fleet.vehicle view when VEHICLE LIC. PLATE field is selected
                4. VEHICLE MODEL:  To pull from model_id in fleet.vehicle view when VEHICLE LIC. PLATE field is selected
                5. VEHICLE LIC. PLATE #: Selection field to pull from license_plate in fleet.vehicle view or leave blank so client can type in
                    - When the selection pulls from fleet.vehicle, the Vehicle Make and Model fields above will pull from the record selected
                6. ACTUAL DATE AND TIME OF ARRIVAL: to be typed in manually by client
        9. PRODUCT SHIPPED DETAILS:
            1. Detail products as per sale.order.line on sale.order
                1. UID TAG NUMBER: UID Tag number field on Product.template x_studio_uid_tag_number
                2. ITEM NAME AND PRODUCT DESCRIPTION: product_id on sale order line
                3. QTY ORDERED: Pull from product_uom_qty on sale order line
                4. QTY REC’D: same as QTY ORDERED field above
                5. UNIT COST: pull from price_unit on sale order line
                6. TOTAL COST: pull from price_subtotal on sale order line
                7. UNIT RETAIL VALUE: same as UNIT COST field above
                8. TOTAL RETAIL VALUE: same as TOTAL COST field above
            2. When Back order is generated: Detail products as per stock.picking
    - PAGE 2
        1. INVOICE/MANIFEST NUMBER ATTACHED TO: This will be the Sales Order number – pull from name field on sale.order
        2. ATTACHED PAGE: to be typed in manually by client
        3. PRODUCT SHIPPED DETAILS: detail products as per sale.order.line on sale.order when needed (not enough lines on page 1)
        4. Fields in all other sections of the document are to be left blank. Client will manually hand write details.
""",
    'author': "Odoo Inc",
    'website': "https://www.odoo.com",
    'category': 'Custom',
    'version': '0.1',
    'depends': ['sale_management', 'sale_stock', 'hr', 'fleet'],
    'data': [
        # DATA
        'data/paperformat_data.xml',
        # security
        'security/ir.model.access.csv',

        # VIEWS
        'views/metrc_license_view.xml',
        'views/stock_picking_views.xml',
        'views/partner_view.xml',
        'views/sale_views.xml',
        'views/company_view.xml',

        # REPORT
        'report/shipping_manifest_report_view.xml',
    ],
    'demo': [
    ],
}
