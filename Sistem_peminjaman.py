### SIMULASI BANK ###

### NAMA    : M. MUSTHOFA MASYHUR           DOSEN PENGAMPU  : MUHAMMAD AFFANDES, S.T, M.T.
### NIM     : 12550111055                   MATA KULIAH     : PEMROGRAMAN BERORIENTASI OBJEK
### KELAS   : B                             TUGAS           : 5   

from Pegawai_bank import TellerBank
from Nasabah import CustomerBank

class LoanSystem:
    def __init__(self):
        self.list_loan = []

    def add_loan(self, teller:TellerBank, customer:CustomerBank, loan_date, loan_total, pay_date):
        customer.account.balance += loan_total
        print(f"\n Pinjaman Rp.{loan_total} telah ditambahkan ke rekening {customer.name}!")
        print(f"Dikonfirmasi oleh Teller {teller.name}")
 
        data_loan = {
            "teller_name":teller.name,
            "loan_date":loan_date,
            "name":customer.name,
            "acc_number":customer.acc_number,
            "loan_total":loan_total,
            "pay_date":pay_date,
            "loan_balance":loan_total,
            "pay_history":[],
            "state":"Belum Lunas"
        } 

        self.list_loan.append(data_loan)
        print(f"Daftar pinjaman telah ditambahkan!!\n")

    def pay_loan(self, customer: CustomerBank, pay_amount):
        pay_amount = pay_amount

        for data in self.list_loan:
            if data["acc_number"] == customer.acc_number:

                if data["state"] == "Lunas":
                    print("\nTransaksi ditolak!! pinjaman ini sudah lunas.")
                    return
                
                customer.account.withdraw(pay_amount)

                data ["loan_balance"] -= pay_amount
                data ["pay_history"].append(f"Bayar Rp.{pay_amount:,.0f}")

                    
                if data["loan_balance"] <= 0:
                    data["state"] = "Lunas"

                    if data["loan_balance"] < 0:
                        customer.account.deposit(abs(data["loan_balance"]))
                        data["loan_balance"] = 0

                print(f"Pembayaran berhasil! Sisa pinjaman anda: Rp.{data['loan_balance']}")
                return
            
        print(f"\nData pinjaman {customer.name} tidak ditemukan!")


    def view_list(self):
        print(f"\n=== RIWAYAT PINJAMAN NASABAH ===\n")

        for a in self.list_loan:
            print(f"{'Teller Bank':<15} : {a['teller_name']}")
            print(f"{'Hari/tanggal':<15} : {a['loan_date']}")
            print(f"{'Nama':<15} : {a['name']}")
            print(f"{'No.Rekening':<15} : {a['acc_number']}")
            print(f"{'Jumlah Pinjaman':<15} : {a['loan_total']}")
            print(f"{'Status Pinjaman':<15} : {a['state']}")

            if a['pay_history']:
                print(f"{'Riwayat bayar':<15} : {', '.join(a['pay_history'])}")
            
            else:
                print(f"{'Riwayat bayar':<15} : Belum ada pembayaran!")
        
            print("-" * 45)