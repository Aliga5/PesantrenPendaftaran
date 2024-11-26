from odoo import models, fields, api
import random
import hashlib
from datetime import datetime

class ResPartner(models.Model):
    _inherit            = 'res.partner'

    virtual_account     = fields.Char(string='Virtual Account', store=True)
    va_saku     = fields.Char(string='No. VA Uang Saku', store=True)
    bank                = fields.Many2one('ubig.bank', string="Bank", help="Pilih bank untuk membuat virtual account")
    petunjuk_pembayaran = fields.Text(related='bank.petunjuk_pembayaran', string="Petunjuk Pembayaran")
    jns_partner         = fields.Selection(
        string='Jenis Partner',
        selection=[('siswa', 'Siswa'), ('ortu', 'Orang Tua'), ('guru', 'Guru'), ('umum', 'Umum'), ('calon_santri', 'Calon Santri')]
    , default="calon_santri", readonly="true")

    # def _generate_virtual_account(self):
    #     """Helper method untuk generate Virtual Account"""
    #     return f"{random.randint(10000000, 99999999)}"

    # def create_data_account(self):
    #     """Method untuk auto-generate Virtual Account dan No. VA Uang Saku"""
    #     for partner in self:
    #         # Generate virtual account jika belum diisi
    #         account = partner._generate_virtual_account()
    #         if not partner.virtual_account:
    #             partner.virtual_account = "01" + account

