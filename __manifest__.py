# -*- coding: utf-8 -*-

#    ________  __      ________  _______   ______          _______    _______   ________     __      _____  ___  ___________  _______    _______  _____  ___   
#   /"       )|" \    /"       )/"     "| /    " \        |   __ "\  /"     "| /"       )   /""\    (\"   \|"  \("     _   ")/"      \  /"     "|(\"   \|"  \  
#  (:   \___/ ||  |  (:   \___/(: ______)// ____  \       (. |__) :)(: ______)(:   \___/   /    \   |.\\   \    |)__/  \\__/|:        |(: ______)|.\\   \    | 
#   \___  \   |:  |   \___  \   \/    | /  /    ) :)      |:  ____/  \/    |   \___  \    /' /\  \  |: \.   \\  |   \\_ /   |_____/   ) \/    |  |: \.   \\  | 
#    __/  \\  |.  |    __/  \\  // ___)(: (____/ //       (|  /      // ___)_   __/  \\  //  __'  \ |.  \    \. |   |.  |    //      /  // ___)_ |.  \    \. | 
#   /" \   :) /\  |\  /" \   :)(:  (    \        /       /|__/ \    (:      "| /" \   :)/   /  \\  \|    \    \ |   \:  |   |:  __   \ (:      "||    \    \ | 
#  (_______/ (__\_|_)(_______/  \__/     \"_____/       (_______)    \_______)(_______/(___/    \___)\___|\____\)    \__|   |__|  \___) \_______) \___|\____\) 

{
    'name': "Modul Pendaftaran Santri SISFO Pesantren",

    'summary': """
        Aplikasi SISFO Pesantren
        - Modul Pendaftaran untuk SISFO Pesantren""",

    'description': """
        Aplikasi SISFO Pesantren memiliki fitur-fitur sebagai berikut :
        ===============================================================
        * Modul Base / Dasar
        * Modul Akademik
        * Modul Musyrif
        * Modul Guru
        * Modul Orang Tua
        * Modul Kesantrian
        * Modul Pendaftaran

        Developed by : 
        - Fahmi
        - Aby
        - Aliga
        - Akim

        November 2024

        Informasi Lebih lanjut, hubungi :

            PT. Universal Big Data 
            - Ruko Modern Kav A16-A17
              Jl Loncat Indah, Tasikmadu, Kota Malang
    """,

    'author': "PT. Universal Big Data",
    'website': "https://ubig.co.id",
    'category': 'Education',
    'version': '18.0.1.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'pesantren_base'],

    # always loaded
    'data': [
        # security
        'security/groups.xml',
        'security/ir.model.access.csv',

        # Data
        'data/ubig_pendaftaran_action.xml',

        # View
        'views/pendaftaran_santri.xml',
        'views/ref_bank.xml',
        'views/ref_biaya.xml',
        'views/ref_kecamatan.xml',
        'views/ref_kota.xml',
        'views/ref_provinsi.xml',
        'views/pendaftaran_form_template.xml',
        'views/pendaftaran_succses_template.xml',
        'views/pendaftaran_login_template.xml',
        'views/pendaftaran_cetak_form_pembayaran_template.xml',
        'views/pendaftaran_seleksi_template.xml',
        'views/komponen_biaya.xml',
        'views/biaya_daftarulang.xml',

        # report
        'report/ubig_pendaftaran_report.xml',
        
        # wizard
        # 'wizard/wizard_va.xml',

        # Menu
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'pendaftaran_santri/static/src/img/logoweb.png',
        ],
    },
}

