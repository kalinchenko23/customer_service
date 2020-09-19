import smtplib
with smtplib.SMTP('smtp.gmail.com', 587 ) as emailpdf:
    smtp.starttls()
    smtp.ehlo()
    smtp.login("kalinchenko.max@gmail.com","ttzmuceljetrzesd")