class DataPendaftaran(models.Model):
    _name               = 'ubig.pendaftaran'
    _inherit            = ['mail.thread', 'mail.activity.mixin']
    _inherits           = {"res.partner": "partner_id"}
    _description        = 'Data Pendaftaran'

    nomor_pendaftaran   = fields.Char(string='Nomor Pendaftaran', readonly=True)
    tanggal_daftar      = fields.Date(string='Tanggal Daftar', default=fields.Date.context_today)
    partner_id          = fields.Many2one('res.partner', string="Nama Santri", required=False, help="Nama Calon Santri")

    # Username
    nik                 = fields.Char(string="NIK", help="Nomor Induk Keluarga Calon santri")
    email               = fields.Char(string="email", help="Email Calon Santri")
    password            = fields.Char(string="Kata Sandi", help="Kata Sandi Akun")

    # Jenjang Calon Santri
    jenjang_id          = fields.Many2one('ubig.pendidikan', string="Jenjang Pendidikan")
    jenjang             = fields.Selection(related='jenjang_id.jenjang', string='Jenjang', readonly=True)
    biaya               = fields.Integer(related='jenjang_id.biaya', string='Biaya Pendaftaran', readonly=True)
    keterangan          = fields.Char(related='jenjang_id.keterangan', string='Keterangan', readonly=True)

    # Data Diri
    gender              = fields.Selection([('l','Laki - Laki'),('p','Perempuan'),], string="Jenis Kelamin")
    kota_lahir          = fields.Char(string="Kota Kelahiran")
    tanggal_lahir       = fields.Date(string="Tgl Lahir Calon Santri")
    golongan_darah      = fields.Selection([
                          ('a', 'A'),
                          ('b', 'B'),
                          ('ab', 'AB'),
                          ('o', 'O'),
                        ], string="Golongan Darah")
    kewarganegaraan     = fields.Selection(selection=[('wni','WNI'),('wna','WNA')],  string="Kewarganegaraan",  help="")
    alamat              = fields.Char(string='Alamat Calon Santri')
    provinsi_id         = fields.Many2one(comodel_name="cdn.ref_propinsi",  string="Provinsi",  help="")
    kota_id             = fields.Many2one(comodel_name="cdn.ref_kota",  string="Kota",  help="")
    kecamatan_id        = fields.Many2one(comodel_name="cdn.ref_kecamatan",  string="Kecamatan",  help="")
    nisn                = fields.Char(string="NISN", required=True)
    nis                 = fields.Char(string="NIS", store=True)
    anak_ke             = fields.Integer( string="Anak ke",  help="")
    jml_saudara_kandung = fields.Integer( string="Jml Saudara Kandung",  help="")
    cita_cita           = fields.Char(string='Cita-Cita')

    # Data Pendidikan
    asal_sekolah        = fields.Char(string='Asal Sekolah')
    alamat_asal_sek     = fields.Char(string='Alamat Sekolah Asal')
    telp_asal_sek       = fields.Char(string='No Telp Sekolah Asal')
    status_sekolah_asal = fields.Selection(string='Status Sekolah Asal', selection=[('swasta', 'Swasta'), ('negeri', 'Negeri'),])
    npsn                = fields.Char(string='NPSN Sekolah')

    # Data Orang Tua - Ayah
    nama_ayah           = fields.Char(string="Nama Ayah")
    ktp_ayah            = fields.Char(string="Nomor KTP Ayah")
    tanggal_lahir_ayah  = fields.Date(string="Tanggal Lahir Ayah")
    telepon_ayah        = fields.Char(string="Nomor Telepon Ayah")
    pekerjaan_ayah      = fields.Many2one('cdn.ref_pekerjaan',string="Pekerjaan Ayah")
    penghasilan_ayah    = fields.Selection([
                          ('1juta', ' < Rp. 1.000.000'),
                          ('5juta', 'Rp. 1.000.000 - Rp. 5.000.000'),
                          ('10juta', 'Rp. 6.000.000 - Rp. 10.000.000')
                          ], string="Penghasilan Ayah")
    email_ayah          = fields.Char(string="Email Ayah")
    agama_ayah          = fields.Selection([
                          ('islam', 'Islam'),
                          ('kristen', 'Kristen'),
                          ('katolik', 'Katolik'),
                          ('hindu', 'Hindu'),
                          ('budha', 'Budha'),
                          ('lainnya', 'Lainnya'),
                          ], string="Agama Ayah")
    kewarganegaraan_ayah = fields.Selection(selection=[('wni','WNI'),('wna','WNA')], string="Kewarganegaraan Ayah")
    pendidikan_ayah     = fields.Many2one('cdn.ref_pendidikan', string="Riwayat Pendidikan Ayah")

    # Data Orang Tua - Ibu
    nama_ibu            = fields.Char(string="Nama Ibu")
    ktp_ibu             = fields.Char(string="Nomor KTP Ibu")
    tanggal_lahir_ibu   = fields.Date(string="Tanggal Lahir Ibu")
    telepon_ibu         = fields.Char(string="Nomor Telepon Ibu")
    pekerjaan_ibu       = fields.Many2one('cdn.ref_pekerjaan', string="Pekerjaan Ibu")
    penghasilan_ibu     = fields.Selection([
                          ('1juta', ' < Rp. 1.000.000'),
                          ('5juta', 'Rp. 1.000.000 - Rp. 5.000.000'),
                          ('10juta', 'Rp. 6.000.000 - Rp. 10.000.000')
                          ], string="Penghasilan Ibu")
    email_ibu           = fields.Char(string="Email Ibu")
    agama_ibu           = fields.Selection([
                          ('islam', 'Islam'),
                          ('kristen', 'Kristen'),
                          ('katolik', 'Katolik'),
                          ('hindu', 'Hindu'),
                          ('budha', 'Budha'),
                          ('lainnya', 'Lainnya'),
                          ], string="Agama Ibu")
    kewarganegaraan_ibu = fields.Selection(selection=[('wni','WNI'),('wna','WNA')], string="Kewarganegaraan Ibu")
    pendidikan_ibu      = fields.Many2one('cdn.ref_pendidikan', string="Riwayat Pendidikan Ibu")

    wali_nama           = fields.Char( string="Nama Wali",  help="")
    wali_tmp_lahir      = fields.Char( string="Tmp lahir (Wali)",  help="")
    wali_tgl_lahir      = fields.Date( string="Tgl lahir (Wali)",  help="")
    wali_telp           = fields.Char( string="No Telepon (Wali)",  help="")
    wali_email          = fields.Char( string="Email (Wali)",  help="")
    wali_agama          = fields.Selection(selection=[('islam', 'Islam'), ('katolik', 'Katolik'), ('protestan', 'Protestan'), ('hindu', 'Hindu'), ('budha', 'Budha')],  string="Agama (Wali)",  help="")
    wali_hubungan       = fields.Char( string="Hubungan dengan Siswa",  help="")
                          
    # Dokumen Anak
    akta_kelahiran      = fields.Binary(string="Akta Kelahiran")
    kartu_keluarga      = fields.Binary(string="Kartu Keluarga")
    ijazah              = fields.Binary(string="Ijazah")
    surat_kesehatan     = fields.Binary(string="Surat Keterangan Sehat")
    pas_foto            = fields.Binary(string="Pas Foto Berwarna")
    skhun               = fields.Binary(string="SKHUN")
    raport_terakhir     = fields.Binary(string="Raport Terakhir")

    # Dokumen Orang Tua
    ktp_ortu            = fields.Binary(string="KTP Orang Tua/Wali")

    # Aspek Penilaian
    tajwid              = fields.Integer(string="Tajwid", help="Aturan Bacaan")
    makhraj             = fields.Integer(string="Makhraj", help="Pengucapan Huruf")
    fashahah            = fields.Integer(string="Fashahah", help="Kelancaran Membaca")
    gharib              = fields.Integer(string="Gharib", help="Bacaan-bacaan Khusus")
    irama               = fields.Integer(string="Irama", help="Mujawwad atau Murattal")
    tartil              = fields.Integer(string="Tartil", help="Kecepatan Membaca yang Tepat")

    motivasi            = fields.Integer(string="Motivasi", help="Motivasi Masuk Pesantren")
    pemahaman           = fields.Integer(string="Pemahaman", help="Pemahaman Tentang Kehidupan di Pesantren")
    komitmen            = fields.Integer(string="Komitmen", help="Komitmen dan Kemandirian")
    kedisiplinan        = fields.Integer(string="Kedisiplinan", help="Kedisiplinan dan Sikap")
    pengetahuan         = fields.Integer(string="Pengetahuan", help="Pengetahuan Dasar Agama")
    minat               = fields.Integer(string="Minat & Bakat", help="Minat dan Bakat")

    # Computed field untuk total nilai
    total_nilai         = fields.Integer(string="Total Nilai", compute="_compute_total_nilai", store=True)

    # Virtual Account
    # virtual_account = fields.Char(string='Virtual Account', store=True)
    # bank = fields.Many2one('ubig.bank', string="Bank")
    # petunjuk_pembayaran = fields.Text(related='bank.petunjuk_pembayaran', string="Petunjuk Pembayaran")
    orangtua_id = fields.Many2one('cdn.orangtua', string="Data Orang Tua", readonly=True)
    siswa_id = fields.Many2one('cdn.siswa', string="Data Siswa", readonly=True)

    # State
    state = fields.Selection([
        ('draft', 'Draft'),
        ('terdaftar', 'Terdaftar'),
        ('seleksi', 'Seleksi'),
        ('diterima', 'Diterima'),
        ('ditolak', 'Ditolak'),
        ('batal', 'Batal'),
    ], string='Status', default='draft',
        track_visibility='onchange')
    
    # def _generate_virtual_account(self):
    #     """Helper method to generate a Virtual Account"""
    #     return f"{random.randint(10000000, 99999999)}"

    @api.depends(
        'tajwid', 'makhraj', 'fashahah', 'gharib', 'irama', 'tartil', 
        'motivasi', 'pemahaman', 'komitmen', 'kedisiplinan', 
        'pengetahuan', 'minat', 'total_nilai'
    )
    def _compute_total_nilai(self):
        for record in self:
            record.total_nilai = (
                record.tajwid + record.makhraj + record.fashahah +
                record.gharib + record.irama + record.tartil +
                record.motivasi + record.pemahaman + record.komitmen +
                record.kedisiplinan + record.pengetahuan + record.minat
            )
            # if record.total_nilai >= 75:
            #     record.state = 'diterima'
            # elif record.total_nilai != 0 and record.total_nilai < 75:
            #     record.state = 'ditolak'

    # def _generate_nis(self, nisn):
    #     for record in self:
    #         nisn = nisn
    #         if nisn and len(nisn) >= 5:
    #             last_nisn = nisn[-5:]
    #             npsn = record.jenjang_id.npsn
    #             last_npsn = npsn[-3:]
    #             thn_sekarang = str(datetime.now().year)
    #             last_thn_sekarang = thn_sekarang[-2:]
    #             nis = f"{last_nisn}{last_npsn}{last_thn_sekarang}"
    #         else:
    #             last_nisn = ''
    #     return nis


    # Constraint untuk validasi nilai antara 1 hingga 10
    @api.onchange(
        'tajwid', 'makhraj', 'fashahah', 'gharib', 'irama', 'tartil', 
        'motivasi', 'pemahaman', 'komitmen', 'kedisiplinan', 
        'pengetahuan', 'minat'
    )
    def _onchange_nilai(self):
        for record in self:
            fields_to_check = [
                'tajwid', 'makhraj', 'fashahah', 'gharib', 'irama', 
                'tartil', 'motivasi', 'pemahaman', 'komitmen', 
                'kedisiplinan', 'pengetahuan', 'minat'
            ]
            
            # Check each field for valid range (1-10)
            for field in fields_to_check:
                value = getattr(record, field)
                if value and (value < 1 or value > 10):
                    # Set the value to 0 to reset invalid input
                    setattr(record, field, 0)
                    return {
                        'warning': {
                            'title': 'Nilai Tidak Valid',
                            'message': f'Nilai untuk {field} harus berada antara 1 - 10. Nilai telah direset ke 0.',
                        }
                    }

    @api.model
    def create(self, vals):
        # Get the current year
        current_year = fields.Date.context_today(self).year
        
        # Search for existing records with the same year
        existing_records = self.search([('nomor_pendaftaran', 'ilike', f'PSB/{current_year}/%')])
        
        # Determine the next sequence number
        if existing_records:
            last_number = max(int(record.nomor_pendaftaran.split('/')[-1]) for record in existing_records)
            next_number = last_number + 1
        else:
            next_number = 1
            
        # Generate the new nomor_pendaftaran
        vals['nomor_pendaftaran'] = f'PSB/{current_year}/{str(next_number).zfill(5)}'

        return super(DataPendaftaran, self).create(vals)


    def action_terdaftar(self):
        self.state = 'terdaftar'

    def action_seleksi(self):
        self.state = 'seleksi'

    def action_diterima(self):
        self.state = 'diterima'

    def action_ditolak(self):
        self.state = 'ditolak'

    def action_batal(self):
        self.state = 'batal'

    def action_draft(self):
        # Optional: You can define additional actions for when "Draft" is clicked
        self.write({'state': 'draft'})


    def action_report_pendaftaran(self):
        # Logika untuk meng-generate laporan PDF atau aksi lainnya
        return self.env.ref('pesantren_pendaftaran.action_report_pendaftaran').report_action(self)

    # @api.model
    # def default_get(self, fields):
    # res = super(DataPendaftaran, self).default_get(fields)  # Use the exact class name here
    # res['jns_partner'] = 'calon_santri'
    # return res

    def write(self, vals):
        # if 'bank' in vals:
        #     nisn = self.nisn
        #     vals['virtual_account'] = self._generate_virtual_account(vals, nisn)

        if 'state' in vals and vals['state'] == 'diterima':
            for record in self:
                # Buat akun orang tua jika belum ada
                if not record.orangtua_id:
                    orangtua = record.create_orangtua()
                    record.orangtua_id = orangtua.id

                # Buat data siswa jika belum ada
                if not record.siswa_id:
                    siswa = record.create_siswa()
                    record.siswa_id = siswa.id

                # Buat data virtual account
                if not record.virtual_account:
                    nisn = record.nisn
                    record.virtual_account = record._generate_virtual_account(nisn)

                # Buat data virtual account uang saku
                if not record.va_saku:
                    nisn = record.nisn
                    record.va_saku = record._generate_va_uangsaku(nisn)

                # Generate nis
                if not record.nis:
                    nisn = record.nisn
                    record.nis = record._generate_nis(nisn)

        # Check if state is being changed to 'terdaftar'
        # if 'state' in vals and vals['state'] == 'diterima':
        #     for record in self:
        #         if not record.virtual_account:
        #             record.virtual_account = "01" + record._generate_virtual_account()

        return super(DataPendaftaran, self).write(vals)
    
    def create_orangtua(self):
        for record in self:
            """Fungsi untuk membuat akun orang tua di cdn.orangtua"""

            # Cek apakah email orang tua sudah ada di res.partner
            existing_partner = self.env['res.partner'].search([('email', '=', record.email)], limit=1)

            if existing_partner:
                # Jika partner sudah ada, cek apakah data orang tua sudah ada
                existing_orangtua = self.env['cdn.orangtua'].sudo().search([('partner_id', '=', existing_partner.id)], limit=1)
                if existing_orangtua:
                    # Jika data orang tua sudah ada, gunakan data tersebut
                    return existing_orangtua
                else:
                     # Jika partner ada tapi data orang tua belum ada, buat data orang tua
                     orangtua_vals = {
                         'partner_id': existing_partner.id,
                         'hubungan': 'ayah',
                         'email': record.email,
                         'nik': record.ktp_ayah,
                     }
                     orangtua = self.env['cdn.orangtua'].sudo().create(orangtua_vals)
                     return orangtua
            else:
                # Jika partner belum ada, buat data partner baru
                # Membuat data orangtua otomatis saat pendaftaran diterima
                partner_vals = {
                    'name': record.nama_ayah,
                    'email': record.email,  # Asumsi field email ada di model Pendaftaran
                    'phone': record.telepon_ayah,  # Asumsi field phone ada di model Pendaftaran
                    'street': record.alamat,  # Asumsi field Alamat ada di model Pendaftaran
                    'city': record.kota_id.name,
                }
                
                # Membuat data partner untuk orang tua
                partner = self.env['res.partner'].create(partner_vals)

                orangtua_vals = {
                    'partner_id': partner.id,
                    'hubungan': 'ayah',
                    'email': record.email,
                    'nik': record.ktp_ayah,
                }
                orangtua = self.env['cdn.orangtua'].sudo().create(orangtua_vals)

                # Mengatur password untuk user_id yang sudah dibuat otomatis
                if partner.user_id:  # Pastikan user_id sudah ada
                    password = record.password
                    partner.user_id.write({'password': password,})

                # Mengirim email menggunakan mail.mail
                email_values = {
                    'subject': "Informasi Login Orang Tua Santri Baru Pesantren Daarul Qur'an Istiqomah",
                    'email_to': record.email,
                    'body_html': f'''
                        <p>Assalamualaikum Wr.wb, Bapak/Ibu {record.nama_ayah}</p>
                        <p>Akun OrangTua telah dibuat di sistem pesantren kami. Dengan ini kami kirimkan informasi akun login sebagai berikut:</p>
                        <ul>
                            <li>Web Login   : Gunakan <a href="https://clever-gelding-alive.ngrok-free.app/odoo">Akun Anda</a></li>
                            <li>Email       : {record.email}</li>
                            <li>Password    : {password}</li>
                        </ul>
                        <p>Apabila terdapat kesulitan saat login atau membutuhkan bantuan, Bapak/Ibu dapat menghubungi tim teknis kami melalui nomor telepon 0822 5207 9785/0853 9051 1124. <br> <br>
                        Kami harap portal ini dapat memudahkan Bapak/Ibu dalam memantau perkembangan putra/putri selama berada di pesantren. <br> <br>
                        Demikian informasi ini kami sampaikan. Atas perhatian dan kerjasamanya, kami ucapkan terima kasih.<br> <br> <br>

                        Hormat kami, <br>
                        Admin Pendaftaran <br>
                        Pesantren Tahfizh Daarul Qur'an Istiqomah</p>
                    ''',
                }

                # Membuat dan mengirim email
                mail = self.env['mail.mail'].sudo().create(email_values)
                mail.send()

                return orangtua

    def create_siswa(self):
        for record in self:
            """Fungsi untuk membuat data siswa dari pendaftaran"""
            siswa_vals = {
                'name': record.partner_id.name,
                'propinsi_id': record.provinsi_id.id,
                'kota_id': record.kota_id.id,
                'kecamatan_id': record.kecamatan_id.id,
                'street': record.alamat,
                'nisn': record.nisn,
                'nis': record.nis,
                'nik': record.nik,
                'jenjang': record.jenjang,
                'kewarganegaraan': record.kewarganegaraan,
                'orangtua_id': record.orangtua_id.id,
                'tgl_lahir': record.tanggal_lahir,
                'jns_kelamin': record.gender,
                'tmp_lahir': record.kota_lahir,
                'gol_darah': record.golongan_darah,
                'anak_ke': record.anak_ke,
                'asal_sekolah': record.asal_sekolah,
                'status_sekolah_asal': record.status_sekolah_asal,
                'telp_asal_sek': record.telp_asal_sek,
                'alamat_asal_sek': record.alamat_asal_sek,
                'virtual_account': record.virtual_account,
                'va_saku': record.va_saku,

                # Orang Tua
                'ayah_nama': record.nama_ayah,
                'ayah_tgl_lahir': record.tanggal_lahir_ayah,
                'ayah_telp': record.telepon_ayah,
                'ayah_pekerjaan_id': record.pekerjaan_ayah.id,
                'ayah_agama': record.agama_ayah,
                'ayah_warganegara': record.kewarganegaraan_ayah,
                'ayah_email': record.email_ayah,
                'ayah_pendidikan_id': record.pendidikan_ayah.id,

                'ibu_nama': record.nama_ibu,
                'ibu_tgl_lahir': record.tanggal_lahir_ibu,
                'ibu_telp': record.telepon_ibu,
                'ibu_pekerjaan_id': record.pekerjaan_ibu.id,
                'ibu_agama': record.agama_ibu,
                'ibu_warganegara': record.kewarganegaraan_ibu,
                'ibu_email': record.email_ibu,
                'ibu_pendidikan_id': record.pendidikan_ibu.id,
            }
            siswa = self.env['cdn.siswa'].sudo().create(siswa_vals)
            return siswa
    

    # def generate_password_akun_ortu(ktp, additional_arg=None):
    #     ktp_str = str(ktp)
    #     # Buat hash dari nomor KTP menggunakan SHA-256
    #     hash_object = hashlib.sha256(ktp_str.encode())
    #     hashed_ktp = hash_object.hexdigest()

    #     # Ambil 8 karakter pertama dari hasil hash
    #     password = hashed_ktp[:8]
    #     return password
    
    # def _generate_virtual_account(self, vals, nis):
    #     # if not self.bank or not self.bank.kode_bank:
    #     #     raise ValueError("Kode bank tidak ditemukan. Pastikan Anda memilih bank dengan kode yang valid.")
        
    #     bank = self.env['ubig.bank'].browse(vals.get('bank'))

    #     kode_va_bank = bank.kode_va_bank if bank else ''
    #     account_type = "01"

    #     nis = nis

    #     return f"{kode_va_bank}{account_type}{nis}"


    def _generate_virtual_account(self, nis):
        for record in self:
            kode_va_bank = "88810"
            account_type = "01"
            nis = nis

            return f"{kode_va_bank}{account_type}{nis}"
        
    def _generate_va_uangsaku(self, nis):
        for record in self:
            kode_va_bank = "88810"
            account_type = "02"
            nis = nis

            return f"{kode_va_bank}{account_type}{nis}"
        