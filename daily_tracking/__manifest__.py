{
    'name': "S&t DATA",
    'author': "Leano Sesanyane",
    'depends': ['base', 'web','mail'],
    # Puts the app at the top of the app list
    'sequence': -10,
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/snt_daily_tracker.xml",
        "views/snt_arrangements.xml",
        "views/snt_book.xml",
        "views/snt_matter.xml",
        "views/snt_payments.xml",
        "views/snt_campaign_register.xml",
        "views/snt_confirmations.xml",
        "views/snt_scripts.xml",
        "views/snt_call_flow.xml",
        "views/snt_debt_type.xml", 
        "views/snt_menus.xml",
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    # This will make your module available when searching in apps
    'application': True
}
