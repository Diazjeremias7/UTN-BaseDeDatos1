**Esquema de BD:**

`PROGRAMA<radio, año, programa, conductor, gerente, frecuencia_radio>`

**Restricciones:**

a. Una radio se transmite por una única frecuencia (frecuencia_radio) en un año
determinado, y puede cambiarla en años diferentes.
b. Cada radio tiene un único gerente por año, pero el mismo gerente puede repetirse en la
misma radio en diferentes años. Y la misma persona puede ser gerente de diferentes
radios durante el mismo año.
c. Un mismo programa puede transmitirse por varias radios y en diferentes años.
d. Un programa transmitido en una radio en un año determinado tiene un solo conductor

### Determinamos las Dependencias Funcionales (DFs):

A partir del esquema y las restricciones dadas, podemos determinar las siguientes dependencias funcionales:

1. **radio, año -> frecuencia_radio**: Cada radio por año tiene una frecuencia de radio.

2. **radio, año -> gerente**: Cada radio tiene un gerente por año.

3. **programa, año -> radio**: Cada programa se transmite en muchas radios por año.

4. **programa, radio, año -> conductor**: Un programa transmitido en una radio en un año determinado tiene un solo conductor.

### Determinamos las Claves Candidatas:

Hay que encontrar un conjunto de atributos que identifican de unicamente a cada fila de la tabla `PROGRAMAS`.

- La combinación de **`radio`, `año`, y `programa`** sirve para identificar de forma única cada registro en la tabla, ya que deterniman **`frecuencia_radio`, `gerente` y `conductor`**

Entonces, la **clave candidata** es:
- (`radio`, `año`, y `programa`)

### Normalizamos hasta la 3FN:

Sacamos las dependencias parciales. Vemos que `(radio, año)` determina `frecuencia_radio` y `gerente`. Por eso, dividimos la relación en las siguientes dos relaciones:

- **RADIO(radio, año, frecuencia_radio, gerente):** donde `(radio, año)` es la clave primaria y `frecuencia_radio` y `gerente` dependen completamente de esta clave.

- **PROGRAMA_RADIO(radio, año, programa, conductor):** donde `(radio, año, programa)` es la clave primaria y `conductor` depende de esta clave.
