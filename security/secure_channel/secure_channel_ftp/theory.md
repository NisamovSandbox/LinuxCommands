## Conceptos básicos de encriptación

### Tipos de encriptación
#### Encriptación simétrica
La encriptación simétrica utiliza **una única clave** tanto para encriptar como para desencriptar la información.  
Esta clave debe ser compartida de forma segura entre el emisor y el receptor.

**Características principales:**
- Alta velocidad de procesamiento.
- Adecuada para grandes volúmenes de datos.
- Menor seguridad en el intercambio de la clave.

#### Encriptación asimétrica
La encriptación asimétrica emplea **dos claves distintas pero relacionadas matemáticamente**: una pública y una privada.

**Características principales:**
- Mayor nivel de seguridad.
- No requiere compartir la clave privada.
- Más lenta que la encriptación simétrica.

### Tipos de claves
Las llaves utilizan representaciones **binarias o ASCII** para su almacenamiento y uso criptográfico.

#### Clave pública
- Se utiliza para **encriptar** la información.
- Puede ser compartida libremente.
- Los datos encriptados con esta llave solo pueden ser desencriptados con la llave privada correspondiente.

#### Clave privada
- Se utiliza para **desencriptar** la información.
- Debe mantenerse estrictamente confidencial.
- En algoritmos como **RSA**, suele tener longitudes de **2048 o 4096 bits** para garantizar la seguridad.

**Ejemplo (RSA):**  
Un mensaje encriptado con una llave pública RSA de 4096 bits solo puede ser desencriptado con su llave privada asociada.

### Passphrase
Una passphrase es una frase o conjunto de palabras utilizado para **proteger una llave privada**.

**Funciones principales:**
- Añade una capa adicional de seguridad.
- Evita el uso no autorizado de la llave privada.
- Suele ser más larga y segura que una contraseña convencional.
