function CheckForm(element) {
    /* 
        * Данная функция выполняет валидацию данных в регистрационной форме
    */
    var FirstName = document.getElementById('FirstName').value;
    var LastName = document.getElementById('LastName').value;
    var UserName = document.getElementById('UserName').value;
    var Email = document.getElementById('Email').value;
    var Password = document.getElementById('Password').value;
    var PasswordConfirmation = document.getElementById('PasswordConfirmation').value

    if(Number(FirstName.length) > 0){
        if(Number(LastName.length) > 0){
            if(Number(UserName.length) > 0){
                if(Number(Email.length) > 0){
                    if(Number(Password.length) >= 8){
                        if(Password != PasswordConfirmation){
                            console.error("Пароли должны совпадать")
                        }
                    } else{
                        console.error("Пользователь не ввел свой пароль")
                        return false;
                    }
                }else{
                    console.error("Пользователь не ввел свою почту")
                    return false;
                }
            }else{
                console.error("Пользователь не ввел имя пользователя")
                return false;
            }
        }else{
            console.error("Пользователь не вел свою фамилию")
            return false;
        }
    }
    else{
        console.error("Пользователь не ввел свое имя")
        return false;
    }
};