class PID:
    def __init__(self, kp, ki, kd): # inisialisasi
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.reset()
        
    def update(self, error, dt):
        integral = integral + error * dt # menghitung integral dengan menambahkan error yang dikalikan dengan selisih waktu ke hasil integral sebelumnya
        # integral digunakan untuk nyimpen memori / data tentang apa yg terjadi sebelumnya (buat nge track kondisi masa lalu)
        derivative = (error - self.last_error) / dt # menghitung turunan error dengan membagi selisih error terakhir dengan selisih waktu. 
        # turunan buat nge prediksi masa depan (buat ngitung seberapa cepat perubahan + / - nya error biar tau langkah yg di ambil di step selanjutnya)
        self.last_error = error
        return self.kp * error + self.ki * integral + self.kd * derivative # komponen nya integral ya di kali error dari integral
                                                          # komponen nya derivative (turunan) ya di kali error dari derivative (turunan)
                                                          # komponen nya nilai proporsional (aktual) ya di kali error dari nilai proporsional (aktual)

pid = PID(1, 0.1, 0.01)

pid = PID(1, 0.1, 0.01)
while True:
    error = setpoint - feedback 
    # setpoint = nilai yang diinginkan (tujuan akhir nya)
    # feedback  = nilai yang sebenarnya
    feedback = pid.update(error, dt)
    if error == 0:
        break