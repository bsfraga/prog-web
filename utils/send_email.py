import smtplib


def send_email_confirmation(cls, email_target, target_public_id):
    EMAIL_ADDRESS = 'spotted.automaticmail@gmail.com'
    EMAIL_PASSWORD = 'Ab102030#'

    with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Confirmação de Cadastro - Spotted'
        body = 'Para finalizar o processo de criação de conta no Spotted, acesse o link:\n'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email_target, EMAIL_ADDRESS, msg )

        return True
