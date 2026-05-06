<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/css/style.css">
    <title>Explicacion</title>
    <script src="ejemplo.js"></script>
</head>
<script src="ejemplo.js"></script>
<style>


      /* formas de controlar elementos html desde css:  
      hacerlo por etiquete o elemento (img, h1 p...)
      id (controlo 1 elemento a la vez)
      class (me permite que todo elemento que comparta dicha clase);;*/
   #proyecto-1 img {

   
      border-style: double;
      /*unidades de medida en css:
      px=pixeles que contiene la pantalla
      %= es usado cuando deseo hacer paginas responsivas
      rem
      em
      vh
      ;*/
      padding-right: 20px ; /*redondea el bordel del elemento*/
      border: 20; /* establece un borde personal personalizado*/
       
   }
   

/*
Herencia: hereda componente hijo
*/

section{
   text-align: center;
}
</style>

<body>


    <!--Comentario HTML: 
    Acá se genera el body / cuerpo es donde se escribirá el código de las etiquetas o elementos a manejar-->
    <!--Elementos o etiquetas-->
    <!--Semantica HMTL (SEO) para que el navegador encuentre que hay en la pg.-->
    <header>
      <nav>
    <ul>
    <li><a class="a-encabezado" href="#sobre-mi"></a></li>
     <li><a class="a-encabezado" href="#skills"></a></li>
     <li><a class="a-encabezado" href="#repositorios"></a></li>
     <li><a class="a-encabezado" href="#proyectos"></a></li>
     <li><a class="a-encabezado" href="#contactos"></a></li>
     <li><a class="a-encabezado" href="#team-developer"></a></li>
     <li><a class="a-encabezado" href="#collage"></a></li>
   </ul>
   </nav>


    <br> <!--Salto de linea-->
    <!--- H se usan para los titulos de 1-6 segun importancia, solo un H1 por documento-->
 

    </header>  
     <main>

        <!--Identificación de cada elemento en HTML
         id: permite identificar 1 elemento dentro de la página se recomienda que sea unico para evitar
         que se pueda el enfoque incial
         clase: Busca agrupar varios elementos para controlarlos de forma masiva
         Elemento: para controlar todos aquellos que comparten la misma semantica -->
   <section id="sobre-mi">
      <div id="sobre-mi-texto">
        <h1 style="color: palevioletred;"><span class="tipografia">Saray Jiced David Ortega</span></h1>
        <em>Estudiante</em><strong> Desarrollo de software</strong>
      <p> Desarrolladora java backend en proceso y pausa de profesional en Lenguas Modernas
      </p>
      </div>
      <span class="style"></span> <!--Parrafo-->
      <br><p></p> <!--salto de linea más grande-->
      <!--la imagen puede ser local o por URL-->
      <br>
      <div id="sobre-mi-img">
     <img  id="imagen-personal" src="/software imagen.jpg" alt="">
     </div>
     <button> Descargar CV </button>

    <section id="skills">
      <h2>Skills</h2>

            <article id="blandas">
            <ul>
                 <li> Comunicación asertiva</li>
                 <li>Compromiso</li>
                 <li>Adaptabilidad al cambio</li>
            </ul>
                <!--Se usa para cosas que no se relacionan entre si pero comparten la misma sección-->
            </article>
      <article id="tecnicas">
         <ol>
            <li> Git/GitHub</li>
            <li>Python</li>
            <li>Pseint </li>
            <li> Python</li>
         </ol>
      </article>
     </section>    
     <!-- Las secciones en HTML hacen referencia a un bloque de contenido que se encarga de mostrar o explicarn un punto fundamental de la página-->   
   <section id="repositorios">    
     <table border="1">
      <thead> 
         <tr>
            <th colspan="4"> PROYECTOS TRABAJADOS</th>
         </tr>
         <tr>
            <th> Item </th>
            <th> Proyecto </th>
            <th> Descripción</th>
            <th> GitHub</th>
         </tr>
     </thead>
      <tbody>
         <tr>
            <td>1</td>
            <td>Drogueria</td>
            <td>Proyecto</td>
            <td> <a href="https://github.com/saraydavidtavera-lgtm/Proyecto_drogueriaequipo"></a></td>
         </tr> 
           <tr>
            <td>2l</td>
            <td>Herramientas</td>
            <td>Proyecto</td>
            <td> <a href="https://github.com/saraydavidtavera-lgtm/taller_githerramientas"></a></td>
         </tr> 
           <tr>
            <td>3</td>
            <td>AromaCapus</td>
            <td>Proyecto</td>
            <td> <a href="https://github.com/saraydavidtavera-lgtm/Examen_AromaCampus"></a></td>
         </tr> 
      </tbody>

      </table>
   </section>

   <section id="proyectos">
<article id="proyecto-1">
   <img class="img-personalizada" src="/software imagen.jpg">
   <h3>Herramientas</h3>
   <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Labore beatae eveniet, ipsa temporibus excepturi ad, suscipit quaerat cumque ab eius, est enim nisi quod animi odit dolores voluptatibus? Possimus, molestiae?</p>
   <button>Ver Proyecto</button>
</article>
<article>
   <img class="img-personalizada" src="/software imagen.jpg">
   <h3>Herramientas</h3>
   <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Labore beatae eveniet, ipsa temporibus excepturi ad, suscipit quaerat cumque ab eius, est enim nisi quod animi odit dolores voluptatibus? Possimus, molestiae?</p>
   <button>Ver Proyecto</button>
</article>
<article>
   <img class="img-personalizada" src="/software imagen.jpg">
   <h3>Herramientas</h3>
   <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Labore beatae eveniet, ipsa temporibus excepturi ad, suscipit quaerat cumque ab eius, est enim nisi quod animi odit dolores voluptatibus? Possimus, molestiae?</p>
   <button>Ver Proyecto</button>
</article>
</section>

<section id="contactos">
   <h2>contactos</h2>
   <form action="/table.html" method="">
      <label for="">Ingrese el nombre: </label>
     <input id="txt.nombre" type="text" placeholder="Ej: Saray David">
     <br>
     <label for=""> Ingrese la edad: </label>
     <input  type="number" id="input.edad" placeholder="Ej: 22">
     <br>
     <label for=""> Ingrese el correo: </label>
     <input id="email" type="txt.email" placeholder="Ej: correo@gmail.com">
     <br>
     <h3>Selecciones sexo</h3>
     <label for="radio.Masculino"> Masculino</label>
     <input type="radio" id="radio.Masculino" name="opciones.sexo">
     <label for="radio.Femenino"> Femenino</label>
     <input type="radio" id="radio.Femenino" name="opciones.sexo">
     <h3>Seleccione nivel de backend </h3>
     <label for="radio.junior"> junior <input type="radio" name="opciones.backend" id="radio.junior">  </label>
     <br>
     <h3> Selecciones los colores de la página </h3>
     <label for="check-azul">Azul <input type="checkbox"></label>
     <label for="check-azul">Rojo <input type="checkbox"></label>
     <label for="check-azul">Amarillo <input type="checkbox"></label>
     <br>
     <input type="date" name="" id="">
     <br>
     <input type="color" name="" id="">
     <br>
     <input type="submit" value="navegar">
   </form>
</section>
     </main>

     <footer> 
        <!---pie de página-->
     </footer>
    <nav>

    </nav>
</body>

</html>
