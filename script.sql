select * from Users where id=1111

select * from Users where email='<variable_email>' AND pass='<variable_pass>'

--input: "a@gmail.com" || "megustamaria"
select * from Users where email='a@gmail.com' AND pass='megustamaria'
-- output: Rodrigo

--input: "' OR '' = '" || "' OR '' = '"
select * from Users where email='' OR '' = '' AND pass='' OR '' = ''
-- output: all users

-- condicionamiento de flujo basado en midlewares
-- validacion del request
-- ejecucion

{
    id: 11111,
    name: "Rodrigo",
    email: "a@gmail.com",
    pass: "megustamaria"
}

{
    "id": 22222,
    "name": "Maria",
    "email": "b@gmail.com",
    pass: "nomegustgarodrigo"
}

207.230.11.49 != 181.56.68.4

jwt

// quien hizo la peticion?
-- 403
-- 200
// getDataByUser(22222)