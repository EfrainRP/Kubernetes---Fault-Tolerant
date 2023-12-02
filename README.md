# Kubernetes

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

## Kubernetes
***Kubernetes*** se utiliza para **orquestar contenedores**, lo que significa que gestiona la implementación, la escalabilidad, la gestión del ciclo de vida y la operación de aplicaciones en contenedores en un entorno informático en la nube o local. Ofreciendo una infraestructura para alojar y coordinar aplicaciones distribuidas en múltiples nodos.

1. ***Orquestación de contenedores***: Permite desplegar, escalar y gestionar contenedores de manera eficiente.
1. ***Autoscalado***: Permite que las aplicaciones se adapten automáticamente a la demanda, aumentando o reduciendo la cantidad de instancias según sea necesario.
1. ***Gestión de recursos***: Controla y asigna recursos como CPU, memoria y almacenamiento para garantizar un rendimiento óptimo de las aplicaciones.
1. ***Balanceo de carga***: Distribuye el tráfico de red de manera equitativa entre los contenedores para mejorar la disponibilidad y el rendimiento.
1. ***Despliegue automatizado***: Facilita la implementación y actualización de aplicaciones sin tiempo de inactividad.

## Ingress
En Kubernetes, ***Ingress*** **es una API que gestiona el acceso externo a los servicios que se ejecutan dentro de un clúster**. Permite exponer servicios HTTP y HTTPS dentro del clúster Kubernetes y proporciona reglas para dirigir el tráfico hacia los servicios correspondientes. Actuando como una capa de entrada para las solicitudes HTTP y HTTPS que llegan desde fuera del clúster hacia los servicios dentro del clúster. Algunas de las funcionalidades que ofrece Ingress incluyen:

1. ***Enrutamiento basado en reglas***: Permite configurar reglas para dirigir el tráfico hacia diferentes servicios basados en criterios como la URL, el nombre del host, los encabezados HTTP, entre otros.
1. ***Terminación de SSL/TLS***: Puede encargarse de la terminación de SSL/TLS (Secure Socket Layer/Transport Layer Security) para las solicitudes HTTPS antes de llegar a los servicios.
1. ***Balanceo de carga***: Ingress puede trabajar con controladores de Ingress (como NGINX Ingress Controller, Traefik, entre otros) para realizar el balanceo de carga entre los servicios expuestos.
1. ***Gestión de múltiples dominios***: Permite definir múltiples dominios y rutas para dirigir el tráfico a diferentes servicios dentro del clúster Kubernetes.
1. ***Configuración flexible***: Proporciona una forma flexible de configurar las reglas de enrutamiento utilizando recursos declarativos de Kubernetes.

## LoadBalancer (Balanceador de Carga)
Un ***LoadBalancer***  es un componente de red que distribuye el tráfico entrante entre varios servidores, dispositivos de red o recursos computacionales. Su función principal es mejorar la disponibilidad y el rendimiento de un sistema al distribuir la carga de trabajo de manera equitativa entre los distintos recursos disponibles.

- Los proveedores de servicios en la nube, como AWS, Azure o Google Cloud Platform, ofrecen servicios de Load Balancer que se integran con Kubernetes. Estos Load Balancers pueden configurarse para distribuir el tráfico entre los nodos del clúster Kubernetes.

- Los controladores de Ingress en Kubernetes también pueden trabajar con Load Balancers para gestionar y distribuir el tráfico entrante hacia los servicios internos del clúster, proporcionando así escalabilidad, redundancia y alta disponibilidad.

## Ejemplo

Para poder realizar esta actividad fue necesario instalar ***Docker Desktop***, para Windows desde la pagina principal de [**Docker**](https://docs.docker.com/desktop/install/windows-install/). Una vez instalado la aplicacion (y verificado que funcione correctamente, iniciando el programa), procederemos a activar la opcion de ***kubernetes*** dentro de Doker Desktop, por lo que empezara a actualizarse la aplicacion con esta nueva modalidad.

Para empezar a utilizar lo basico de **kubernetes** deberemos conocer los comandos basicos:
- `kubectl apply -f [file.yaml]`, nos permitira aplicar la implementación de la aplicacion ya configurada del archivo .yaml.
- `kubectl get deployments`, podremos observar que nuestras implementaciones, ya enumeradas, esten funcionando correctamente.
- `kubectl get services`, podremos observar que nuestrso servicios esten funcionando correctamente.
- `kubectl get all`, podremos observar que todo nuestras implementaciones, servicios y replicas esten funcionando bien.
- `kubectl delete -f [file.yaml]`, eliminrará los recursos del archivo yaml.

![commands](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Kubernetes/Images/commands.jpg)

Este sitio Web nos permite escribir palabras para asi irlas guardando en una BD, pero se utilizo kubernetes para poder entender el comportamiento y ventajs que nos ofrece esta tecnologia. Ya que nos permite administrar los contenedores que vayamos creando, haciendolo escalable nuestro proyecto.

Asi que para este ejemplo tenemos 5 replicas, locual significa que tenemos 5 "mini-sistemas" que tienen la misma pagina con el mismo funcionamiento. Lo cual, ***kubernetes*** nos ayuda a orquestar/administrar nuestros contenedores por si llega a haber problema con alguna conexión.

Si descargas estos archivos de esta carpeta, y ejecutas los comandos:
1. `docker build -t node-app` 
1. `kubectl apply -f demo.yaml`

A continuación, podras entrar desde tu navegador con el url: ***localhost:30001***, con el cual nuestra implementacion gestionara los contenedores para redirigirnos a uno concretamente, facilitando el acceso a nuestro sitio Web.
Podras pobrar con los comandos explicados anteriormente, para poder observar el comportamiento que tiene los kubernetes en este sistema/sitio Web, lo cual nos ofrece ventajas para evitar caidas de pagina.

## Conclución
Kubernetes es una herramienta que nos permite el desarrollo y despliegue de aplicaciones modernas, que ofrece capacidades avanzadas de orquestación, escalabilidad y gestión de contenedores. Mediante esta actividad, tuve que realizar bastante investigación para entender como funciona correctamente Kubernetes ya que tienes que conocer no solo los comandos de Kubernetes sino que tambien la sintaxis y aplicaciones de sus propios archivos yaml. Pero al aplicar y probar los ejemplos sencillos de las paginas de Kubernetes y de DigitalOcean, pude realizar correctamente la actividad.