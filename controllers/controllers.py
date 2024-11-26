# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http
from odoo.http import request
import random
from datetime import date
import datetime
from odoo.exceptions import UserError
import hashlib


class PesantrenBeranda(http.Controller):
    @http.route('/beranda', auth='public')
    def index(self, **kw):
        return """
                    <!doctype html>
                    <html lang="en">

                    <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Daarul Qur'an Istiqomah</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
                        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
                    </head>
                    <style>
                    .bg-body-grenyellow {
                        background: linear-gradient(to right, #009688 40%, #ccff33 130%);
                    }

                    .rounded-90 {
                        border-radius: 0 0 25% 0;
                    }

                    .p-auto {
                        padding: 6% 0;
                    }

                    .stepper {
                        display: flex;
                        justify-content: space-around;
                        align-items: center;
                        margin-top: 50px;
                    }

                    .step {
                        text-align: center;
                        position: relative;
                        padding-top: 30px;
                    }

                    .step-circle {
                        width: 50px;
                        height: 50px;
                        background-color: #009688;
                        color: white;
                        font-size: 1.5rem;
                        border-radius: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin: 0 auto;
                        position: relative;
                        z-index: 1;
                    }

                    .step-line {
                        width: 100%;
                        height: 2px;
                        background-color: #009688;
                        position: absolute;
                        top: 55px;
                        left: 0;
                        z-index: -10;
                    }

                    .mt-3 {
                        height: 48px;
                    }

                    .step:last-child .step-line {
                        width: 50%;
                    }

                    .step:first-child .step-line {
                        width: 50%;
                        left: 50%;
                    }

                    .text-green {
                        color: #009688;
                    }
                    .footer {
                    background-color: #4a4a4a;
                    }
                    .footer h5 {
                    font-weight: bold;
                    }
                    .footer p, .footer a {
                    color: #ffffff;
                    font-size: 0.9rem;
                    }
                    .footer a:hover {
                    text-decoration: underline;
                    }
                    .footer hr {
                    border-color: #ffffff;
                    opacity: 0.3;
                    }

                    </style>

                    <body>
                    <!-- Navbar -->
                    <nav class="navbar navbar-expand-lg bg-body-grenyellow shadow sticky-top">
                        <div class="container">
                        <a class="navbar-brand" href="#">
                            <img src="https://i.ibb.co.com/68BTxC9/dqi-2.png" alt="Icon Daarul Qur’an Istiqomah" width="40" height="40">
                            Daarul Qur’an Istiqomah</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse d-flex justify-content-end " id="navbarSupportedContent">
                            <div class="">
                            <a href="/psb" class="btn btn-light" type="submit">Pendaftaran</a>
                            <a href="/web/login" class="btn btn-warning" type="submit">Login</a>
                            </div>
                        </div>
                        </div>
                    </nav>
                    <!-- Navbar end -->

                    <!-- banner -->
                    <div class="bg-body-grenyellow rounded-90">
                        <div class="container p-auto d-flex text-light justify-content-center align-items-center">
                        <div class="me-5">
                            <img src="https://i.ibb.co.com/f9j819p/1731466812700.png" alt="" width="400">
                        </div>
                        <div class="ms-3">
                            <h1 class="fw-bold">Pendaftaran Santri Baru</h1>
                            <h3 class="fw-bold pb-3">Pondok Pesantren Daarul Qur’an Istiqomah</h3>
                            <h5 class="fw-bold">Daarul Qur’an Istiqomah Boarding School for Education and Science</h5>
                            <h5 class="fw-bold">Tahun Ajaran 2024 - 2025</h5>
                            <button class="btn btn-light rounded-5 text-primary">Daftar Sekarang</button>
                        </div>
                        </div>
                    </div>
                    <!-- banner end -->

                    <!-- Step Pendaftaran -->
                    <div class="container text-center my-3">
                        <h1 class="fw-bold"><span class="text-green">Alur</span> Pendaftaran Online</h1>
                        <div class="container">
                        <div class="stepper">
                            <div class="step">
                            <div class="step-circle">1</div>
                            <div class="step-line"></div>
                            <h5 class="mt-3">Pembuatan Akun</h5>
                            <p class="text-muted">Mengisi identitas calon peserta didik sekaligus pembuatan akun untuk mendapatkan Nomor
                                Registrasi.</p>
                            </div>
                            <div class="step">
                            <div class="step-circle">2</div>
                            <div class="step-line"></div>
                            <h5 class="mt-3">Login & Melengkapi Data</h5>
                            <p class="text-muted">Melengkapi data peserta didik, data orang tua / wali atau mahram khususnya santri putri.
                            </p>
                            </div>
                            <div class="step">
                            <div class="step-circle">3</div>
                            <div class="step-line"></div>
                            <h5 class="mt-3">Mengunggah Berkas</h5>
                            <p class="text-muted">Mengunggah berkas persyaratan dan berkas pendukung lainnya yang berupa gambar / foto.
                            </p>
                            </div>
                            <div class="step">
                            <div class="step-circle">4</div>
                            <div class="step-line"></div>
                            <h5 class="mt-3">Pembayaran</h5>
                            <p class="text-muted">Melakukan pembayaran biaya pendaftaran sesuai pendidikan yang telah dipilih.</p>
                            </div>
                            <div class="step">
                            <div class="step-circle">5</div>
                            <div class="step-line"></div>
                            <h5 class="mt-3">Cetak Pendaftaran</h5>
                            <p class="text-muted">Cetak atau simpan Nomor Registrasi sebagai bukti pendaftaran untuk ditunjukkan ke
                                petugas PSB.</p>
                            </div>
                        </div>
                        </div>
                    </div>
                    <!-- End step pendaftaran -->


                    <!-- Syarat Pendaftaran -->
                    <div class="container my-5">
                        <div class="row align-items-center">
                        <!-- Text Section -->
                        <div class="col-md-6">
                            <h2 class="fw-bold"><span class="text-green ">Syarat</span> Pendaftaran</h2>
                            <p>Untuk memenuhi persyaratan pendaftaran santri baru, perlu beberapa berkas yang harus disiapkan:</p>
                            <ul class="list-unstyled d-grid gap-2">
                            <li class="d-flex"><i class="bi bi-check-circle-fill me-2 text-warning"></i>
                                <div class="d-flex flex-column"><strong>Photo Copy Akta Kelahiran Peserta Didik</strong> </div>
                            </li>
                            <li class="d-flex"><i class="bi bi-check-circle-fill me-2 text-warning"></i>
                                <div class="d-flex flex-column"><strong>Photo Copy KTP orang tua/wali</strong> <span>sebanyak 3
                                    lembar</span></div>
                            </li>
                            <li class="d-flex"><i class="bi bi-check-circle-fill me-2 text-warning"></i>
                                <div class="d-flex flex-column"><strong>Photo Copy Kartu Keluarga (KK)</strong> <span>sebanyak 3
                                    lembar</span></div>
                            </li>
                            <li class="d-flex"><i class="bi bi-check-circle-fill me-2 text-warning"></i>
                                <div class="d-flex flex-column"><strong>Photo Copy STL/SKHUN/Ijazah</strong> <span>sebanyak 3 lembar</span>
                                </div>
                            </li>
                            <li class="d-flex"><i class="bi bi-check-circle-fill me-2 text-warning"></i>
                                <div class="d-flex flex-column"><strong>Surat Keterangan Sehat dari Fasilitas Kesehatan</strong> </div>
                            </li>
                            </ul>
                        </div>
                        <!-- Image Section -->
                        <div class="col-md-6">
                            <img src="https://psb.nuruljadid.net/img/PAGE2.44b0e259.png" class="img-fluid rounded-4"
                            alt="Syarat Pendaftaran">
                        </div>
                        </div>
                    </div>
                    <!-- Syarat Pendaftaran End -->

                    <!-- Alur Penyerahan Santri -->
                    <div class="container mt-5">
                        <h1 class="fw-bold">Alur <span class="text-green">Penyerahan Santri</span></h1>
                        <div class="row justify-content-center">
                        <!-- Card 1 -->
                        <div class="col-md-4 text-center my-2">
                            <div class="card p-4 shadow border-0">
                            <div class="circle-icon mb-3">
                                <i class="bi bi-plus-circle-fill h1 text-green"></i>
                            </div>
                            <h2 class="step-number">1</h2>
                            <h5 class="font-weight-bold mt-3">Checkup / Periksa Kesehatan</h5>
                            <p>Pemeriksaan kesehatan dari calon peserta didik oleh petugas klinik Az-Zainiyah.</p>
                            <div class="bottom-icon mt-4">
                                <i class="bi bi-shirt text-info"></i>
                            </div>
                            </div>
                        </div>
                        <!-- Card 2 -->
                        <div class="col-md-4 text-center my-2">
                            <div class="card p-4 shadow border-0">
                            <div class="circle-icon mb-3">
                                <i class="bi bi-file-earmark-text-fill h1 text-green"></i>
                            </div>
                            <h2 class="step-number">2</h2>
                            <h5 class="font-weight-bold mt-3">Konfirmasi Nomor Registrasi</h5>
                            <p>Menyerahkan Nomor Registrasi dan bukti pendaftaran online kepada petugas PSB.</p>
                            <div class="bottom-icon mt-4">
                                <i class="bi bi-handshake text-success"></i>
                            </div>
                            </div>
                        </div>
                        <!-- Card 3 -->
                        <div class="col-md-4 text-center my-2">
                            <div class="card p-4 shadow border-0">
                            <div class="circle-icon mb-3">
                                <i class="bi bi-person-check-fill h1 text-green"></i>
                            </div>
                            <h2 class="step-number">3</h2>
                            <h5 class="font-weight-bold mt-3">Ikrar Santri</h5>
                            <p>Melakukan Ikrar Santri dan kesediaan mengikuti aturan yang ditetapkan oleh Pondok Pesantren Nurul Jadid.
                            </p>
                            </div>
                        </div>
                        <!-- Card 4 -->
                        <div class="col-md-4 text-center my-2">
                            <div class="card p-4 shadow border-0">
                            <div class="circle-icon mb-3">
                                <i class="bi bi-box-seam-fill h1 text-green"></i>
                            </div>
                            <h2 class="step-number">4</h2>
                            <h5 class="font-weight-bold mt-3">Pengambilan Seragam</h5>
                            <p>Pengambilan seragam sesuai dengan pemilihan ukuran seragam yang telah dipilih oleh pendaftar. </p>
                            <div class="bottom-icon mt-4">
                                <i class="bi bi-shirt text-info"></i>
                            </div>
                            </div>
                        </div>
                        <!-- Card 5 -->
                        <div class="col-md-4 text-center my-2">
                            <div class="card p-4 shadow border-0">
                            <div class="circle-icon mb-3">
                                <i class="bi bi-people h1 text-green"></i>
                            </div>
                            <h2 class="step-number">5</h2>
                            <h5 class="font-weight-bold mt-3">Sowan Pengasuh</h5>
                            <p>Penyerahan calon peserta didik oleh orangtua / wali kepada pengasuh </p>
                            <div class="bottom-icon mt-4">
                                <i class="bi bi-handshake text-success"></i>
                            </div>
                            </div>
                        </div>
                        <!-- Card 6 -->
                        <div class="col-md-4 text-center my-2">
                            <div class="card p-4 shadow border-0">
                            <div class="circle-icon mb-3">
                                <i class="bi bi-buildings h1 text-green"></i>
                            </div>
                            <h2 class="step-number">6</h2>
                            <h5 class="font-weight-bold mt-3">Asrama Santri</h5>
                            <p>Santri baru menempati asrama yang telah ditetepkan oleh pengurus. </p>
                            </div>
                        </div>
                        </div>
                    </div>
                    <!-- Alur Penyerahan Santri end-->

                    <!-- Informasi Pelayanan Pendaftaran -->
                    <div class="container my-5">
                        <div class="row align-items-center">
                        <div class="col-md-6">
                            <img src="https://psb.nuruljadid.net/img/PAGE3.e3b6d704.png" alt="Image" class="rounded-custom img-fluid" />
                        </div>
                        <div class="col-md-6">
                            <h3 class="fw-bold"><span class="text-primary ">Informasi</span> Pelayanan Pendaftaran</h3>
                            <div class="accordion" id="accordionExample">
                            <div class="accordion-item mb-3">
                                <h2 class="accordion-header" id="headingOne">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne"
                                    aria-expanded="true" aria-controls="collapseOne">
                                    Pembukaan Pendaftaran & Kantor Layanan:
                                </button>
                                </h2>
                                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <p class="m-0">Tanggal:</p>
                                    <p class="fw-bold">1 Maret s.d. 8 Juli 2024</p>
                                    <p class="m-0">Layanan Putra:</p>
                                    <p class="fw-bold">Kantor Sekretariat Putra</p>
                                    <p class="m-0">Layanan Putri:</p>
                                    <p class="fw-bold">Kantor Sekretariat Putri</p>
                                </div>
                                </div>
                            </div>
                            <div class="accordion-item mb-3">
                                <h2 class="accordion-header" id="headingTwo">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                                    Penerimaan Satu Atap & Verifikasi Berkas:
                                </button>
                                </h2>
                                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <!-- Konten untuk Verifikasi Berkas -->
                                    <p class="m-0">Tanggal:</p>
                                    <p class="fw-bold">3 s.d 8 Juli 2024</p>
                                    <p class="m-0">Tempat Penerimaan:</p>
                                    <p class="fw-bold">Aula II Pesantren, Lantai 3</p>
                                </div>
                                </div>
                            </div>
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="headingThree">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                    data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                                    Waktu Pelayanan:
                                </button>
                                </h2>
                                <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree"
                                data-bs-parent="#accordionExample">
                                <div class="accordion-body">
                                    <!-- Konten untuk Waktu Pelayanan -->
                                    <p class="m-0">Pagi:</p>
                                    <p class="fw-bold">08.00 ~ 12.00 WIB</p>
                                    <p class="m-0">Siang:</p>
                                    <p class="fw-bold">13.00 ~ 16.00 WIB</p>
                                </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    <!-- Informasi Pelayanan Pendaftaran end-->

                    <!-- Footer -->
                    <footer class="footer py-4">
                        <div class="container">
                        <div class="row text-white">
                            <div class="col-md-4">
                            <h5>Pondok Pesantren Daarul Qur’an Istiqomah</h5>
                            <p>
                                Jl. Ambawang, RT.03/RW.01, Karang Taruna, Kec. Pelaihari, Kabupaten Tanah Laut, Kalimantan Selatan 70815 <br>
                                Telp. (0888-307-7077)
                            </p>
                            </div>
                            <div class="col-md-4">
                            <h5>Social Pages</h5>
                            <ul class="list-unstyled">
                                <li><a href="#" class="text-white"><i class="bi bi-facebook"></i> Facebook</a></li>
                                <li><a href="#" class="text-white"><i class="bi bi-twitter"></i> Twitter</a></li>
                                <li><a href="#" class="text-white"><i class="bi bi-instagram"></i> Instagram</a></li>
                                <li><a href="#" class="text-white"><i class="bi bi-youtube"></i> Youtube</a></li>
                            </ul>
                            </div>
                            <div class="col-md-4">
                            <h5><i class="bi bi-telephone"></i> Pusat Layanan Informasi</h5>
                            <p>
                                0813-3622-2034 (Sekretariat Putra)<br>
                                0821-4639-3907 (Sekretariat Putri)<br>
                                0852-5880-0137 (Keuangan)<br>
                                0822-4633-5137 (Layanan Umum)
                            </p>
                            </div>
                        </div>
                        <div class="text-center text-white mt-4">
                            <hr class="border-white">
                            <p>©Copyright 2024 - Daarul Qur’an Istiqomah</p>
                        </div>
                        </div>
                    </footer>
                    
                    <!-- Footer end -->
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
                        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
                        crossorigin="anonymous"></script>
                    </body>

                    </html>
        """

