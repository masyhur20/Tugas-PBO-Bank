### SIMULASI BANK ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B                             TUGAS           : 5 

from Error_bank import DepositError, WithdrawError
from Akun_bank import BankAccount
from Pegawai_bank import TellerBank
from Nasabah import CustomerBank
from Sistem_peminjaman import LoanSystem


# KELAS AKUN BANK
rekening_1 = BankAccount("Ethan Hunt", 0)
rekening_2 = BankAccount("Luther Stickell", 0)
rekening_3 = BankAccount("Benji Dunn", 0)

try:
    nasabah_1 = CustomerBank("Ethan Hunt", 5000000001, account = rekening_1)
    nasabah_1.account.deposit(5000000) # Setor 5 Jt.
    nasabah_1.account.get_balance()

    nasabah_2 = CustomerBank("Luther Stickell", 5000000002, account = rekening_2)
    nasabah_2.account.deposit(3000000) # Setor 3 Jt, Narik 1 Jt. Sisa saldo 2 Jt.
    nasabah_2.account.withdraw(1000000)
    nasabah_2.account.get_balance()

    nasabah_3 = CustomerBank("Benji Dunn", 5000000003, account = rekening_3)
    nasabah_3.account.withdraw(100000) # Narik 100k padahal belum menyetorkan, akan Error.
    nasabah_3.account.get_balance()

except DepositError as a: 
    print(a)

except WithdrawError as b:
    print(b)


# KELAS TELLER BANK
teller_1 = TellerBank("Sarah", "T001")
teller_2 = TellerBank("Neytiri", "T002")


# KELAS SYSTEM PEMINJAMAN
sistem_bank = LoanSystem()

sistem_bank.add_loan(teller_1, nasabah_1, "12-03-2026", 1000000, "12-05-2026") # Ethan minjam 1 Jt. Daftar pinjam ditambahkan.
sistem_bank.add_loan(teller_2, nasabah_2, "12-03-2026", 1000000, "12-05-2026") # Luther minjam 1 Jt. Daftar pinjam ditambahkan. total saldo 3 jt.
#sistem_bank.add_loan(teller_1, nasabah_3, "12-03-2026", 1000000, "12-05-2026")

sistem_bank.pay_loan(nasabah_1, 1000000) # Ethan balekkan pinjaman 1 Jt. Berhasil.
sistem_bank.pay_loan(nasabah_1, 100000) # Ethan balekkan pinjaman lagi 100k. Otomatis akan ditolak.
sistem_bank.pay_loan(nasabah_3, 1000000) # Benji tidak meminjam tapi dia mengembalikan uang 1 Jt. Akan ditolak.

sistem_bank.view_list() # List Riwayat Pinjaman Nasabah


# KELAS NASABAH BANK
print("\n=== INFORMASI SALDO ===\n")
nasabah_1.show_info()
nasabah_2.show_info()
nasabah_3.show_info()
print("=" * 70)