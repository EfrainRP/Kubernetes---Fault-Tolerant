# Rancher & Istio

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Andrea Gaspar Miramontes** CÓDIGO: **221350664**

**Miguel Alejandro Lomeli Haro** CÓDIGO: ****

**Maria Fernanda Barroso Monroy** CÓDIGO: **218128918**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)


## Rancher
Rancher es una plataforma de gestión de Kubernetes que permite a los equipos de DevOps ejecutar cargas de trabajo en contenedores. Es una pila de software completa que aborda los desafíos operativos y de seguridad de la gestión de múltiples clústeres de Kubernetes, mientras proporciona herramientas integradas para ejecutar cargas de trabajo en contenedores. Rancher es una plataforma de gestión de contenedores de código abierto que se construye para organizaciones que implementan contenedores en producción. 

### Rancher vs Docker

Rancher y Docker son dos herramientas diferentes que se utilizan en la gestión de contenedores. Docker es una plataforma de contenedores que permite a los desarrolladores crear, distribuir y ejecutar aplicaciones en contenedores. Por otro lado, Rancher es una plataforma de gestión de Kubernetes que permite a los equipos de DevOps ejecutar cargas de trabajo en contenedores. 

En cuanto a cuál es mejor, depende de las necesidades específicas de su organización. Si su organización tiene limitaciones presupuestarias y necesita soporte integrado de escalado de infraestructura, Rancher puede ser una buena opción. Por otro lado, si su organización necesita seguridad avanzada, soporte de CLI y controles de acceso granulares, Docker Enterprise puede ser una mejor opción.

### Rancher Desktop

Rancher Desktop es una aplicación de escritorio de código abierto que proporciona Kubernetes, gestión de contenedores y utilidades integradas en el escritorio. Con Rancher Desktop, puede ejecutar un clúster K3s ligero dentro de una máquina virtual. La aplicación también incluye los entornos de ejecución de contenedores containerd y dockerd. 

Con Rancher Desktop, puede hacer lo siguiente:
- Configurar Kubernetes usando la interfaz de usuario sencilla de Rancher Desktop.
- Elegir la versión de Kubernetes que desea utilizar.
- Elegir su entorno de ejecución de contenedores preferido.
- Configurar los recursos del sistema para la máquina virtual (en Mac y Linux).
- Reiniciar Kubernetes o el entorno de ejecución de contenedores a su configuración predeterminada con solo presionar un botón.

### Ejemplo Rancher