class PesantrenPendaftaran(http.Controller):
    @http.route('/psb', auth='public')
    def index(self, **kw):
        return """
            <!DOCTYPE html>
<html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>PSB - Daarul Qur'an Istiqomah</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
                <style>

                    body {
                        background: linear-gradient(to bottom left, #065c5c 18%, #f5e505 100%) !important;
                    }

                    .offcanvas.offcanvas-end {
                        
                        width: 250px; /* Lebar kustom untuk offcanvas */
                    }
                    
                    .offcanvas .nav-link {
                        color: #ffffff; /* teks warna putih */
                    }
                    
                    .offcanvas .btn-close {
                        position: absolute;
                        top: 10px;
                        right: 10px;
                        filter: invert(1);
                    }

                    .judul {
                        height: 81px;
                        display: flex;
                        align-items: end;
                    }

                    .teks-judul {
                        height: 72px;
                    }

                    .background {
					    background: linear-gradient(to bottom left, #065c5c 18%, #f5e505 100%) !important;
					}

					a.effect {
						transition: .1s !important;
					}

					a.effect:hover {
						box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
					}

                    /* Desain Dropdown */
                    .dropdown {
                        position: relative;
                    }

                    .dropdown-link {
                        cursor: pointer;
                    }

                    .dropdown-content {
                        display: none;
                        position: absolute;
                        top: 100%;
                        right: 0;
                        background-color: #ffffff;
                        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                        border-radius: 5px;
                        min-width: 150px;
                        z-index: 1;
                        overflow: hidden;
                    }

                    .dropdown-content a {
                        color: #333;
                        padding: 10px 15px;
                        display: block;
                        text-decoration: none;
                        transition: background-color 0.2s;
                    }

                    .dropdown-content a:hover {
                        background-color: #f1f1f1;
                    }

                    /* Menampilkan dropdown saat hover */
                    .dropdown:hover .dropdown-content {
                        display: block;
                        animation: fadeIn 0.3s;
                    }

                    /* Animasi fade-in */
                    @keyframes fadeIn {
                        from {
                        opacity: 0;
                        transform: translateY(-10px);
                        }
                        to {
                        opacity: 1;
                        transform: translateY(0);
                        }
                    }

                </style>
            </head>
            <body>

            <nav class="navbar navbar-expand-lg" style="height: 65px;">
                <div class="container-fluid">
                    <a class="navbar-brand ms-5 text-white fw-semibold" href="/psb">
                    	<img src="https://i.ibb.co.com/f9j819p/1731466812700.png" alt="1731466812700" width="50" alt="Logo Pesantren">       Daarul Qur'an Istiqomah
                	</a>
                    <button class="navbar-toggler ms-auto" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item me-3">
                                <a class="nav-link text-white" href="/psb"><i class="fa-solid fa-house me-2"></i>Beranda</a>
                            </li>
                            <li class="nav-item me-3">
                                <a class="nav-link text-white" href="/pendaftaran"><i class="fa-solid fa-note-sticky me-2"></i>Pendaftaran</a>
                            </li>
                            <li class="nav-item me-3">
                                <a class="nav-link text-white" href="/web/login"><i class="fa-solid fa-fingerprint me-2"></i>Login</a>
                            </li>
                            <li class="nav-item me-3">
                                <a class="nav-link text-white" href="/bantuan"><i class="fa-solid fa-lock me-2"></i>Bantuan</a>
                            </li>
                            <li class="nav-item dropdown">
                                <a href="#" class="dropdown-link nav-link text-white"><i class="fa-solid fa-bullhorn me-2"></i>Pengumuman</a>
                                <div class="dropdown-content">
                                    <a href="/pengumuman/sd-mi">SD / MI</a>
                                    <a href="/pengumuman/smp-mts">SMP / MTS</a>
                                    <a href="/pengumuman/sma-ma">SMA / MA</a>
                                </div>
                            </li>

                        </ul>
                    </div>
                </div>
            </nav>

            <div class="offcanvas offcanvas-end background" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                <a class="navbar-brand mt-1 text-white fw-semibold" href="/psb" style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://i.ibb.co.com/f9j819p/1731466812700.png" alt="1731466812700" width="50" alt="Logo Pesantren">
                    Daarul Qur'an Istiqomah
                </a>
                <div class="offcanvas-body">
                    <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                        <li class="nav-item me-3">
                            <a class="nav-link text-white" href="/psb"><i class="fa-solid fa-house me-2"></i>Beranda</a>
                        </li>
                        <li class="nav-item me-3">
                            <a class="nav-link text-white" href="/pendaftaran"><i class="fa-solid fa-note-sticky me-2"></i>Pendaftaran</a>
                        </li>
                        <li class="nav-item me-3">
                            <a class="nav-link text-white" href="/web/login"><i class="fa-solid fa-fingerprint me-2"></i>Login</a>
                        </li>
                        <li class="nav-item me-3">
                            <a class="nav-link text-white" href="/bantuan"><i class="fa-solid fa-lock me-2"></i>Bantuan</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a href="#" class="dropdown-link nav-link text-white"><i class="fa-solid fa-bullhorn me-2"></i>Pengumuman</a>
                            <div class="dropdown-content">
                                <a href="/pengumuman/sd-mi">SD / MI</a>
                                <a href="/pengumuman/smp-mts">SMP / MTS</a>
                                <a href="/pengumuman/sma-ma">SMA / MA</a>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <div style="display: flex; justify-content: center;" class="mt-5">
                <div class="text-center text-white">
                    <h4 class="fs-2 fw-semibold mb-4">Aplikasi penerimaan santri baru</h4>
                    <span>Daarul Qur'an Istiqomah Tanah Laut Kalimantan Selatan</span>
                    <a href="/pendaftaran" class="btn btn-dark">Daftar Sekarang</a>
                </div>
            </div>

            <div class="container mt-5 mb-5">
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;">
                    <div class="bg-white shadow-lg rounded p-3" style="width: 270px; display: flex; flex-direction: column; align-items: center; justify-content: space-between;">
                        <span class="text-uppercase text-secondary mb-3">Program Pendidikan</span>
                        <div>
                            <i class="fa-solid fa-graduation-cap fs-1 border rounded-circle p-5" style="color: #e91e63 !important;"></i>
                        </div>
                        <span class="text-uppercase fs-3 judul">Prodi</span>
                        <div class="text-center mb-4 teks-judul">
                            <span class="text-secondary" style="font-size: 14px;">1. TK TAHFIZH</span>
                            <span class="text-secondary" style="font-size: 14px;">2. SD BILINGUAL</span>
                            <span class="text-secondary" style="font-size: 14px;">3. SMP / MTS</span>
                            <span class="text-secondary" style="font-size: 14px;">4. SMA / MA</span>
                        </div>
                        <div class="text-uppercase">
                            <a href="" data-bs-toggle="modal" data-bs-target="#detailProgramPendidikan" class="effect" style="background-color: #9F1FB2 !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;">Detail</a>
                            <a href="/pendaftaran" class="effect" style="background-color: #009CFF !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;" target="_blank">Daftar</a>
                        </div>
                    </div>
                    <div class="bg-white shadow-lg rounded p-3" style="width: 270px; display: flex; flex-direction: column; align-items: center; justify-content: space-between;">
                        <span class="text-uppercase text-secondary mb-3">Jadwal Kegiatan</span>
                        <div>
                            <i class="fa-regular fa-calendar fs-1 border rounded-circle p-5" style="color: #e91e63 !important;"></i>
                        </div>
                        <span class="text-uppercase fs-3 judul">Jadwal Kegiatan</span>
                        <div class="text-center mb-4 teks-judul">
                            <span class="text-secondary" style="font-size: 14px;">Jadwal kegiatan PSB dan Kuota Test </span>
                        </div>
                        <div class="text-uppercase">
                            <a href="" data-bs-toggle="modal" data-bs-target="#detailJadwalKegiatan" class="effect" style="background-color: #9F1FB2 !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;">Detail</a>
                            <a href="/pendaftaran" class="effect" style="background-color: #009CFF !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;" target="_blank">Daftar</a>
                        </div>
                    </div>
                    <div class="bg-white shadow-lg rounded p-3" style="width: 270px; display: flex; flex-direction: column; align-items: center; justify-content: space-between;">
                        <span class="text-uppercase text-secondary mb-3">Persyaratan</span>
                        <div>
                            <i class="fa-solid fa-clipboard-list fs-1 border rounded-circle p-5" style="color: #e91e63 !important;"></i>
                        </div>
                        <span class="text-uppercase fs-3 text-center judul">Syarat pendaftaran</span>
                        <div class="text-center mb-4 teks-judul">
                            <span class="text-secondary" style="font-size: 14px;">Persyaratan Pendaftaran dapat dilihat disini</span>
                        </div>
                        <div class="text-uppercase">
                            <a href="" data-bs-toggle="modal" data-bs-target="#detailPersyaratan" class="effect" style="background-color: #9F1FB2 !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;">Detail</a>
                            <a href="/pendaftaran" class="effect" style="background-color: #009CFF !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;" target="_blank">Daftar</a>
                        </div>
                    </div>
                    <div class="bg-white shadow-lg rounded p-3" style="width: 270px; display: flex; flex-direction: column; align-items: center; justify-content: space-between;">
                        <span class="text-uppercase text-secondary mb-3">Bantuan</span>
                        <div>
                            <i class="fa-solid fa-graduation-cap fs-1 border rounded-circle p-5" style="color: #e91e63 !important;"></i>
                        </div>
                        <span class="text-uppercase fs-3 judul">Hubungi Kami</span>
                        <div class="text-center mb-4 teks-judul">
                            <span class="text-secondary" style="font-size: 14px;">Jika memerlukan bantuan : Telp / WA : 62271-858199 </span>
                        </div>
                        <div class="text-uppercase">
                            <a href="/bantuan" class="effect" style="background-color: #9F1FB2 !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;">Detail</a>
                            <a href="/pendaftaran" class="effect" style="background-color: #009CFF !important; padding: 10px 20px; border-radius: 20px; text-decoration: none; color: white;" target="_blank">Daftar</a>
                        </div>
                    </div>
                </div>
                
            </div>

            <footer class="text-white p-2" style="display: flex; justify-content: space-between; flex-wrap: wrap;">
            	<div class="ms-5">
            		<ul style="list-style-type: none; display: flex; text-transform: uppercase; font-size: 13px;" class="fw-semibold">
            			<li><a href="/psb" class="me-4" style="text-decoration: none; color: white;">Home</a></li>
            			<li><a href="/beranda" class="me-4" style="text-decoration: none; color: white;" target="_blank">Info Pondok</a></li>
            			<li><a href="https://drive.google.com/drive/mobile/folders/1EYat5411joyoOmH_DkJ3g2DeJKgyyuBQ?usp=share_link&fbclid=IwY2xjawGflGlleHRuA2FlbQIxMQABHTusVv9hD3VRDSLW9-671QhOL86e3KMv30smsAYW0DHkkWf7zwPlcBlbeA_aem_XXofAY-ay0syx043L5BLvw" class="me-4" style="text-decoration: none; color: white;" target="_blank">Brosur</a></li>
            			<li><a href="" class="me-4" style="text-decoration: none; color: white;">Panduan</a></li>
            		</ul>
            	</div>
            	<div class="me-5">
            		<p class="text-center mt-1">© 2024 TIM IT PPIB</p>
            	</div>
            </footer>


            <div class="modal fade" id="detailProgramPendidikan" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-secondary" id="exampleModalLabel">Pendaftaran Santri Baru</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
<div class="modal-body">
                    <div class="row mb-3">
                        <div class="col-md-8">
                            <div>
                                <span class="fw-semibold">PEMBUKAAN PROGRAM PENDIDIKAN (Putra dan Putri)</span>
                                <ul class="text-secondary">
                                    <li>Program TK TAHFIZH</li>
                                    <li>Program SD BILINGUAH</li>
                                    <li>Program SMP dan MTS</li>
                                    <li>Program SMA dan MA</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <img src="https://lh5.googleusercontent.com/p/AF1QipMnvLLieVur8fZEE0qY8b-LWTgqcpf-etDo5_Sq=w408-h306-k-no" alt="Gambar Pondok" width="150"
                                class="rounded">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <div class="col-md-8">
                            <div>
                                <span class="fw-semibold">PELAKSANAAN TEST MASUK</span>
                                <p class="text-secondary">Seluruh test dilaksanakan dalam 2 Gelombang <br>
                                    Test
                                    dilaksanakan secara ONLINE menggunakan media ZOOM meeting</p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <img src="https://img.antaranews.com/cache/730x487/2020/08/20/IMG_0098.jpg" alt="Gambar Pondok" width="150"
                                class="rounded">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <div class="col-md-8">
                            <div>
                                <span class="fw-semibold">MATERI UJIAN SELEKSI</span>
                                <ul>
                                    <li>Membaca Al Qur’an dan Tulis Arab</li>
                                    <li>Tes wawancara anak dan wawancara orangtua</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <img src="https://scontent.fmlg16-1.fna.fbcdn.net/v/t39.30808-6/399219372_741110998033602_2170725576008554610_n.jpg?stp=c342.0.1365.1365a_dst-jpg_s206x206&_nc_cat=100&ccb=1-7&_nc_sid=50ad20&_nc_eui2=AeFWrV5IGO6AqGuEZ6eWZv_dO0d-5pTsLCc7R37mlOwsJyt2n0I7aZyoSfBi-tDYip3Dsx8Id7kOq4IsuFyhQuXd&_nc_ohc=gaONd5lqy1AQ7kNvgEE8QWy&_nc_zt=23&_nc_ht=scontent.fmlg16-1.fna&_nc_gid=AQRiTXPxABtPCk42NrbbYHV&oh=00_AYB7pb7cLJHEHsHTcA3u_MjSrWzgjsnqjGxFGDaRvnC-wQ&oe=673C70F9" alt="Gambar Pondok" width="150"
                                class="rounded">
                        </div>
                    </div>
                </div>
                </div>
            </div>
            </div>

<div class="modal fade" id="detailJadwalKegiatan" tabindex="-1" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-secondary" id="exampleModalLabel">Jadwal Pelaksanaan PSB</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="row mb-3">
                        <div class="col-md-8">
                            <div>
                                <span class="fw-semibold">1. Pendaftaran Online</span>
                                <p class="text-secondary">Pendaftaran dilaksanakan pada: <br>
                                        Gel 1: 21 November - 24 November 2025 <br>
                                        Gel 2: 1 Februai - 4 Maret 2025 <br> melalui website <a href="http://localhost:8070/pendaftaran"
                                    class="text-decoration-none text-primary">https://psb.daarulquranistiqomah</a></p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <img src="https://scontent.fmlg16-1.fna.fbcdn.net/v/t39.30808-6/298621082_3013095435648995_7345129981216140240_n.jpg?stp=c315.0.810.810a_dst-jpg_s206x206&_nc_cat=109&ccb=1-7&_nc_sid=8b96af&_nc_eui2=AeExpGOLkXvyR5wEXToaUm-p9hAXDNyrN6T2EBcM3Ks3pGuZpdiK7tg5euGv8hjNK5ITZMh-Zm5QNxsWRPIIxezm&_nc_ohc=YgS73NuhAcwQ7kNvgGCPyUk&_nc_zt=23&_nc_ht=scontent.fmlg16-1.fna&_nc_gid=AUzsAXdWRiW7snf88lNwf62&oh=00_AYAj_QhvqtPQp57x4P9uOhv4SSznbolgRzQCISifs9oQeA&oe=673C981E" alt="Gambar Pondok" width="150"
                                class="rounded">
                        </div>
                    </div>
                    <div class="row mb-3">
                        <div class="col-md-8">
                            <div>
                                <span class="fw-semibold">2. Pelaksanaan Test Masuk</span>
                                <p class="text-secondary">Gel 1: 26-29 Desember 2025<br> Gel 2: 13-18 Maret 2025 <br> (Test seleksi dilaksanakan secara ONLINE dengan
                                    kuota
                                    sebanyak 100 peserta per hari).</p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <img src="https://scontent.fmlg16-1.fna.fbcdn.net/v/t39.30808-6/271738407_2862177990740741_2560153557144834086_n.jpg?stp=c188.0.488.488a_dst-jpg_s206x206&_nc_cat=101&ccb=1-7&_nc_sid=50ad20&_nc_eui2=AeG2Vs7WVnUHEzU-cxfxFizt0Xmjc99eVwHReaNz315XAf0CJVwYcIHHs3rpQylnMFYytXEw1BEQifeDIWkGmIEa&_nc_ohc=642w7dLq7swQ7kNvgHuulQD&_nc_zt=23&_nc_ht=scontent.fmlg16-1.fna&_nc_gid=AUhop87O8T2aG3MKs-gQxaC&oh=00_AYDP29eZ8WwKpMf52ujqPgQJ02eQhz85V7YxKG2uEGawxA&oe=673C86B8" alt="Gambar Pondok" width="150"
                                class="rounded">
                        </div>
                    </div>
                    <div>
                        <span class="fw-semibold">4. Pengumuman Hasil Seleksi</span>
                        <p class="text-secondary">Gel 1: 9-31 Januari 2025 <br>
                                                Gel 2: 3-29 April 2025
                        </p>
                    </div>
                    <div>
                        <p class="text-secondary">Catatan : Seluruh kegiatan akan mengikuti protokol kesehatan sesuai
                            ketentuan dari pemerintah.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="detailPersyaratan" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 text-secondary" id="exampleModalLabel">Persyaratan Test Masuk</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="row mb-3">
                        <div class="col-md-12">
                            <div>
                                <span class="fw-semibold">SYARAT UTAMA PENDAFTARAN :</span>
                                <ol class="text-secondary">
                                    <li>Telah duduk dikelas terakhir SD/MI/sederajat untuk Program SMP & MTS</li>
                                    <li>Telah duduk dikelas terakhir SMP/MTs/sederajat untuk program SMA & MA</li>
                                    <li>Tidak mempunyai riwayat penyakit menular dan berbahaya.</li>
                                    <li>Menandatangani surat pernyataan penyanggupan wali santri bermaterai dan diupload
                                    </li>
                                    <li>Mengisi formulir online secara lengkap dan benar melalui laman https://psb.daarulquranistiqomah
                                    </li>
                                    <li>Membayar biaya pendaftran untuk program TK TAHFIZH sebesar Rp.75.000,-</li>
                                    <li>Membayar biaya pendaftran untuk program SD Bilingual sebesar Rp.90.000,-</li>
                                    <li>Membayar biaya pendaftran untuk program SMP & MTS sebesar Rp.100.000,-</li>
                                    <li>Membayar biaya pendaftran untuk program SMA & MA sebesar Rp.120.000,-</li>
                                    <li>
                                        Menguplod berkas :
                                        <ul type="disc" class="text-secondary">
                                            <li>Akte Kelahiran</li>
                                            <li>Kartu Keluarga</li>
                                            <li>KTP Orangtua/Wali</li>
                                            <li>Ijazah</li>
                                            <li>Raport Pendidikan Terakhir</li>
                                            <li>Pas foto terbaru dengan 80% wajah dengan latar belakang merah</li>
                                            <li>Surat Keterangan Sehat</li>
                                        </ul>
                                    </li>
                                </ol>
                            </div>
                        </div>
                    </div>
                    <div>
                        <p class="text-secondary">Seluruh persyaratan yang harus di upload / diunggah ke website
                            pendaftaran
                            harus sesuai format yang ditentukan</p>
                    </div>
                </div>
                </div>
            </div>
            </div>


            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
        """
    



