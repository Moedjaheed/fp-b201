# Dokumentasi topSubscriber API
topSubscriber API adalah sebuah API yang akan memberikan data - data Top 1000 youtuber.
Terdapat 1000 data channel youtube teratas di dalamnya.
API ini dibuat dengan menggunakan Python dan SQL.
Di dalam API ini terdapat 2 jenis endpoint, yaitu yang terbuka untuk umum dan yang memerlukan autentikasi berupa token JTW.
Untuk melakukan request, dapat dilakukan dengan mengakses ip berikut :
**IP** : (`127.0.0.1`)

Dalam API ini terdapat beberapa endpoint yang dapat dikelompokkan menjadi 2 :

  * Endpoint User (`127.0.0.1/api/login`)
  * Endpoint Youtuber (`127.0.0.1/api`)
  
# Endpoint User
Endpoint ini menghandle mengenai data user
  * Post Login User : `POST 127.0.0.1/api/login`
  
# Endpoint Youtuber
Endpoint ini menghandle mengenai data youtuber
  * Create Data Youtuber (NEED AUTHENTICATION) : `POST 127.0.0.1/api`
  * Get Semua Youtuber : `GET 127.0.0.1/api`
  * Update Youtuber (NEED AUTHENTICATION) : `PUT 127.0.0.1/api`
  * Delete Youtuber (NEED AUTHENTICATION) : `DELETE 127.0.0.1/api`
  * Delete Semua Youtuber (NEED AUTHENTICATION) : `DELETE 127.0.0.1/api`