En anteriores practicas vimos el uso de *Docker* o *Kubernetes* por separado pero ahora vamos a hacer uso de la herramienta de ***Rancher Desktop*** la cual encapsula los dos antes mencionados. Siendo así lo primero a efectuar en la practica es descargar [**Rancher**](https://github.com/rancher-sandbox/rancher-desktop/releases) desde su pagina oficial

*La instalacion puede ser algo lenta pues ademas de descargar e instalar el programa se debe esperar la primera vez que abrimos el programa a que cargué algunos kubernetes que incluye rancher*

Ahora que nos ofrece Rancher: Rancher nos va a permitir hacer uso tanto de kubernetes como de Dockers (o su variante llamada containerd) por lo que podemos hacer uso de los mismos comandos de los cuales solo mencionamos los necesarios para la practica pero puede ver la lista completa aqui <<efra aqui incluye tus repositorios>>

Usaremos el mismo ejemplo de la practica pasada y para hacer uso de el no hace falta más que descargar los archivos que dejamos aqui mismo en el repositorio y ejecutar los siguientes comandos

1. `docker build -t node-app .` 
2. `kubectl apply -f demo.yaml`

Es posible que en caso de que antes contarás con *Docker Desktop* tengas un problema al momento de intentar usar el comando de kubectl. La respuesta a por que se genera este problema incluso se puede ver desde la interfaz de rancher desktop 

![image](https://github.com/EfrainRP/Kubernetes---Fault-Tolerant/assets/142550697/e812e7c0-45e1-43bf-b211-1cec9d2059fe)

El problema es que kubernetes está tratando de hacer uso del contexto de Docker Desktop, por lo que este se debe cambiar por medio del comando

`kubectl config use-context rancher-desktop`

Este pequeño problema ya nos permitió ver una de las funciones de Rancher Desktop la cual es informarnos sobre diagnosticos

Tambien tenemos la posibilidad de ver las imagenes que se encuentran activas por medio de una pestaña, al igual que podemos crearlas de una forma grafica presionando el botón de `Add Image` (solo que aqui una servidora no le entendío ni maiz)

![image](https://github.com/EfrainRP/Kubernetes---Fault-Tolerant/assets/142550697/3f5adbcb-041d-4e65-aafc-378437909af3)

Y al igual que las imagenes que se encuentran activas tambien podemos ver los contenedores que se encuentran activos

![image](https://github.com/EfrainRP/Kubernetes---Fault-Tolerant/assets/142550697/866b7b6e-854f-4f49-abdd-db5f94ffd48c)

Note como ademas de los 5 que nostros creamos tambien existen otros 5 que en descripcion dicen *rancher/mirrored* esto es porque en caso de que eliminemos uno de nuestros contenedores rancher lo va a suplantar con el que tiene en copia

Finalmente para ver el funcionamiento podras entrar desde tu navegador con el url: ***localhost:30001***, con el cual nuestra implementacion gestionara los contenedores para redirigirnos a uno concretamente, facilitando el acceso a nuestro sitio Web.
Podras pobrar con los comandos explicados anteriormente, para poder observar el comportamiento que tiene los kubernetes en este sistema/sitio Web, lo cual nos ofrece ventajas para evitar caidas de pagina.

## Istio

Primero descargamos la ultima version de Istio, que en nuestr caso fue istio-1.20.0-win.zip, esto en la pagina https://github.com/istio/istio/releases.

Abrimos en la barra de tareas, editar "Editar las variables de entorno del sistema". Dentro de las variables del usuario editamos la variable path y agregamos una nueva entrada a la carpeta `bin`

![image](https://github.com/EfrainRP/Kubernetes---Fault-Tolerant/blob/main/Images/imagen%201.jpg)

Despues en el cmd ejecutamos el comando `istioctl`

![image](https://github.com/EfrainRP/Kubernetes---Fault-Tolerant/blob/main/Images/imagen%202.jpg)

Finamlmente ya que se ejecuto el comando anterior, ahora se tiene que instalar el perfil demo mediante el siguiente comando `istioctl manifest apply --set profile=demo`

![image](https://github.com/EfrainRP/Kubernetes---Fault-Tolerant/blob/main/Images/imagen%203.jpg)

Para visualizar el panel de kiali, primero se tiene que ejecutar los siguiente `kubectl apply -f samples/addons/kiali.yaml` donde tienes que estar dentor de la carpeta de istio en el cmd.

Además de que si queremos ver la grafica del flujo de informacion de nuestra pagina deberemos de instalar otra sub-herramienta de Istio llamada ***"prometheus"***, asi que ejecutaremos el comando `kubectl apply -f samples/addons/prometheus.yaml`.

Y despues de todo lo anterior solo tienes que ejecutar lo siguiente `kubectl dashboard kiali` y ya podras ver el panel de Kiali.

![image](https://github.com/EfrainRP/Kubernetes---Fault-Tolerant/blob/main/Images/imagen%204.jpg)

OWASP TOP 10:
OWASP TOP 10 proyecto abierto de seguridad de aplicaciones web, es una organizacion internacional sin animo de lucro, dedicada a la seguridad de las aplicaciones web. 
Este sistema tiene una estrategia basada en datos de analices de vulnerabilidades, al igual que se basa en la causa y no en la consecuencia. 
Este tambien se basara en la inicidencia y no en la frecuencia es decir que se enofcara en el problema y no en la frecuencia con el que este ocurre. 

Los factores de analisis:
° CWE mapeados.
° Tasa de incidencia.
° Cobertura de prueba.
° CVSS Score total (Daño/Impacto)
° Impacto de la vulnerabilidad.

Los tres principales metodos de analisis, son:
° Broken Access Control: 
Los controles de acceso permiten hacer cumplir las reglas de modo que los usuarios no pueden actuar fuera de sus permisos permitidos.
° Fallos Criptograficos:
Protege de robo y acceso no autorizado a la informacion sensible y que requiere proteccion adicional (puede ser un sniffer de red viendo el transito).
° Injection + Cross site scripting:
Cuando una aplicacion se vuelve vulnerable a una inyeccion de datos, cuando permite que un codigo externo sea ejecutado al contaminar algun parametro recibido por la aplicacion web, lo cual permite que un atacante tome el control del servidor o robe una gran cantidad de datos confidenciales. Este puede ser por algun dato malicioso que ingresen en la pagina web y se puede observar desde la base de datos. 

Como se puede observar el OWASP TOP 10 ha cambiado y modificado el esquema de un analisis de cibersegurirdad dando por hecho que la injection no es ya no es el mayor problema, ni el mayor enfoque en esta ultima actualizacion de su estructura. 

Para poder aplicar esto dentro de nuestro proyecto hemos decidido utilizar OWASP TOP 10 para buscar alguna vulnerabilidad y de ahi poder mejorar y asegurar nuestro trabajo, basicamente estamos haciendo el trabajo de un hacker de sombrero blanco y parchar nuestros errores de seguridad.   

Para esto encontramos un scan que nos permitira hacerlo, una vez terminando de montar toda nuestra aplicacion esto debera generarnos una ip de donde se encuentra el contenedor y esa es la que analizaremos con ayuda de un OWASP SCANNER ONLINE, tenemos una gran variedad, ejemplo: Acunetix, app scanner, app spider, etc. 



 