#     @http.route('/pesantren_pendaftaran/pesantren_pendaftaran/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pesantren_pendaftaran.listing', {
#             'root': '/pesantren_pendaftaran/pesantren_pendaftaran',
#             'objects': http.request.env['pesantren_pendaftaran.pesantren_pendaftaran'].search([]),
#         })

#     @http.route('/pesantren_pendaftaran/pesantren_pendaftaran/objects/<model("pesantren_pendaftaran.pesantren_pendaftaran"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pesantren_pendaftaran.object', {
#             'object': obj
#         })

class UbigPendaftaranController(http.Controller):
    @http.route('/pendaftaran', type='http', auth='public')
    def pendaftaran_form(self, **kwargs):
        # Render form pendaftaran HTML
        pendidikan_list = request.env['ubig.pendidikan'].sudo().search([])
        return request.render('pesantren_pendaftaran.pendaftaran_form_template', {
            'pendidikan_list': pendidikan_list,
        })

    @http.route('/pendaftaran/submit', type='http', auth='public', methods=['POST'], csrf=True)
    def pendaftaran_submit(self, **post):
        # Ambil data dari form
        nama                   = post.get('nama')
        nik                    = post.get('nik')
        email                  = post.get('email')
        password               = post.get('password')
        jenjang_id             = post.get('jenjang_id')
        gender                 = request.params.get('gender')
        kota_lahir             = post.get('kota_lahir')
        tanggal_lahir_str      = request.params.get('tanggal_lahir')
        # Mengonversi format tanggal dd/mm/yyyy menjadi date
        tanggal_lahir          = datetime.datetime.strptime(tanggal_lahir_str, '%d/%m/%Y').date()
        alamat                 = post.get('alamat')
        provinsi_id            = request.params.get('provinsi_id')
        kota_id                = request.params.get('kota_id')
        kecamatan_id           = request.params.get('kecamatan_id')
        golongan_darah         = request.params.get('golongan_darah')
        kewarganegaraan        = request.params.get('kewarganegaraan')
        nisn                   = post.get('nisn')
        anak_ke                = post.get('anak_ke')
        jml_saudara_kandung    = post.get('jml_saudara_kandung')
        cita_cita              = post.get('cita_cita')

        # Data Orang Tua - Ayah
        nama_ayah              = post.get('nama_ayah')
        ktp_ayah               = post.get('ktp_ayah')
        tanggal_lahir_ayah     = post.get('tanggal_lahir_ayah')
        telepon_ayah           = post.get('telepon_ayah')
        pekerjaan_ayah         = request.params.get('pekerjaan_ayah')
        penghasilan_ayah       = request.params.get('penghasilan_ayah')
        email_ayah             = post.get('email_ayah')
        kewarganegaraan_ayah   = request.params.get('kewarganegaraan_ayah')
        pendidikan_ayah        = request.params.get('pendidikan_ayah')

        # Data Orang Tua - Ibu
        nama_ibu               = post.get('nama_ibu')
        ktp_ibu                = post.get('ktp_ibu')
        tanggal_lahir_ibu      = post.get('tanggal_lahir_ibu')
        telepon_ibu            = post.get('telepon_ibu')
        pekerjaan_ibu          = request.params.get('pekerjaan_ibu')
        penghasilan_ibu        = request.params.get('penghasilan_ibu')
        email_ibu              = post.get('email_ibu')
        kewarganegaraan_ibu    = request.params.get('kewarganegaraan_ibu')
        pendidikan_ibu         = request.params.get('pendidikan_ibu')
        
        # Data Wali
        wali_nama              = post.get('wali_nama') if post.get('wali_nama') else ''
        wali_tmp_lahir         = post.get('wali_tmp_lahir') if post.get('wali_tmp_lahir') else ''
        wali_tgl_lahir         = post.get('wali_tgl_lahir') if post.get('wali_tgl_lahir') else None
        wali_telp              = post.get('wali_telp') if post.get('wali_telp') else ''
        wali_email             = post.get('wali_email') if post.get('wali_email') else ''
        wali_hubungan          = post.get('wali_hubungan') if post.get('wali_hubungan') else ''

        # Data Pendidikan
        asal_sekolah           = post.get('asal_sekolah')
        alamat_asal_sek        = post.get('alamat_asal_sek')
        telp_asal_sek          = post.get('telp_asal_sek')
        status_sekolah_asal    = request.params.get('status_sekolah_asal')
        npsn                   = post.get('npsn')

        # Data Berkas
        akta_kelahiran         = request.params.get('akta_kelahiran')
        kartu_keluarga         = request.params.get('kartu_keluarga')
        ijazah                 = request.params.get('ijazah')
        surat_kesehatan        = request.params.get('surat_kesehatan')
        pas_foto               = request.params.get('pas_foto')
        raport_terakhir        = request.params.get('raport_terakhir')
        ktp_ortu               = request.params.get('ktp_ortu')
        skhun                  = request.params.get('skhun')
        
        # Simpan data ke model ubig.pendaftaran
        pendaftaran = request.env['ubig.pendaftaran'].sudo().create({
            'name'                   : nama,
            'nik'                    : nik,
            'email'                  : email,
            'password'               : password,
            'jenjang_id'             : int(jenjang_id),
            'gender'                 : gender,
            'kota_lahir'             : kota_lahir,
            'tanggal_lahir'          : tanggal_lahir,
            'alamat'                 : alamat,
            'provinsi_id'            : provinsi_id,
            'kota_id'                : kota_id,
            'kecamatan_id'           : kecamatan_id,
            'golongan_darah'         : golongan_darah,
            'kewarganegaraan'        : kewarganegaraan,
            'nisn'                   : nisn,
            'anak_ke'                : anak_ke,
            'jml_saudara_kandung'    : jml_saudara_kandung,
            'cita_cita'              : cita_cita,

            # Data Orang Tua - Ayah
            'nama_ayah'              : nama_ayah,
            'ktp_ayah'               : ktp_ayah,
            'tanggal_lahir_ayah'     : tanggal_lahir_ayah,
            'telepon_ayah'           : telepon_ayah,
            'pekerjaan_ayah'         : pekerjaan_ayah,
            'penghasilan_ayah'       : penghasilan_ayah,
            'email_ayah'             : email_ayah,
            'kewarganegaraan_ayah'   : kewarganegaraan_ayah,
            'pendidikan_ayah'        : pendidikan_ayah,

            # Data Orang Tua - Ibu
            'nama_ibu'               : nama_ibu,
            'ktp_ibu'                : ktp_ibu,
            'tanggal_lahir_ibu'      : tanggal_lahir_ibu,
            'telepon_ibu'            : telepon_ibu,
            'pekerjaan_ibu'          : pekerjaan_ibu,
            'penghasilan_ibu'        : penghasilan_ibu,
            'email_ibu'              : email_ibu,
            'kewarganegaraan_ibu'    : kewarganegaraan_ibu,
            'pendidikan_ibu'         : pendidikan_ibu,
            
            # Data Wali
            'wali_nama'              : wali_nama,
            'wali_tmp_lahir'         : wali_tmp_lahir,
            'wali_tgl_lahir'         : wali_tgl_lahir,
            'wali_telp'              : wali_telp,
            'wali_email'             : wali_email,
            'wali_hubungan'          : wali_hubungan,

            # Data Pendidikan
            'asal_sekolah'           : asal_sekolah,
            'alamat_asal_sek'        : alamat_asal_sek,
            'telp_asal_sek'          : telp_asal_sek,
            'status_sekolah_asal'    : status_sekolah_asal,
            'npsn'                   : npsn,

            # Data Berkas
            'akta_kelahiran'         : akta_kelahiran.read() if akta_kelahiran else False,
            'kartu_keluarga'         : kartu_keluarga.read() if kartu_keluarga else False,
            'ijazah'                 : ijazah.read() if ijazah else False,
            'surat_kesehatan'        : surat_kesehatan.read() if surat_kesehatan else False,
            'pas_foto'               : pas_foto.read() if pas_foto else False,
            'raport_terakhir'        : raport_terakhir.read() if raport_terakhir else False,
            'ktp_ortu'               : ktp_ortu.read() if ktp_ortu else False,
            'skhun'                  : skhun.read() if skhun else False,
            'state'                  : 'draft'  # set status awal menjadi 'terdaftar'
        })

        pendaftaran_id = pendaftaran.id

        # Redirect ke halaman sukses atau halaman lain yang diinginkan
        return request.redirect(f'/pendaftaran/success?id={pendaftaran_id}')

    @http.route('/pendaftaran/success', type='http', auth='public')
    def pendaftaran_success(self, **kwargs):
        # Menangkap ID pendaftaran dari URL
        pendaftaran_id = request.params.get('id')

        # Cek apakah ID ada
        if not pendaftaran_id:
            return "ID pendaftaran tidak ditemukan."

        # Mengambil data pendaftaran berdasarkan ID
        pendaftaran = request.env['ubig.pendaftaran'].sudo().browse(int(pendaftaran_id))

        # Cek apakah record pendaftaran ditemukan
        if not pendaftaran.exists():
            return "Data pendaftaran tidak ditemukan."

        return request.render('pesantren_pendaftaran.pendaftaran_success_template', {
            'pendaftaran': pendaftaran,
        })
    
