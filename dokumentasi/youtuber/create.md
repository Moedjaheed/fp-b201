# Dokumentasi Create Youtuber
## **Method :**  `POST`
## **Route :**  `127.0.0.1:5005/api`
## **Authentication :**  `JWT`
Endpoint ini berfungsi untuk menambahkan data youtuber baru. Autentikasi dilakukan agar hanya admin yang dapat menambahkan data baru.

## **Body :** 
```json
{
    "rank" : "[number]",
    "channel" :"[String]",
    "subs" :"[number]",
    "views" :"[number]",
    "count" :"[number]",
    "category" :"[String]",
    "started" :"[number]"
}
```
#### *Example :* 
```json
{
            "id": 1001,
            "rank": 100000,
            "channel": "T-Series",
            "subs": 234000000,
            "views": 21290027155,
            "count": 1851512,
            "category": "Music",
            "started": 2006
}
```

## **Response :**

- ### **Success**
    Status Code : 200 OK
    ```json
    {
    "msg" : "Data berhasil dimasukan",
    "data": [
        {
            "id": 1001,
            "rank": 100000,
            "channel": "T-Series",
            "subs": 234000000,
            "views": 21290027155,
            "count": 1851512,
            "category": "Music",
            "started": 2006
        }]
    }
    ```
