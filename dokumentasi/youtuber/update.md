# Dokumentasi Update Pokemon
## **Method :**  `PUT`
## **Route :**  `127.0.0.1/api/<id>`
## **Authentication :**  `JWT`
Endpoint ini berfungsi untuk mengubah data dari youtuber berdasarkan id. Autentikasi dilakukan agar hanya admin yang dapat melakukan perubahan data

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
	"Rank": 1,
	"Channel": "asdfg",
	"Subscribers": "234,000,000",
	"Video Views": "212,900,271,553",
	"Video Count": "18,515",
	"Category": "Music",
	"Started": 2006
}
```

## **Response :**

- ### **Success**
    Status Code : 200 OK
    ```json
    {
    "message": "Edit data berhasil",
    "data": {
        	    "id": 1001,
		    "Rank": 1,
		    "Channel": "asdfg",
		    "Subscribers": "234,000,000",
		    "Video Views": "212,900,271,553",
		    "Video Count": "18,515",
		    "Category": "Music",
		    "Started": 2006
        }
    }   
    ```