class PesantrenLogin(http.Controller):
    @http.route('/psblogin', auth='public')
    def index(self, **kw):
        return request.render('pesantren_pendaftaran.pendaftaran_login_template')

class PesantrenCetakPembayaran(http.Controller):
    @http.route('/pendaftaran/cetak', type='http', auth='public')
    def pendaftaran_cetak(self, **kwargs):
        # Menangkap ID pendaftaran dari URL
        pendaftaran_id = request.params.get('id')

        # Cek apakah ID ada
        if not pendaftaran_id:
            return "ID pendaftaran tidak ditemukan."

        # Mengambil data pendaftaran berdasarkan ID
        pendaftaran = request.env['ubig.pendaftaran'].sudo().browse(int(pendaftaran_id))

        # Cek apakah record pendaftaran ditemukan
        if not pendaftaran.exists():
            return "Data pendaftaran tidak ditemukan."

        return request.render('pesantren_pendaftaran.pendaftaran_cetak_form_pembayaran_template', {
            'pendaftaran': pendaftaran,
        })

class PesantrenPsbBantuan(http.Controller):
    @http.route('/bantuan', auth='public')
    def index(self, **kw):
        return """
                <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Bantuan - Daarul Qur'an Istiqomah</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" integrity="sha512-Kc323vGBEqzTmouAECnVceyQqyqdsSiqLQISBL29aUW4U/M7pSPA/gEUZQqv1cwx4OnYxTxve5UMg5GT6L4JJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />

                <style>

                    body {
                        background: linear-gradient(to bottom left, #065c5c 18%, #f5e505 100%) !important;
                    }

                    .offcanvas.offcanvas-end {
                        
                        width: 250px; /* Lebar kustom untuk offcanvas */
                    }
                    
                    .offcanvas .nav-link {
                        color: #ffffff; /* teks warna putih */
                    }
                    
                    .offcanvas .btn-close {
                        position: absolute;
                        top: 10px;
                        right: 10px;
                        filter: invert(1);
                    }

                    .timeline {
                        position: relative;
                        padding: 20px 0;
                    }

                    .timeline::before {
                        content: '';
                        position: absolute;
                        left: 5px;
                        top: 50px;
                        bottom: 0;
                        width: 4px;
                        background: white;
                    }

                    .timeline-item {
                        position: relative;
                        margin-left: 50px;
                        margin-bottom: 40px;
                    }

                    .timeline-icon {
                        position: absolute;
                        left: -63px;
                        top: 20px;
                        width: 40px;
                        height: 40px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        border-radius: 50%;
                        color: #fff;
                        font-size: 18px;
                        box-shadow: 0px 3px 20px rgba(0, 0, 0, 0.5);
                    }

                    .timeline-icon::after {
                        content: "";
                        position: absolute;
                        top: 50%;
                        left: 84%;  /* Mengarahkan panah ke ikon */
                        border-width: 15px;
                        border-style: solid;
                        border-color: transparent transparent transparent white;  /* Panah segitiga mengarah ke ikon */
                        transform: translateY(-50%) rotate(180deg);
                    }

                    .timeline-content {
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }

                    .judul {
                        height: 81px;
                        display: flex;
                        align-items: end;
                    }

                    .teks-judul {
                        height: 72px;
                    }

                    .background {
                        background: linear-gradient(to bottom left, #065c5c 18%, #f5e505 100%) !important;
                    }

                    a.effect {
                        transition: .1s !important;
                    }

                    a.effect:hover {
                        box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
                    }

                    /* Desain Dropdown */
                    .dropdown {
                        position: relative;
                    }

                    .dropdown-link {
                        cursor: pointer;
                    }

                    .dropdown-content {
                        display: none;
                        position: absolute;
                        top: 100%;
                        right: 0;
                        background-color: #ffffff;
                        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
                        border-radius: 5px;
                        min-width: 150px;
                        z-index: 1;
                        overflow: hidden;
                    }

                    .dropdown-content a {
                        color: #333;
                        padding: 10px 15px;
                        display: block;
                        text-decoration: none;
                        transition: background-color 0.2s;
                    }

                    .dropdown-content a:hover {
                        background-color: #f1f1f1;
                    }

                    /* Menampilkan dropdown saat hover */
                    .dropdown:hover .dropdown-content {
                        display: block;
                        animation: fadeIn 0.3s;
                    }

                    /* Animasi fade-in */
                    @keyframes fadeIn {
                        from {
                        opacity: 0;
                        transform: translateY(-10px);
                        }
                        to {
                        opacity: 1;
                        transform: translateY(0);
                        }
                    }

                </style>
                
            </head>
            <body>

            <nav class="navbar navbar-expand-lg" style="height: 65px;">
                <div class="container-fluid">
                    <a class="navbar-brand ms-5 text-white fw-semibold" href="/psb">
                        <img src="https://i.ibb.co.com/f9j819p/1731466812700.png" alt="1731466812700" width="50" alt="Logo Pesantren">
                        Daarul Qur'an Istiqomah
                    </a>
                    <button class="navbar-toggler ms-auto" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item me-3">
                                <a class="nav-link text-white" href="/pendaftaran"><i class="fa-solid fa-note-sticky me-2"></i>Pendaftaran</a>
                            </li>
                            <li class="nav-item me-3">
                                <a class="nav-link text-white" href="/web/login"><i class="fa-solid fa-fingerprint me-2"></i>Login</a>
                            </li>
                            <li class="nav-item me-3">
                                <a class="nav-link text-white" href="/bantuan"><i class="fa-solid fa-lock me-2"></i>Bantuan</a>
                            </li>
                            <li class="nav-item dropdown">
                                <a href="#" class="dropdown-link nav-link text-white"><i class="fa-solid fa-bullhorn me-2"></i>Pengumuman</a>
                                <div class="dropdown-content">
                                    <a href="/pengumuman/sd-mi">SD / MI</a>
                                    <a href="/pengumuman/smp-mts">SMP / MTS</a>
                                    <a href="/pengumuman/sma-ma">SMA / MA</a>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="offcanvas offcanvas-end background" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                <a class="navbar-brand mt-1 text-white fw-semibold" href="/pendaftaran" style="display: flex; flex-direction: column; align-items: center;">
                    <img src="https://i.ibb.co.com/f9j819p/1731466812700.png" alt="1731466812700" width="50" alt="">
                    Daarul Qur'an Istiqomah
                </a>
                <div class="offcanvas-body">
                    <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                        <li class="nav-item me-3">
                            <a class="nav-link text-white" href="/pendaftaran"><i class="fa-solid fa-note-sticky me-2"></i>Pendaftaran</a>
                        </li>
                        <li class="nav-item me-3">
                            <a class="nav-link text-white" href="/web/login"><i class="fa-solid fa-fingerprint me-2"></i>Login</a>
                        </li>
                        <li class="nav-item me-3">
                            <a class="nav-link text-white" href="/bantuan"><i class="fa-solid fa-lock me-2"></i>Bantuan</a>
                        </li>
                            <li class="nav-item dropdown">
                                <a href="#" class="dropdown-link nav-link text-white"><i class="fa-solid fa-bullhorn me-2"></i>Pengumuman</a>
                                <div class="dropdown-content">
                                    <a href="/pengumuman/sd-mi">SD / MI</a>
                                    <a href="/pengumuman/smp-mts">SMP / MTS</a>
                                    <a href="/pengumuman/sma-ma">SMA / MA</a>
                                </div>
                            </li>
                    </ul>
                </div>
            </div>

            <div class="container mt-5 mb-5">
            <div class="row">
                <!-- Timeline -->
                <div class="col-lg-6 mb-5">
                <div class="timeline">
                    <!-- Panduan Pendaftaran Online -->
                    <div class="timeline-item">
                    <div class="timeline-icon bg-danger">
                        <i class="fa-solid fa-briefcase text-white"></i>
                    </div>
                    <div class="timeline-content bg-white rounded p-3">
                        <span class="badge text-bg-danger text-uppercase mb-2">Panduan Pendaftaran Online</span>
                        <p>Panduan pendaftaran online dapat didownload dengan klik link di bawah ini :</p>
                        <div class="ratio ratio-16x9 my-4">
                        <iframe src="https://youtu.be/OiPEDy0Sv1U?si=8tm9xvqPE36NgfaP" title="YouTube video player" allowfullscreen></iframe>
                        </div>
                        <a href="https://psb.bukhari.or.id/assets/img/panduan_gabung_gambar_jadi_pdf.pdf" target="_blank" class="text-decoration-none fs-5" style="color: purple;">
                        <i class="fa-solid fa-download text-dark me-1"></i>Panduan cara menggabungkan beberapa foto menjadi file pdf
                        </a>
                    </div>
                    </div>

                    <!-- Alur Pendaftaran Santri Baru -->
                    <div class="timeline-item">
                    <div class="timeline-icon bg-success">
                        <i class="fa-solid fa-puzzle-piece text-white"></i>
                    </div>
                    <div class="timeline-content bg-white rounded p-3">
                        <span class="badge text-bg-success text-uppercase mb-3">Alur Pendaftaran Santri Baru</span>
                        <ul>
                        <li>Buka website <a href="#" class="text-decoration-none" style="color: purple;">https://psb.daarukquranistiqomah.or.id/</a></li>
                        <li>Klik menu daftar dan isikan data yang tersedia.</li>
                        <li>Login di <a href="#" class="text-decoration-none" style="color: purple;">https://psb.daarulquranistiqomah.or.id/login</a></li>
                        <li>Upload berkas yang dipersyaratkan dan bukti pembayaran.</li>
                        <li>Tunggu verifikasi maksimal 3 hari.</li>
                        <li>Login kembali dan pilih tanggal tes.</li>
                        <li>Ikuti tes seleksi online menggunakan aplikasi ZOOM meeting.</li>
                        <li>Lihat hasil tes di <a href="#" class="text-decoration-none" style="color: purple;">https://psb.daarulquranistiqomah.or.id/login</a></li>
                        <li>Setelah pembayaran daftar ulang, tunggu pengumuman serah terima santri baru.</li>
                        </ul>
                    </div>
                    </div>

                    <!-- Video Profil -->
                    <div class="timeline-item">
                    <div class="timeline-icon bg-info">
                        <i class="fa-solid fa-fingerprint text-white"></i>
                    </div>
                    <div class="timeline-content bg-white rounded p-3">
                        <span class="badge text-bg-info text-white text-uppercase">Video Profil Ponpes Daarul Qur'an Istiqomah</span>
                        <div class="ratio ratio-16x9 my-4">
                        <iframe width="437" height="315" src="https://www.youtube.com/embed/VfMmhPHh9Ek" title="" frameborder="0" allowfullscreen></iframe>
                        </div>
                    </div>
                    </div>
                </div>
                </div>

                <!-- Informasi Kontak -->
                <div class="col-lg-6">
                <div class="bg-white rounded p-3 text-center">
                    <span style="font-size: 60px; font-weight: bold;">"</span>
                    <div class="text-secondary mb-4">
                    <span>Pondok Pesantren Daarul Qur'an Istiqomah</span><br>
                    <span>Jl. Ambawang, RT.03/RW.01, Karang Taruna, Kec. Pelaihari, Kabupaten Tanah Laut, Kalimantan Selatan 70815 </span><br>
                    <span>Telp/Whatsapp: <a href="#" class="text-decoration-none" style="color: purple;">(+62 271) 858199</a></span><br>
                    <span>Email: <a href="#" style="color: purple;">daarulquranistiqomah@gmail.com</a></span>
                    </div>
                    <div class="text-secondary mb-4">
                    <span>Informasi PSB & Konsultasi Pendidikan:</span><br>
                    <a href="#" class="text-decoration-none" style="color: purple;">+62 812 7812 9773</a><br>
                    <span>Informasi PSB & Konsultasi Pendidikan:</span><br>
                    <a href="#" class="text-decoration-none" style="color: purple;">+62 896 3203 3096</a><br>
                    <span>Informasi Keuangan:</span><br>
                    <a href="#" class="text-decoration-none" style="color: purple;">+62 822 2733 1234</a>
                    </div>
                    <h5>Silahkan hubungi kami</h5>
                    <span class="text-uppercase" style="color: purple;">@daqubanat_</span>
                </div>
                </div>
            </div>
            </div>

            <footer class="text-white p-2" style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div class="ms-5">
                    <ul style="list-style-type: none; display: flex; text-transform: uppercase; font-size: 13px;" class="fw-semibold">
                        <li><a href="/psb" class="me-4" style="text-decoration: none; color: white;">Home</a></li>
                        <li><a href="/beranda" class="me-4" style="text-decoration: none; color: white;" target="_blank">Info Pondok</a></li>
                        <li><a href="https://drive.google.com/drive/mobile/folders/1EYat5411joyoOmH_DkJ3g2DeJKgyyuBQ?usp=share_link&fbclid=IwY2xjawGflGlleHRuA2FlbQIxMQABHTusVv9hD3VRDSLW9-671QhOL86e3KMv30smsAYW0DHkkWf7zwPlcBlbeA_aem_XXofAY-ay0syx043L5BLvw" class="me-4" style="text-decoration: none; color: white;" target="_blank">Brosur</a></li>
                        <li><a href="" class="me-4" style="text-decoration: none; color: white;">Panduan</a></li>
                    </ul>
                    </ul>
                </div>
                <div class="me-5">
                    <p class="text-center mt-1">© 2024 TIM IT PPIB</p>
                </div>
            </footer>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            </body>
            </html>
        """


