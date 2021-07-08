import smtplib
from tkinter import messagebox


class EmailSlicer:
    def __init__(self):
        pass

    def send_message(self, email_adress, password, receiver, subject, body):
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(email_adress, password)

                message = f"Assunto: {subject}\n\n{body}"

                smtp.sendmail(email_adress, receiver, message)

                messagebox.showinfo("Sucesso!", "Parabéns, seu email foi enviado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", "Por favor, verifique se seu email ou senha estão corretos!")
