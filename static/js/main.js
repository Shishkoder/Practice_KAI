function CheckForm(element) {
    /* 
        * Данная функция выполняет валидацию данных в регистрационной форме
    */
    var FirstName = document.getElementById('FirstName').value;
    var LastName = document.getElementById('LastName').value;
    var UserName = document.getElementById('UserName').value;
    var Email = document.getElementById('Email').value;
    var Password = document.getElementById('Password').value;
    var PasswordConfirmation = document.getElementById('PasswordConfirmation').value;

    if(Number(FirstName.length) > 0){
        if(Number(LastName.length) > 0){
            if(Number(UserName.length) > 0){
                if(Number(Email.length) > 0){
                    if(Number(Password.length) >= 8){
                        if(Password != PasswordConfirmation){
                            console.error("Пароли должны совпадать");
                            alert("Пароли должны совпадать");
                            return false;
                        }
                    } else{
                        console.error("Пользователь не ввел свой пароль");
                        alert("Вы оставили поле Пароль пустым");
                        return false;
                    }
                }else{
                    console.error("Пользователь не ввел свою почту");
                    alert("Вы оставили поле почта пустым");
                    return false;
                }
            }else{
                console.error("Пользователь не ввел имя пользователя");
                alert("Вы оставили поле Имя пользователя пустым");
                return false;
            }
        }else{
            console.error("Пользователь не вел свою фамилию");
            alert("Вы оставили поле Фамилия пустым");
            return false;
        }
    }
    else{
        console.error("Пользователь не ввел свое имя");
        alert("Вы оставили поле Имя пустым");
        return false;
    }
};