# class PendaftaranController(http.Controller):

#     @http.route('/pendaftaran/step1', type='http', auth='public', methods=['GET', 'POST'], csrf=True)
#     def pendaftaran_step1(self, **post):
#         if request.httprequest.method == 'POST':
#             jenjang_id = post.get('jenjang_id')
#             if jenjang_id:
#                 jenjang_id = int(jenjang_id)

#             # Simpan data dari Step 1 ke session
#             request.session['pendaftaran_data'] = {
#                 'name'                   : post.get('nama'),
#                 'nik'                    : post.get('nik'),
#                 'email'                  : post.get('email'),
#                 'nomor_hp'               : post.get('nomor_hp'),
#                 'jenjang_id'             : jenjang_id
#             }
#             # Redirect ke Step 2
#             return request.redirect('/pendaftaran/step2')
        
#         # Ambil data dari session jika ada, untuk mengisi form secara default
#         pendaftaran_data = request.session.get('pendaftaran_data', {})

#         # Mengambil opsi jenjang pendidikan dari model `ubig.pendidikan`
#         jenjang_options = request.env['ubig.pendidikan'].sudo().search([])

#         # Render template untuk Step 1
#         return request.render('pesantren_pendaftaran.pendaftaran_step1', {
#             'jenjang_options': jenjang_options,
#         })

