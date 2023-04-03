# Dokumentasi Delete Pokemon
## **Method :**  `DELETE`
## **Route :**  `127.0.0.1/api`
## **Authentication :**  `JWT`
Endpoint ini berfungsi untuk menghapus data youtuber yang telah ada. Autentikasi dilakukan agar hanya admin yang dapat menghapus data tersebut. 

## **Response :**

- ### **Success**
    Status Code : 200 OK
    ```json
    {
        "msg": "Data berhasil di hapus",
        "code": 200
    }
    ```
