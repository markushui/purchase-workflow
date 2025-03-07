import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-partner_supplierinfo_smartbutton>=16.0dev,<16.1dev',
        'odoo-addon-procurement_purchase_no_grouping>=16.0dev,<16.1dev',
        'odoo-addon-product_main_seller>=16.0dev,<16.1dev',
        'odoo-addon-product_supplier_code_purchase>=16.0dev,<16.1dev',
        'odoo-addon-product_supplierinfo_purchase_contact>=16.0dev,<16.1dev',
        'odoo-addon-product_supplierinfo_qty_multiplier>=16.0dev,<16.1dev',
        'odoo-addon-purchase_advance_payment>=16.0dev,<16.1dev',
        'odoo-addon-purchase_all_shipments>=16.0dev,<16.1dev',
        'odoo-addon-purchase_allowed_product>=16.0dev,<16.1dev',
        'odoo-addon-purchase_blanket_order>=16.0dev,<16.1dev',
        'odoo-addon-purchase_cancel_reason>=16.0dev,<16.1dev',
        'odoo-addon-purchase_commercial_partner>=16.0dev,<16.1dev',
        'odoo-addon-purchase_date_planned_manual>=16.0dev,<16.1dev',
        'odoo-addon-purchase_default_terms_conditions>=16.0dev,<16.1dev',
        'odoo-addon-purchase_delivery_split_date>=16.0dev,<16.1dev',
        'odoo-addon-purchase_deposit>=16.0dev,<16.1dev',
        'odoo-addon-purchase_discount>=16.0dev,<16.1dev',
        'odoo-addon-purchase_exception>=16.0dev,<16.1dev',
        'odoo-addon-purchase_fop_shipping>=16.0dev,<16.1dev',
        'odoo-addon-purchase_force_invoiced>=16.0dev,<16.1dev',
        'odoo-addon-purchase_force_invoiced_quantity>=16.0dev,<16.1dev',
        'odoo-addon-purchase_invoice_method>=16.0dev,<16.1dev',
        'odoo-addon-purchase_invoice_plan>=16.0dev,<16.1dev',
        'odoo-addon-purchase_landed_cost>=16.0dev,<16.1dev',
        'odoo-addon-purchase_last_price_info>=16.0dev,<16.1dev',
        'odoo-addon-purchase_line_procurement_group>=16.0dev,<16.1dev',
        'odoo-addon-purchase_location_by_line>=16.0dev,<16.1dev',
        'odoo-addon-purchase_lot>=16.0dev,<16.1dev',
        'odoo-addon-purchase_manual_delivery>=16.0dev,<16.1dev',
        'odoo-addon-purchase_merge>=16.0dev,<16.1dev',
        'odoo-addon-purchase_no_rfq>=16.0dev,<16.1dev',
        'odoo-addon-purchase_only_by_packaging>=16.0dev,<16.1dev',
        'odoo-addon-purchase_open_qty>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_approved>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_archive>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_downpayment>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_general_discount>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_hide_receipt_status>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_line_menu>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_line_receipt_status>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_line_sequence>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_line_stock_available>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_no_zero_price>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_owner>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_price_recalculation>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_product_attachment_mgmt>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_product_recommendation>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_purchase_manager>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_qty_change_no_recompute>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_secondary_unit>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_supplier_return>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_supplierinfo_update>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_type>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_type_dashboard>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_uninvoiced_amount>=16.0dev,<16.1dev',
        'odoo-addon-purchase_order_weight_volume>=16.0dev,<16.1dev',
        'odoo-addon-purchase_packaging_default>=16.0dev,<16.1dev',
        'odoo-addon-purchase_packaging_level_qty>=16.0dev,<16.1dev',
        'odoo-addon-purchase_partner_incoterm>=16.0dev,<16.1dev',
        'odoo-addon-purchase_partner_selectable_option>=16.0dev,<16.1dev',
        'odoo-addon-purchase_product_packaging_container_deposit>=16.0dev,<16.1dev',
        'odoo-addon-purchase_quick>=16.0dev,<16.1dev',
        'odoo-addon-purchase_reception_status>=16.0dev,<16.1dev',
        'odoo-addon-purchase_reorder_control>=16.0dev,<16.1dev',
        'odoo-addon-purchase_request>=16.0dev,<16.1dev',
        'odoo-addon-purchase_request_department>=16.0dev,<16.1dev',
        'odoo-addon-purchase_request_exception>=16.0dev,<16.1dev',
        'odoo-addon-purchase_request_tier_validation>=16.0dev,<16.1dev',
        'odoo-addon-purchase_request_type>=16.0dev,<16.1dev',
        'odoo-addon-purchase_requisition_tier_validation>=16.0dev,<16.1dev',
        'odoo-addon-purchase_return>=16.0dev,<16.1dev',
        'odoo-addon-purchase_sale_link_by_origin>=16.0dev,<16.1dev',
        'odoo-addon-purchase_security>=16.0dev,<16.1dev',
        'odoo-addon-purchase_sign>=16.0dev,<16.1dev',
        'odoo-addon-purchase_stock_packaging>=16.0dev,<16.1dev',
        'odoo-addon-purchase_stock_price_unit_sync>=16.0dev,<16.1dev',
        'odoo-addon-purchase_tag>=16.0dev,<16.1dev',
        'odoo-addon-purchase_tier_validation>=16.0dev,<16.1dev',
        'odoo-addon-purchase_transport_mode>=16.0dev,<16.1dev',
        'odoo-addon-purchase_triple_discount>=16.0dev,<16.1dev',
        'odoo-addon-purchase_vendor_promotion>=16.0dev,<16.1dev',
        'odoo-addon-purchase_warn_message>=16.0dev,<16.1dev',
        'odoo-addon-purchase_work_acceptance>=16.0dev,<16.1dev',
        'odoo-addon-sale_purchase_force_vendor>=16.0dev,<16.1dev',
        'odoo-addon-supplier_calendar>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
