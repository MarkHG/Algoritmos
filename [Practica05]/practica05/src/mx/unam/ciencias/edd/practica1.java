package mx.unam.ciencias.edd;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

/**
 * Práctica 9: Trayectoria mínima y algoritmo de Dijkstra.
 */
public class practica1 {

    private static String cadena;

    private static String v;
  /*  private static Lista<VerticeGrafica<String>> ELista2 = new Lista<VerticeGrafica<String>>();*/





    private static void uso() {
        System.err.println("El uso es: java -jar practica8.jar <Nombre Archivo>");
        System.exit(1);
    }

    public static Grafica<String> CreaGrafica(String archivo){
      Grafica<String> g = new Grafica<String>();
      String cadena;

    try {

      FileReader f = new FileReader(archivo);
      BufferedReader b = new BufferedReader(f);

      String primeraLinea=b.readLine();
      String[] partsAux = primeraLinea.split(", |,");
      v = partsAux[0];

      /*ZONE TRIKI*/


      for(String s: partsAux){
        g.agrega(s);
      }

      /*for(String ss: partsAux){
        VerticeGrafica<String>  verticeLista = g.vertice(ss);
        ELista2.agrega(verticeLista);

      }Habilitar par inconexas*/


      while((cadena = b.readLine())!=null) {
        String[] parts = cadena.split(", |,");
        if(cadena.length()<=5){
            String part1 = parts[0];
            String part2 = parts[1];
            g.conecta(part1,part2);

        }

      }
      b.close();
    }catch (IOException ioe) {
      System.out.printf("No pude cargar del archivo \"%s\".\n",
      archivo);
      System.exit(1);
    }
      return g;
  }


    @SuppressWarnings("unchecked")
    public static Lista<VerticeGrafica<String>> MinRecursivo(Lista<VerticeGrafica<String>> original, VerticeGrafica<String> vertice, Grafica f){

      Lista<VerticeGrafica<String>> copiat= new Lista<VerticeGrafica<String>>();

      for(VerticeGrafica<String> elem: original){

        if (f.sonVecinos( vertice.getElemento(), elem.getElemento()) == false){
          copiat.agrega(elem);
        }
      }

      return copiat;

    }





    public static void main(String[] args) {



      if (args.length != 2)
            uso();

        String nombreArchivo = args[0];

        Grafica<String> g = new Grafica<String>();
        g = CreaGrafica(nombreArchivo); //aqui se crea tu grafica


        //VAMOS A EJECUTAR DFS DE CLASE GRAFICA
        /* DFS de la clase */

        if(args[1].equals("dfs")){

          for (String s: g) {
            System.out.println(s);

          }
        while(g.esVacio() != true){
          Lista<String> a= new Lista<String>();
          cadena="";
          g.dfs(v, (v) -> cadena +=v.getElemento()+",");
          System.out.println("----------------");
          String[] parts=cadena.split(",");
          System.out.println(cadena);



          for (String s:parts ) {
            a.agrega(s);

            }


          System.out.println(a.toString());

          for (String v : a) {
            g.elimina(v);

            }

          Lista<String> res=new Lista<String>();
          for(String s: g){
            res.agrega(s);
          }
          if(res.esVacio() == true){
            break;
          }else{

            v= res.getPrimero();
          }

            System.out.println(g.getElementos());

      }

    }
    else if(args[1].equals("bfs")) {
      while(g.esVacio() != true){
        Lista<String> b = new Lista<String>();
        cadena="";
        g.bfs(v, (v) -> cadena +=v.getElemento()+",");
        System.out.println("----------------");
        String[] parts=cadena.split(",");
        System.out.println(cadena);

        String cadenaristas= g.bfsAristas(v);
        System.out.println("----------------");



        System.out.println("hola"+ cadenaristas);





        for (String s:parts ) {
          b.agrega(s);

        }


        System.out.println(b.toString());

        for (String v : b) {
          g.elimina(v);

          }

          Lista<String> res=new Lista<String>();
          for(String s: g){
            res.agrega(s);
          }
          if(res.esVacio() == true){
            break;
          }else{

            v= res.getPrimero();
          }

          System.out.println(g.getElementos());
        }


        }
        else{
          System.out.println("hola");
        }
      }







    //System.out.println(a.toS



    }
