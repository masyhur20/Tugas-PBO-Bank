### SIMULASI BANK ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B                             TUGAS           : 5 

import unittest

from Akun_bank import BankAccount
from Sistem_peminjaman import LoanSystem
from Nasabah import CustomerBank
from Pegawai_bank import TellerBank
from Error_bank import DepositError,WithdrawError

class TestBankSystem(unittest.TestCase):
    
    def setUp(self):
        self.akun_ethan = BankAccount("Ethan Hunt", 5000000)
        self.nasabah_ethan = CustomerBank("Ethan Hunt", 5000000001, self.akun_ethan)
        self.teller_sarah = TellerBank("Sarah", "T001")
        self.system_loan_test = LoanSystem()

    def test_1_add_loan(self):
        self.system_loan_test.add_loan(self.teller_sarah, self.nasabah_ethan, "12-03-2026", 1000000, "12-05-2026")
        self.assertEqual(self.nasabah_ethan.account.balance, 6000000)
        self.assertEqual(len(self.system_loan_test.list_loan), 1)

    def test_2_pay_loan(self):
        self.system_loan_test.add_loan(self.teller_sarah, self.nasabah_ethan, "12-03-2026", 1000000, "12-05-2026")
        self.system_loan_test.pay_loan(self.nasabah_ethan, 1000000)
        self.assertEqual(self.system_loan_test.list_loan[0]['loan_balance'], 0)
        self.assertEqual(self.system_loan_test.list_loan[0]['state'], "Lunas")

    def test_3_pay_without_loan(self):
        self.system_loan_test.pay_loan(self.nasabah_ethan, 60000)
        self.assertEqual(self.nasabah_ethan.account.balance, 5000000)

    def test_4_withdraw_error(self):
        with self.assertRaises(WithdrawError):
            self.nasabah_ethan.account.withdraw(6000000)

    def test_5_deposit_error(self):
        with self.assertRaises(DepositError): 
            self.nasabah_ethan.account.deposit(-50000)

 
if __name__== '__main__':
    unittest.main(verbosity=2)