#     @http.route('/pendaftaran/step2', type='http', auth='public', csrf=True, methods=['GET', 'POST'])
#     def pendaftaran_step2(self, **post):
#         pendaftaran_data = request.session.get('pendaftaran_data', {})  # Ambil data dari session

#         if post:
#             # Tambahkan data Step 2 ke session jika ada data yang diposting
#             pendaftaran_data.update({
#                 'gender'                : post.get('gender'),
#                 'kota_lahir'            : post.get('kota_lahir'),
#                 'tanggal_lahir'         : post.get('tanggal_lahir'),
#                 'alamat'                : post.get('alamat'),
#                 'provinsi_id'           : int(post.get('provinsi_id')) if post.get('provinsi_id') else False,
#                 'kota_id'               : int(post.get('kota_id')) if post.get('kota_id') else False,
#                 'kecamatan_id'          : int(post.get('kecamatan_id')) if post.get('kecamatan_id') else False,
#                 'nisn'                  : post.get('nisn'),
#                 'anak_ke'               : post.get('anak_ke'),
#                 'jml_saudara_kandung'   : post.get('jml_saudara_kandung'),
#                 'cita_cita'             : post.get('cita_cita')
#             })
#             # Simpan kembali data ke session setelah diperbarui
#             request.session['pendaftaran_data'] = pendaftaran_data

