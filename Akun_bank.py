### SIMULASI BANK ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B                             TUGAS           : 5 

from Error_bank import DepositError, WithdrawError


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount, ):
        if amount > 0:
            self.balance += amount
            print (f"\n- Setoran uang sejumlah Rp.{self.balance} atas nama {self.owner} berhasil!!!")
            return self.balance
            
        
        else:
            raise DepositError("\nERROR: Jumlah setoran harus lebih dari nol!!")
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\n- Penarikan uang sejumlah Rp.{amount} atas nama {self.owner} berhasil!!!")
            return self.balance
        
        else:
            raise WithdrawError("\nERROR: Saldo tidak mencukupi atau jumlah penarikan tidak valid!!")
        
    def get_balance(self):
        return self.balance
    