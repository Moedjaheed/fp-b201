# Dokumentasi Login
## **Method :**  `POST`
## **Route :**  `127.0.0.1/api/login`
## **Authentication :**  `None`
Endpoint ini berfungsi untuk login dan mendapatkan access token untuk pertama kali.
## **Body :** 
```json
{
    "username" : "[Anything]",
    "password" : "[superuser]"
}
```
#### *Example :* 
```json
{
    "username" : "asep",
    "password" : "superuser"
}
```

## **Response :**

- ### **Success**
    Status Code : 200 OK
    ```json
    {
        "msg": "Anda berhasil login!",
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFzZXAiLCJleHAiOjE2ODA0ODY1MTd9.GwX4MnK_i3ToV4AulMo_-G6SHXH_2Cde-tKgsqj5VHE"
    }
    ```
- ### **Error**
    Status Code : 400 Bad Request

    Error :
    - Username atau Password bukan "superuser"
    ```json
    {
        "msg": "Silahkan login!"
    }
    ```