#             # Redirect ke Step 3
#             return request.redirect('/pendaftaran/step3')

#         # Render template untuk Step 2 dengan data yang ada di session
#         return request.render('pesantren_pendaftaran.pendaftaran_step2', {
#             'pendaftaran_data': pendaftaran_data
#         })

#     @http.route('/pendaftaran/step3', type='http', auth='public', csrf=True, methods=['GET', 'POST'])
#     def pendaftaran_step3(self, **post):
#         if post:
#             pendaftaran_data = request.session.get('pendaftaran_data', {})
#             pendaftaran_data.update({
#                 # Data Orang Tua - Ayah
#                 'nama_ayah'              : post.get('nama_ayah'),
#                 'ktp_ayah'               : post.get('ktp_ayah'),
#                 'tanggal_lahir_ayah'     : post.get('tanggal_lahir_ayah'),
#                 'telepon_ayah'           : post.get('telepon_ayah'),
#                 'pekerjaan_ayah'         : post.get('pekerjaan_ayah'),
#                 'penghasilan_ayah'       : post.get('penghasilan_ayah'),
#                 'email_ayah'             : post.get('email_ayah'),
#                 'kewarganegaraan_ayah'   : post.get('kewarganegaraan_ayah'),
#                 'pendidikan_ayah'        : post.get('pendidikan_ayah'),


