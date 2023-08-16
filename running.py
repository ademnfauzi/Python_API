import multiprocessing
import os

def run_script(script):
    """Fungsi untuk menjalankan file Python"""
    os.system(f"python {script}")

if __name__ == '__main__':
    # Buat sebuah Pool dengan jumlah proses sesuai jumlah CPU yang tersedia
    pool = multiprocessing.Pool()

    # Buat sebuah list dengan nama file Python yang akan dijalankan
    scripts = ["index.py", "index2.py"]

    # Jalankan setiap file Python pada proses yang berbeda
    pool.map(run_script, scripts)

    # Tunggu sampai semua proses selesai dijalankan
    pool.close()
    pool.join()
