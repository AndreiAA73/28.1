from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'Т'
    first_name_31_char = 'Аннрееееееееееееейаааааааааааан'
    last_name_1_char = 'Т'
    last_name_31_char = 'Аннрееееееееееееейаааааааааааан'
    password_21_char = 'FFFylhtq7390qwertyuiopasd'
    password_no_Lower = 'FFylhtq7390'
    password_9_char = 'Fylhtq73'
    password_not_contain_digit = "Fylhtqaan"
    xss = '<script>alert(123)</script>'
    email_without_domain = 'test@.ru'
    invalid_phoneNumber = '+7098765432'

class Valid_Data:
    valid_first_name = 'Андрей'
    valid_last_name = 'Андреев'
    valid_password = 'FFFylhtq7390'
    valid_phoneNumber = '+79370340333'