#                 # Data Orang Tua - Ibu
#                 'nama_ibu'               : post.get('nama_ibu'),
#                 'ktp_ibu'                : post.get('ktp_ibu'),
#                 'tanggal_lahir_ibu'      : post.get('tanggal_lahir_ibu'),
#                 'telepon_ibu'            : post.get('telepon_ibu'),
#                 'pekerjaan_ibu'          : post.get('pekerjaan_ibu'),
#                 'penghasilan_ibu'        : post.get('penghasilan_ibu'),
#                 'email_ibu'              : post.get('email_ibu'),
#                 'kewarganegaraan_ibu'    : post.get('kewarganegaraan_ibu'),
#                 'pendidikan_ibu'         : post.get('pendidikan_ibu'),
                
#                 # Data Wali
#                 'wali_nama'              : post.get('wali_nama'),
#                 'wali_tmp_lahir'         : post.get('wali_tmp_lahir'),
#                 'wali_tgl_lahir'         : post.get('wali_tgl_lahir'),
#                 'wali_telp'              : post.get('wali_telp'),
#                 'wali_email'             : post.get('wali_email'),
#                 'wali_hubungan'          : post.get('wali_hubungan')
#             })
#             request.session['pendaftaran_data'] = pendaftaran_data
#             return request.redirect('/pendaftaran/step4')
        
#         return request.render('pesantren_pendaftaran.pendaftaran_step3')

#     @http.route('/pendaftaran/step4', type='http', auth='public', csrf=True, methods=['GET', 'POST'])
#     def pendaftaran_step4(self, **post):
#         if post:
#             pendaftaran_data = request.session.get('pendaftaran_data', {})
#             pendaftaran_data.update({
#                 # Data Pendidikan
#                 'asal_sekolah'            : post.get('asal_sekolah'),
#                 'alamat_asal_sek'         : post.get('alamat_asal_sek'),
#                 'telp_asal_sek'           : post.get('telp_asal_sek'),
#                 'status_sekolah_asal'     : post.get('status_sekolah_asal'),
#                 'npsn'                    : post.get('npsn')
#             })
#             request.session['pendaftaran_data'] = pendaftaran_data
            
#             # Simpan data akhir ke database
#             request.env['ubig.pendaftaran'].sudo().create(pendaftaran_data)
#             return request.redirect('/pendaftaran/success')
        
#         return request.render('pesantren_pendaftaran.pendaftaran_step4')
    
#     @http.route('/pendaftaran/success', type='http', auth='public', csrf=True)
#     def pendaftaran_success(self, **post):
#         # Hapus data session setelah sukses
#         request.session.pop('pendaftaran_data', None)
#         return request.render('pesantren_pendaftaran.pendaftaran_success')
# class CustomLogin(http.Controller):
#     @http.route('/web/login', type='http', auth='public', website=True, csrf=True)
#     def web_login(self, redirect=None, **post):
#         if request.httprequest.method == 'POST':
#             nomor_pendaftaran = post.get('nomor_pendaftaran')
#             nik = post.get('nik')

#             user = request.env['ubig.pendaftaran'].sudo().search([
#                 '&',
#                 ('nomor_pendaftaran', '=', nomor_pendaftaran),
#                 ('nik', '=', nik)
#             ], limit=1)

#             if user:
#                 return request.redirect('/web')


# class CustomAuthController(http.Controller):

#     @http.route('/send-login-email', type='json', auth='public', methods=['POST'], csrf=True)
#     def send_login_email(self, **post):
#         email = request.params.get('email')
#         password = request.params.get('nik')
#         nik = request.params.get('nik')

#         # Buat nama default dari email atau gunakan fallback
#         if email:
#             name = email.split('@')[0]
#         else:
#             name = f'Pengguna {nik}' if nik else 'Pengguna Tanpa Nama'

#         # Cek apakah pengguna sudah ada
#         user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)

#         if not user:
#             try:
#                 # Buat pengguna baru dengan mengisi field `name`
#                 user = request.env['res.users'].sudo().create({
#                     'login': email,
#                     'password': password,
#                     'name': name,  # Pastikan field `name` terisi
#                 })

#                 # Mengirim email menggunakan SMTP bawaan Odoo
#                 email_values = {
#                     'subject': 'Informasi Login Odoo Anda',
#                     'email_to': email,
#                     'body_html': f'<p>Ini adalah email dan password Anda untuk login:</p>'
#                                  f'<p>Email: {email}</p>'
#                                  f'<p>Password: {password}</p>',
#                 }

#                 mail = request.env['mail.mail'].sudo().create(email_values)
#                 mail.send()  # Mengirim email secara langsung

#                 return {'success': True}

#             except Exception as e:
#                 return {'success': False, 'error': f'Error: {str(e)}'}

#         return {'success': False, 'error': 'Pengguna sudah terdaftar'}

class CustomAuthController(http.Controller):

    @http.route('/send-login-email', type='http', auth='public', methods=['POST'], csrf=True)
    def send_login_email(self, **post):
        email = post.get('email')
        name = post.get('name')
        nik = post.get('nik')

        # Mengambil digit tengah dari NIK dan mengacak password
        if nik:
            mid_nik = nik[len(nik)//4 : len(nik)//2]  # Ambil digit tengah
            password = hashlib.sha256(mid_nik.encode('utf-8')).hexdigest()
        else:
            password = 'password123'  # Fallback jika NIK tidak tersedia

        # Cek apakah pengguna sudah ada
        user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)

        if not user:
            try:
                # Buat pengguna baru dengan mengisi field `name`
                user = request.env['res.users'].sudo().create({
                    'login': email,
                    'password': password,
                    'name': name,
                })

                # Mengirim email menggunakan SMTP bawaan Odoo
                email_values = {
                    'subject': 'Informasi Login Odoo Anda',
                    'email_to': email,
                    'body_html': f'<p>Ini adalah email dan password Anda untuk login sistem pesantren:</p>'
                                 f'<p>Email: {email}</p>'
                                 f'<p>Password: {password}</p>',
                }

                mail = request.env['mail.mail'].sudo().create(email_values)
                mail.send()

                return """
                        <script>
                            alert('Akun Berhasil dibuat.');
                            window.location.href = '/web/login';
                        </script>
                """

            except Exception as e:
                return """
                        
                """


class PendaftaranSeleksiSdMi(http.Controller):
    @http.route('/pengumuman/sd-mi', type='http', auth='public')
    def pengumuman(self, **kwargs):
        # Render form pendaftaran HTML
        calon_santri = request.env['ubig.pendaftaran'].sudo().search([('state', 'in', ['diterima', 'ditolak']), ('jenjang_id.jenjang', '=', 'sdmi')])
        return request.render('pesantren_pendaftaran.pendaftaran_seleksi_sdmi_template', {
            'santri': calon_santri,
        })


class PendaftaranSeleksiSmpMts(http.Controller):
    @http.route('/pengumuman/smp-mts', type='http', auth='public')
    def pengumuman(self, **kwargs):
        # Render form pendaftaran HTML
        calon_santri = request.env['ubig.pendaftaran'].sudo().search([('state', 'in', ['diterima', 'ditolak']), ('jenjang_id.jenjang', '=', 'smpmts')])
        return request.render('pesantren_pendaftaran.pendaftaran_seleksi_smpmts_template', {
            'santri': calon_santri,
        })
    
class PendaftaranSeleksiSmaMa(http.Controller):
    @http.route('/pengumuman/sma-ma', type='http', auth='public')
    def pengumuman(self, **kwargs):
        # Render form pendaftaran HTML
        calon_santri = request.env['ubig.pendaftaran'].sudo().search([('state', 'in', ['diterima', 'ditolak']), ('jenjang_id.jenjang', '=', 'smama')])
        return request.render('pesantren_pendaftaran.pendaftaran_seleksi_smama_template', {
            'santri': calon_santri,
        })



