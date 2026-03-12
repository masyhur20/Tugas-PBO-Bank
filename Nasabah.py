### SIMULASI BANK ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B                             TUGAS           : 5   

from Akun_bank import BankAccount

class CustomerBank:
    def __init__(self, name, acc_number, account:BankAccount):
        self.name = name
        self.acc_number = acc_number
        self.account = account

    def show_info(self):
        print(f"Nasabah: {self.name:<15} | Rekening: {self.acc_number} | Saldo: Rp.{self.account.balance:,.0f}")