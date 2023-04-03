# Dokumentasi Delete All Youtuber
## **Method :**  `DELETE`
## **Route :**  `127.0.0.1/api/<id>`
## **Authentication :**  `JWT`
Endpoint ini berfungsi untuk menghapus seluruh data youtuber yang telah ada. Autentikasi dilakukan agar hanya admin yang dapat menghapus data tersebut. 

## **Response :**

- ### **Success**
    Status Code : 200 OK
    ```json
    {
        "msg": "Semua data berhasil di hapus",
        "code": 200
    }
    ```
